from app.services.openai_model_loader import OpenAiModelLoader
import whisper

class AiService():

    def __init__(self, openai_model_loader: OpenAiModelLoader):
        self.openai_model_loader = openai_model_loader

    def transcribe(self, audio_path: str, language: str) -> str:
        # model = self.openai_model_loader.whisper

        # model.load_audio()

        # mel = whisper.log_mel_spectrogram(audio).to(model.device)
        # _, probs = model.detect_language(mel)

        whisper_result = self.openai_model_loader.whisper.transcribe(audio_path, language=language)


        return {
            "text_result": whisper_result["text"]
        }
    
    def process_media(self, audio_path):
        model =  self.openai_model_loader.whisper
