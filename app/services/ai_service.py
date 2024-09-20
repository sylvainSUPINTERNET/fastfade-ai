from app.services.openai_model_loader import OpenAiModelLoader

class AiService():

    def __init__(self, openai_model_loader: OpenAiModelLoader):
        self.openai_model_loader = openai_model_loader

    def transcribe(self, audio_path: str, language: str) -> str:
        
        whisper_result = self.openai_model_loader.whisper.transcribe(audio_path, language=language)

        return {
            "text_result": whisper_result["text"]
        }