# ai/main.py
import os
import threading
import uuid
import json
from flask import Flask, request, jsonify , send_from_directory
from werkzeug.utils import secure_filename
from whisper_utils import transcrever_audio_real
from gpt_utils import gerar_json_clinico_real, salvar_json
from flask_cors import CORS
AUDIO_DIR = "audio"
TRANSCRIPTS_DIR = "transcripts"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

app = Flask(__name__)
consultas = []  # Lista global simulando banco
CORS(app) 
def processar_consulta(consulta_id, caminho_audio):
    idx = next(i for i, c in enumerate(consultas) if c["id"] == consulta_id)
    consultas[idx]["status"] = "processando"

    # 1️⃣ Transcrição real com Whisper
    try:
        texto = transcrever_audio_real(caminho_audio)
    except Exception as e:
        consultas[idx]["status"] = "erro"
        consultas[idx]["erro"] = str(e)
        return

    # 2️⃣ Geração real do JSON clínico com GPT
    try:
        json_clinico = gerar_json_clinico_real(texto)
    except Exception as e:
        consultas[idx]["status"] = "erro"
        consultas[idx]["erro"] = str(e)
        return

    # 3️⃣ Salvar JSON
    nome_saida = os.path.splitext(os.path.basename(caminho_audio))[0] + ".json"
    caminho_saida = os.path.join(TRANSCRIPTS_DIR, nome_saida)
    salvar_json(json_clinico, caminho_saida)

    # Atualiza status
    consultas[idx]["status"] = "pronto"
    consultas[idx]["arquivo"] = caminho_saida

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    arquivo = request.files["file"]
    filename = secure_filename(arquivo.filename)
    caminho_audio = os.path.join(AUDIO_DIR, filename)
    arquivo.save(caminho_audio)

    consulta_id = str(uuid.uuid4())
    consulta = {
        "id": consulta_id,
        "nome": filename,
        "queixa": "Aguardando processamento...",
        "status": "processando",
        "arquivo": None
    }
    consultas.append(consulta)

    # Processa em background
    thread = threading.Thread(target=processar_consulta, args=(consulta_id, caminho_audio))
    thread.start()

    return jsonify({"status": "ok", "id": consulta_id})

@app.route("/consultas", methods=["GET"])
def listar_consultas():
    return jsonify(consultas)

@app.route("/consulta/<nome_arquivo>", methods=["GET"])
def consulta(nome_arquivo):
    caminho = os.path.join(TRANSCRIPTS_DIR, nome_arquivo)
    if not os.path.exists(caminho):
        return jsonify({"error": "Arquivo não encontrado"}), 404

    with open(caminho, "r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
        except Exception as e:
            return jsonify({"error": f"Erro ao ler JSON: {e}"}), 500

    return jsonify(dados)

def carregar_consultas_existentes():
    for arquivo in os.listdir(TRANSCRIPTS_DIR):
        if arquivo.endswith(".json"):
            caminho = os.path.join(TRANSCRIPTS_DIR, arquivo)
            with open(caminho, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                    consultas.append({
                        "id": str(uuid.uuid4()),
                        "nome_paciente": dados.get("clinico", {}).get("S", {}).get("identificacao", {}).get("nome", "Paciente desconhecido"),
                        "nome": os.path.splitext(arquivo)[0],
                        "queixa": dados.get("clinico", {}).get("S", {}).get("queixa_principal", "Consulta processada"),
                        "status": "pronto",
                        "arquivo": arquivo  # <-- só o NOME do arquivo, não o caminho completo
                    })
                except Exception as e:
                    print(f"Erro ao carregar {arquivo}: {e}")
if __name__ == "__main__":
    carregar_consultas_existentes()
    app.run(port=5000, debug=True)
