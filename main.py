from fastapi import FastAPI
from app.di_container import DIContainer
from app.resources import ai_resource 
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

container = DIContainer()
container.config.whisper_model_name.from_env("WHISPER_MODEL_NAME", as_=str, default="medium") # required=True)
# Here you need add module where you neeed @inject decorator to inject dependencies
container.wire(modules=[ai_resource,])

app = FastAPI()
app.container = container
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
app.include_router(ai_resource.router)



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