"""Abstract base class for all puzzle network agents."""

from abc import ABC, abstractmethod
from typing import Any

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

from ..logging import get_logger


logger = get_logger(__name__)


class PuzzleBaseAgent(ABC):
    def __init__(self) -> None:
        self.agent = ChatAgent(
            chat_client=OpenAIChatClient(model_id="gpt-4.1"),
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
        result = await self.agent.run(prompt)
        return str(result)
