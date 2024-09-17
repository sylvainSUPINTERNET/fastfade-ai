from fastapi import FastAPI
from app.resources import myresource  # Import your routes here
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import whisper

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



model = whisper.load_model("base")
result = model.transcribe(r"D:\Dev\workspace\fastfade-ai\audio.mp3")

print(result["text"])
