from fastapi import FastAPI
from app.resources import myresource  # Import your routes here
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

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


# if __name__ == "__main__":
#    pass

