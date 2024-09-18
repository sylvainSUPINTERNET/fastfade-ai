from fastapi import FastAPI
from app.resources import myresource  # Import your routes here
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import whisper
from transformers import pipeline

load_dotenv()

app = FastAPI()
origins = [
    "*",  # Allows requests from any origin (use with caution in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register your routes
app.include_router(myresource.router)  


model = whisper.load_model("medium")
# Initialize the whisper library with the French language , default is optimized for English
result = model.transcribe(r"D:\Dev\workspace\fastfade-ai\audio.mp3", language="fr")

print(result["text"])


analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer="cmarkea/distilcamembert-base-sentiment"
)
result = analyzer(
    "J'aime me promener en forêt même si ça me donne mal aux pieds.",
    return_all_scores=True
)

print(result)

# classifier = pipeline(
#     "text-classification",
#     # model="j-hartmann/emotion-english-multilingual-roberta-base",
#     model="arpanghoshal/EmoRoBERTa",
#     return_all_scores=True,
#     function_to_apply='sigmoid'
# )
# text = "I'm feeling so happy and excited today!"
# results = classifier(text)
# for result in results[0]:
#     print(f"Émotion: {result['label']}, Score: {result['score']:.4f}")