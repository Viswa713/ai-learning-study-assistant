from backend.tools.calculator import calculate
from backend.tools.web_search import web_search
from backend.tools.file_tool import read_file

from backend.rag.qa import answer_from_course_material
from backend.agent.study_planner import create_study_plan
from backend.agent.quiz_generator import generate_quiz


def execute_tool(action: str, tool_input):
    """
    Execute the action selected by the planner.
    """

    if action == "calculator":
        return calculate(tool_input)

    if action == "web_search":
        return web_search(tool_input)

    if action == "file_reader":
        return read_file(tool_input)

    if action == "course_qa":
        return {
            "success": True,
            "result": answer_from_course_material(
                tool_input
            )
        }

    if action in {"study_plan", "quiz"}:
        if not isinstance(tool_input, dict):
            return {
                "success": False,
                "error": "Invalid structured input from planner."
            }

    if action == "study_plan":
        return {
            "success": True,
            "result": create_study_plan(
                subjects=tool_input.get(
                    "subjects",
                    ""
                ),
                exam_date=tool_input.get(
                    "exam_date",
                    ""
                ),
                daily_hours=tool_input.get(
                    "daily_hours",
                    ""
                ),
                learning_goal=tool_input.get(
                    "learning_goal",
                    ""
                )
            )
        }

    if action == "quiz":
        return {
            "success": True,
            "result": generate_quiz(
                course_material=tool_input.get(
                    "course_material",
                    ""
                ),
                number_of_questions=tool_input.get(
                    "number_of_questions",
                    5
                ),
                difficulty=tool_input.get(
                    "difficulty",
                    "medium"
                )
            )
        }

    if action == "none":
        return {
            "success": True,
            "result": None
        }

    return {
        "success": False,
        "error": f"Unknown action: {action}"
    }