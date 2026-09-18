from dynaconf import Dynaconf
from pathlib import Path 

BASE_PATH = Path(__file__).parent
CONFIG_PATH= BASE_PATH / "config"
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[CONFIG_PATH/'settings.toml', CONFIG_PATH/'.secrets.toml'],
    env_switcher="APP_ENV"
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
