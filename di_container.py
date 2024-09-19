from dependency_injector import containers, providers

from app.services.ai_service import AiService

class DIContainer(containers.DeclarativeContainer):
    # Le modèle Whisper est un singleton
    model = providers.Singleton(whisper.load_model, "medium")
    ai_service = providers.Factory(AiService, model=model)

    # Le controller dépend du service
    audio_controller = providers.Factory(AudioController, model_service=model_service)
