"""Sequential workflow for the Puzzle Network using Microsoft Agent Framework."""

import logging
from typing import cast

from agent_framework import ChatMessage, SequentialBuilder, WorkflowOutputEvent

from the_puzzle_network.agents.puzzle_classifier_agent import PuzzleClassifierAgent
from the_puzzle_network.agents.puzzle_formatter_agent import PuzzleFormatterAgent
from the_puzzle_network.agents.puzzle_generator_agent import PuzzleGeneratorAgent
from the_puzzle_network.agents.puzzle_publisher_agent import PuzzlePublisherAgent


logger = logging.getLogger(__name__)


class PuzzleNetworkWorkflow:
    def __init__(self) -> None:
        # Create individual agents
        self.generator = PuzzleGeneratorAgent()
        self.classifier = PuzzleClassifierAgent()
        self.formatter = PuzzleFormatterAgent()
        self.publisher = PuzzlePublisherAgent()

        # Build sequential workflow
        self.workflow = (
            SequentialBuilder()
            .participants(
                [
                    self.generator.agent,
                    self.classifier.agent,
                    self.formatter.agent,
                    self.publisher.agent,
                ]
            )
            .build()
        )

    def _get_name(self) -> str:
        return __name__.split(".")[-1]

    async def run_workflow(self) -> None:
        prompt = (
            "Generate a puzzle, then classify it, format it as HTML and publish it."
        )

        logger.info("🚀 Starting Puzzle Network Workflow")

        try:
            # Collect all outputs
            outputs = []
            step = 0

            async for event in self.workflow.run_stream(prompt):
                if isinstance(event, WorkflowOutputEvent):
                    step += 1
                    output = cast(list[ChatMessage], event.data)
                    outputs.append(output)

                    # Log the latest message from the conversation
                    if output:
                        latest_msg = output[-1]
                        author = getattr(latest_msg, "author_name", "Agent")
                        text = getattr(latest_msg, "text", str(latest_msg))
                        logger.info(f"✅ Step {step} [{author}]: {text[:100]}...")

            logger.info("🎉 Workflow completed successfully")

        except Exception as e:
            logger.error(f"❌ Workflow failed: {e}")
            raise
