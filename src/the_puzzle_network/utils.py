"""Utility functions for The Puzzle Network."""

import os

from dotenv import load_dotenv

from .logging import get_logger


logger = get_logger(__name__)


def load_env():
    load_dotenv()
    app_name = os.getenv("APP_NAME")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    logger.info("✅ OpenAI API key has been configured, %s can proceed.", app_name)
    return app_name
