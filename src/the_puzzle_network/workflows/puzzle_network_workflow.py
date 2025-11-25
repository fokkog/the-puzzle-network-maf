"""Sequential workflow for the Puzzle Network using Microsoft Agent Framework."""

from agent_framework import SequentialBuilder

from the_puzzle_network.agents.puzzle_classifier_agent import PuzzleClassifierAgent
from the_puzzle_network.agents.puzzle_formatter_agent import PuzzleFormatterAgent
from the_puzzle_network.agents.puzzle_generator_agent import PuzzleGeneratorAgent
from the_puzzle_network.agents.puzzle_publisher_agent import PuzzlePublisherAgent


class PuzzleNetworkWorkflow:
    def __init__(self) -> None:
        self.workflow = (
            SequentialBuilder()
            .participants(
                [
                    PuzzleGeneratorAgent().agent,
                    PuzzleClassifierAgent().agent,
                    PuzzleFormatterAgent().agent,
                    PuzzlePublisherAgent().agent,
                ]
            )
            .build()
        )

    async def run_workflow(self) -> None:
        prompt = (
            "Generate a puzzle, then classify it, format it as HTML and publish it."
        )

        await self.workflow.run(prompt)
