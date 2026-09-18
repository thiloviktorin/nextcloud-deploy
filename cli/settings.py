from pydantic import BaseModel
from cli.config import settings


class NextcloudSettings(BaseModel):
    """Pydantic class to validate all settings belonging to the Nextcloud.

    Args:
        BaseModel (_type_): Pydantic Basemodel
    """

    domain: str


class Settings(BaseModel):
    """Pydantic Settings class to validate all settings.

    Args:
        BaseModel (_type_): Pydantic Basemodel.
    """

    nextcloud: NextcloudSettings


def get_settings() -> Settings:
    """Wrapper function to return the settings.

    Returns:
        Settings: Settings object holding the settings as specified
          in the settings.toml and .secrets.toml
    """
    return Settings.model_validate(
        {key.lower(): value for key, value in settings.as_dict().items()}
    )
