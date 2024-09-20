from app.services.firebase_conf import FirebaseConf
from app.services.openai_model_loader import OpenAiModelLoader
from dependency_injector import containers, providers

from app.services.ai_service import AiService
from app.services.upload_service import UploadService

class DIContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    """
    Here you can add your dependencies
    """
    openai_model_loader = providers.Singleton(
        OpenAiModelLoader,
        whisper_model_name=config.whisper_model_name
    )

    firebase_conf = providers.Singleton(
        FirebaseConf,
        firebase_storage_bucket=config.firebase_storage_bucket
    )


    ai_service = providers.Factory(
        AiService,
        openai_model_loader=openai_model_loader,
    )

    upload_service = providers.Factory(
        UploadService,
        firebase_conf=firebase_conf
    )