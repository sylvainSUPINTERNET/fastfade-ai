from fastapi import FastAPI
from app.resources import myresource  # Import your routes here
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from dependency_injector import containers, providers

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



# from transformers import pipeline

# import whisper

# model = whisper.load_model("medium")
# # Initialize the whisper library with the French language , default is optimized for English
# whisper_result = model.transcribe(r"D:\Dev\workspace\fastfade-ai\audio.mp3", language="fr")

# print(type(whisper_result["text"]))

# # eng_trans = translator.translate(whisper_result["text"], dest='en')


# # classifier = pipeline(
# #     "text-classification",
# #     model="j-hartmann/emotion-english-distilroberta-base",
# #     # model="arpanghoshal/EmoRoBERTa",
# #     return_all_scores=True,
# #     function_to_apply='sigmoid'
# # )

# # results = classifier(eng_trans)

# # print(results)