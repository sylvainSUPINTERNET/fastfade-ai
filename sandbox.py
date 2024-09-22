# import whisper

# model = whisper.load_model("base")

# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("audio.mp3")
# audio = whisper.pad_or_trim(audio)

# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)

# # print the recognized text
# print(result.text)


import whisper
from transformers import pipeline
import nltk
nltk.download('stopwords')

from nltk.tokenize import TextTilingTokenizer


emotions_pipeline = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)


model = whisper.load_model("medium")
result = model.transcribe("audio2.mp3")

for segment in result["segments"]:
    print(segment["start"])
    print(segment["end"])
    print(segment["text"])
    print(emotions_pipeline (["text"]))
    print(" ")
# print(result["text"])


# Instancier un tokenizer TextTiling
tt = TextTilingTokenizer()

# Découper en segments thématiques
segments = tt.tokenize(result["text"])

# Afficher les segments thématiques
for segment in segments:
    print(segment)