from app.services.openai_model_loader import OpenAiModelLoader
from dependency_injector import containers, providers

from app.services.ai_service import AiService

class DIContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    """
    Here you can add your dependencies
    """
    openai_model_loader = providers.Singleton(
        OpenAiModelLoader,
        whisper_model_name=config.whisper_model_name
    )

    ai_service = providers.Factory(
        AiService,
        openai_model_loader=openai_model_loader,
    )