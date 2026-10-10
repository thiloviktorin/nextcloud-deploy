"""Test CLI commands"""

from collections.abc import Callable

import pytest
from typer.testing import CliRunner

from cli.main import app
from cli.settings import Settings

runner = CliRunner()


def test_validate_success(
    monkeypatch: pytest.MonkeyPatch, valid_settings: Settings
) -> None:
    """Test validate method's successful path.

    Args:
        monkeypatch (pytest.MonkeyPatch): monkeypatch.
        valid_settings (Settings): valid Settings object.
    """
    monkeypatch.setattr("cli.main.get_settings", lambda: valid_settings)
    result = runner.invoke(app, ["validate"])
    assert result.exit_code == 0
    assert "valid" in result.stdout


def test_validate_unsuccessful(
    monkeypatch: pytest.MonkeyPatch, invalid_settings: Callable[[], Settings]
) -> None:
    """Test validate method's unsuccessful path.

    Args:
        monkeypatch (pytest.MonkeyPatch): monkeypatch
        invalid_settings (Callable[[], Settings]): Callable that returns an invalid
        Settings object.
    """
    monkeypatch.setattr(
        "cli.main.get_settings",
        invalid_settings,
    )
    result = runner.invoke(app, ["validate"])
    assert result.exit_code == 1
    assert "nextcloud" in result.stderr
