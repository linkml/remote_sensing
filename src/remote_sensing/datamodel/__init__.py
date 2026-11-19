"""Data model package for remote-sensing."""

from pathlib import Path
from .remote_sensing import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "remote_sensing.yaml"
