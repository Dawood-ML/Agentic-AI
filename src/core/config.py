# src/core/config.py
# This module handles loading configuration and secrets from the .env file.
# It provides a centralized, secure way to access sensitive information.

import os
from dotenv import load_dotenv
from pathlib import Path

# Determine the project root directory
# This allows the .env file to be found regardless of where the script is run from.
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    """
    A class to hold all application settings, loaded from environment variables.
    This prevents scattering os.getenv() calls throughout the codebase.
    """
    PROJECT_NAME: str = "Agentic AI System"
    PROJECT_VERSION: str = "1.0.0"

    # API Keys - Raise an error if a key is missing. This is a hard failure condition.
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY")
    # Example of an optional key with a default
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", None)


# Instantiate the settings class so it can be imported and used elsewhere.
settings = Settings()

# To use in another file: from src.core.config import settings
# Then access keys like: settings.OPENAI_API_KEY