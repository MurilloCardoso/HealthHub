# ai/gpt_util.py
import os
import json
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")  # Configure sua API key no ambiente

def gerar_json_clinico_real(texto_transcrito: str) -> dict:

    return {
        {
    "clinico": {
        "S": {
            "identificacao": {
                "nome": "Manuel",
                "data_nascimento": "10/05/1976",
                "idade": 50,
                "sexo": "Masculino",
                "nacionalidade": "Não especificada"
            },
            "queixa_principal": "Dor abdominal inferior associada a febre e tremores.",
            "historia_doenca_atual": "Paciente relata dor iniciada há dois dias, localizada inicialmente próximo ao umbigo e depois irradiando para o pé da barriga e região colateral do abdômen. Refere intensidade de dor de 10/10 quando comprimida. Associada a febre alta (39,5°C) controlada com antitérmico. Relata episódios de tremores e mal-estar. Não houve vômitos significativos. Não há alterações urinárias relatadas."
        },
        "O": {
            "sinais_sintomas": [
                "Dor localizada no abdômen inferior, pior ao toque",
                "Febre alta",
                "Tremores",
                "Sem alterações respiratórias ou cardíacas aparentes",
                "Sem queixas neurológicas agudas"
            ],
            "habitos": {
                "tabagismo": "Ex-fumante, 20 anos",
                "alcool": "Consumo social aos finais de semana",
                "substancias": "Negado uso de drogas ilícitas recentes"
            },
            "historico_medico": {
                "doencas_infancia": [
                    "meningite",
                    "alergia"
                ],
                "cirurgias": "Nenhuma",
                "internacoes": "Não relevantes",
                "familiares": "Doença crônica (diabetes) em alguns irmãos"
            },
            "atividade_fisica": "Esforço físico relacionado ao trabalho; pratica esportes esporadicamente",
            "vida_sexual": "Ativa, usa preservativo na maioria das relações"
        },
        "A": {
            "avaliacao": "Dor abdominal inferior aguda com febre alta e tremores, sugestiva de processo infeccioso ou inflamatório agudo no abdômen inferior. Considerar apendicite, colecistite, gastroenterite ou outras causas abdominais agudas. História médica e hábitos de vida não indicam comorbidades significativas, embora paciente tenha antecedentes de meningite e alergias."
        },
        "P": {
            "plano": [
                "Exames laboratoriais: hemograma completo, PCR, urina tipo I",
                "Exames de imagem: ultrassonografia abdominal ou tomografia se indicado",
                "Controle da febre com antitérmico conforme prescrição",
                "Hidratação oral adequada",
                "Orientação para procurar atendimento de emergência caso dor piore, haja vômitos persistentes ou outros sintomas alarmantes",
                "Reavaliação após exames para definição de conduta"
            ]
        }
    },
    "paciente": {
        "mensagem": "Olá Sr. Manuel, observamos que você está com dor na barriga inferior, febre e tremores que começaram há dois dias. É importante fazer exames de sangue e imagem para entender a causa. Tome os remédios para febre conforme orientado e mantenha-se hidratado. Se a dor aumentar, surgirem vômitos ou outros sintomas, procure o pronto-socorro imediatamente. Após os exames, iremos revisar os resultados e decidir o melhor tratamento."
    }
}
    }
    # """
    # Envia o texto transcrito para o GPT real e recebe o JSON clínico.
    # """
    # prompt = f"""
    # Você é um assistente médico. Receba a transcrição do paciente abaixo e gere um JSON clínico estruturado:
    
    # Transcrição: {texto_transcrito}

    # O JSON deve conter 'clinico' e 'paciente', seguindo este exemplo:

    # {{
    #   "clinico": {{
    #     "S": {{...}},
    #     "O": {{...}},
    #     "A": {{...}},
    #     "P": {{...}}
    #   }},
    #   "paciente": {{
    #     "mensagem": "..."
    #   }}
    # }}
    # """
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}],
    #     temperature=0
    # )

    # resposta_texto = response.choices[0].message.content
    # # Tenta converter para dict
    # try:
    #     return json.loads(resposta_texto)
    # except:
    #     # Se falhar, retorna texto dentro de 'historia_doenca_atual'
    #     return {
    #         "clinico": {
    #             "S": {
    #                 "identificacao": {},
    #                 "queixa_principal": "",
    #                 "historia_doenca_atual": resposta_texto
    #             }
    #         },
    #         "paciente": {"mensagem": "Erro ao gerar JSON real, veja transcrição."}
    #     }

def salvar_json(json_data: dict, caminho_saida: str):
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
