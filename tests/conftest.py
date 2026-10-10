"""Testing configuration"""

from collections.abc import Callable

import pytest

from cli.settings import Settings


def break_validation() -> Settings:
    """Return invalid Settings object."""
    return Settings.model_validate({})


@pytest.fixture
def valid_settings() -> Settings:
    """Return validated Settings object."""
    return Settings.model_validate(
        {"nextcloud": {"domain": "cloud.example.com", "admin_mail": ""}}
    )


@pytest.fixture
def invalid_settings() -> Callable[[], Settings]:
    """Return invalid Settings through the 'break_validation' callable."""
    return break_validation
