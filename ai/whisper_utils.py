# ai/whisper_utils.py
import whisper

model = whisper.load_model("base")  # ou "small", "medium", "large" dependendo do seu setup

def transcrever_audio_real(caminho_audio: str) -> str:
    """
    Transcreve o áudio usando o Whisper real.
    """
    result = model.transcribe(caminho_audio)
    return result["text"]
