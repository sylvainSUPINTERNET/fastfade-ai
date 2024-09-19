import whisper

class OpenAiModelLoader():
    def __init__(self, whisper_model_name: str):
        self.whisper_model_name = whisper_model_name
        self.whisper = whisper.load_model(whisper_model_name)
