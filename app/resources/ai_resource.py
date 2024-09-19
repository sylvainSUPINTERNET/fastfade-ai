from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from app.di_container import DIContainer
from app.services.ai_service import AiService

router = APIRouter()

@router.get("/ai")
@inject
async def whisper_transcribe(ai_service:AiService = Depends(Provide[DIContainer.ai_service])):
    # res = ai_service.transcribe(r"D:\Dev\workspace\fastfade-ai\audio.mp3", "fr")
    res = await ai_service.transcribe(r"D:\Dev\workspace\fastfade-ai\audio.mp3", "fr")
    return res["text"]