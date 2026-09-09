from backend.agent.memory import (
    add_message,
    get_recent_memory,
)

from backend.agent.planner import create_plan
from backend.agent.executor import execute_tool
from backend.models.llm import generate_response
from backend.config import MAX_AGENT_STEPS


def format_memory(memory):
    """
    Convert conversation memory into text for the LLM.
    """

    if not memory:
        return "No previous conversation."

    lines = []

    for message in memory:
        role = message.get(
            "role",
            "unknown"
        )

        content = message.get(
            "content",
            ""
        )

        lines.append(
            f"{role.upper()}: {content}"
        )

    return "\n".join(lines)


def generate_final_response(
    user_message: str,
    tool_result=None,
):
    """
    Generate the final response using conversation
    context and the tool result.
    """

    memory = get_recent_memory()

    memory_text = format_memory(memory)

    tool_text = "No tool was used."

    if tool_result is not None:
        tool_text = str(tool_result)

    prompt = f"""
You are an AI Learning and Study Assistant.

Answer the student's request clearly and accurately.

Use the conversation context when useful.

If a tool was used, use its result as evidence.

Do not claim that you performed an action
that you did not perform.

Conversation context:
{memory_text}

Tool result:
{tool_text}

Current student request:
{user_message}

Provide only the final answer.
"""

    return generate_response(prompt)


def run_agent(user_message: str):
    """
    Run the complete agent workflow.
    """

    if not user_message.strip():
        return "Please enter a message."

    add_message(
        "user",
        user_message
    )

    tool_result = None

    for _ in range(MAX_AGENT_STEPS):

        plan = create_plan(
            user_message
        )

        action = plan.get(
            "action",
            "none"
        )

        tool_input = plan.get(
            "input",
            ""
        )

        if action == "none":
            break

        tool_result = execute_tool(
            action,
            tool_input
        )

        break

    final_response = generate_final_response(
        user_message,
        tool_result
    )

    add_message(
        "assistant",
        final_response
    )

    return final_response