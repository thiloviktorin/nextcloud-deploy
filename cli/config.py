"""Config file for CLI"""

from pathlib import Path

from dynaconf import Dynaconf

BASE_PATH = Path(__file__).parent.parent.resolve()
CONFIG_PATH = BASE_PATH / "cli" / "config"

settings = Dynaconf(
    envvar_prefix="NEXTCLOUD",
    settings_files=[CONFIG_PATH / "settings.toml", CONFIG_PATH / ".secrets.toml"],
    env_switcher="APP_ENV",
    environments=True,
    merge_enabled=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
