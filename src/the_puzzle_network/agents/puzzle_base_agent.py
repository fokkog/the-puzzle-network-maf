"""Abstract base class for all puzzle network agents."""

import logging
from abc import ABC, abstractmethod
from typing import Any

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient


logger = logging.getLogger(__name__)


class PuzzleBaseAgent(ABC):
    def __init__(self) -> None:
        self.agent = ChatAgent(
            chat_client=OpenAIChatClient(),
            name=self._get_name(),
            instructions=self._get_instruction(),
            tools=self._get_tools(),
        )

    @abstractmethod
    def _get_name(self) -> str:
        """Get the name for this agent."""
        pass

    @abstractmethod
    def _get_tools(self) -> list[Any]:
        """Get the list of tools for this agent."""
        pass

    @abstractmethod
    def _get_instruction(self) -> str:
        """Get the instruction prompt for this agent."""
        pass

    async def run_agent(self, prompt: str) -> str:
        """Run the agent with a prompt and return the response."""
        try:
            result = await self.agent.run(prompt)
            return str(result)
        except Exception as e:
            logger.error(f"Error running agent {self._get_name()}: {e}")
            raise
