from fastapi import APIRouter, Depends, File, Form, UploadFile
from dependency_injector.wiring import inject, Provide

from app.di_container import DIContainer
from app.services.ai_service import AiService
from app.services.upload_service import UploadService

router = APIRouter()

@router.post("/ai")
@inject
async def whisper_transcribe(
        file: UploadFile = File(...), 
        media_language:str = Form(...), 
        ai_service:AiService = Depends(Provide[DIContainer.ai_service]),
        upload_service:UploadService = Depends(Provide[DIContainer.upload_service])
    ):
    
    upload_service.process_file(file)
    
    # text_result = ai_service.transcribe(r"D:\Dev\workspace\fastfade-ai\audio.mp3", "fr")
    # return text_result

    return ""