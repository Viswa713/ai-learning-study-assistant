import json

from backend.models.llm import generate_response


PLANNER_PROMPT = """
You are the planning component of an AI Learning & Study Assistant.

Your job is to understand the student's request and
choose the most appropriate action.

Available actions:

1. course_qa
   Use when the student asks a question that should
   be answered using uploaded course materials.

2. study_plan
   Use when the student wants a study plan,
   learning schedule, revision plan, or exam preparation plan.

3. quiz
   Use when the student wants a quiz, test,
   practice questions, MCQs, or exam questions.

4. calculator
   Use for mathematical calculations.

5. web_search
   Use when current or external information is required.

6. file_reader
   Use when the student explicitly asks to read
   a local project file.

7. none
   Use for normal conversation.

Return ONLY valid JSON.

For course_qa, calculator, web_search, and file_reader:

{
    "action": "action_name",
    "input": "required input",
    "reason": "short explanation"
}

For study_plan:

{
    "action": "study_plan",
    "input": {
        "subjects": "subjects",
        "exam_date": "exam date",
        "daily_hours": "available hours",
        "learning_goal": "learning goal"
    },
    "reason": "short explanation"
}

For quiz:

{
    "action": "quiz",
    "input": {
        "course_material": "relevant material or topic",
        "number_of_questions": 5,
        "difficulty": "easy | medium | hard"
    },
    "reason": "short explanation"
}

Do not use Markdown.
Do not add explanations outside the JSON.

Student request:
"""


def create_plan(user_message: str):
    """
    Ask the LLM to determine which action
    the agent should take.
    """

    prompt = PLANNER_PROMPT + user_message

    response = generate_response(prompt)

    try:
        plan = json.loads(response)

        if not isinstance(plan, dict):
            raise ValueError(
                "Planner response is not an object."
            )

        allowed_actions = {
            "course_qa",
            "study_plan",
            "quiz",
            "calculator",
            "web_search",
            "file_reader",
            "none"
        }

        action = plan.get(
            "action",
            "none"
        )

        if action not in allowed_actions:
            action = "none"

        return {
            "action": action,
            "input": plan.get(
                "input",
                ""
            ),
            "reason": plan.get(
                "reason",
                ""
            )
        }

    except (
        json.JSONDecodeError,
        ValueError
    ):
        return {
            "action": "none",
            "input": "",
            "reason": (
                "The planner returned "
                "an invalid plan."
            )
        }