"""Utility functions for The Puzzle Network."""

import logging
import os

from dotenv import load_dotenv


logger = logging.getLogger(__name__)


def load_env() -> str:
    """Load environment variables for OpenAI configuration."""
    load_dotenv()
    app_name = os.getenv("APP_NAME", "The Puzzle Network (Agent Framework)")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    logger.info("✅ OpenAI API key has been configured, %s can proceed.", app_name)
    return app_name


# Note: extract_textpart function is no longer needed as agent-framework
# handles response extraction differently through WorkflowOutputEvent
