<!-- @format -->

# 🏥 Saúde HUD - MVP de Transcrição Clínica

![Status](https://img.shields.io/badge/status-beta-yellow)
![Node.js](https://img.shields.io/badge/Backend-Node.js-brightgreen)
![TailwindCSS](https://img.shields.io/badge/Frontend-TailwindCSS-blue)

**Saúde HUD** é um MVP que permite transcrever áudios de consultas médicas usando Whisper e GPT, gerando registros clínicos estruturados. O sistema oferece interface web para médicos e pacientes revisarem e visualizarem transcrições em tempo real.

---

## ✨ Funcionalidades

- 🎙️ Upload de áudio de consultas médicas
- ⏱️ Processamento assíncrono em background
- 🤖 Integração com Whisper (transcrição) e GPT (geração de JSON clínico)
- 🔔 Notificação quando a transcrição é concluída
- ✅ Revisão médica e validação
- 🧾 Visualização de resumo clínico para pacientes

---

## 🖼️ Interface

### Upload e transcrição

![Upload de áudio](https://user-images.githubusercontent.com/SEU-USER/screenshots/upload.png)  
**Exemplo de upload de áudio e status de transcrição.**

### Lista de transcrições

![Lista de transcrições](https://user-images.githubusercontent.com/SEU-USER/screenshots/list.png)  
**Após a transcrição, clique em “Revisar” para abrir o arquivo.**

---

## 📂 Estrutura do Projeto

ai/
├─ audio/ # Áudios enviados
├─ transcripts/ # Transcrições geradas (TXT ou JSON)
├─ gpt_util.py # Funções GPT
├─ main.py # Script principal (opcional)
└─ whisper_utils.py # Funções Whisper

backend/
└─ server.js # Servidor Node.js

frontend/
├─ index.html # Interface web
└─ app.js # Lógica frontend

yaml
Copiar
Editar

---

## 🚀 Instalação e Execução

### 1️⃣ Clonar o repositório

```bash
git clone <URL_DO_REPO>
cd saude_ai
2️⃣ Instalar dependências do backend
bash
Copiar
Editar
cd backend
npm install express multer cors
3️⃣ Rodar o servidor backend
bash
Copiar
Editar
node server.js
O servidor ficará disponível em http://localhost:3000.

4️⃣ Abrir frontend
Acesse no navegador:

bash
Copiar
Editar
http://localhost:3000/index.html
Faça upload do áudio, aguarde a transcrição e clique em Revisar.

⚡ Próximos Passos
Substituir a simulação por Whisper real

Integrar GPT para gerar JSON clínico completo

Adicionar autenticação de médicos e pacientes

Histórico de transcrições com filtros

Notificações em tempo real via WebSocket

Exportação de relatórios em PDF

📌 Observações
Abra o frontend via HTTP (localhost:3000), não file://.

Certifique-se de que ai/transcripts existe e tem permissão de gravação.

Arquivos de transcrição atualmente são .txt (JSON será implementado em breve).

```
