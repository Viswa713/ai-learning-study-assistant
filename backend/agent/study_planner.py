from backend.models.llm import generate_response


def create_study_plan(
    subjects: str,
    exam_date: str,
    daily_hours: str,
    learning_goal: str
):
    """
    Generate a personalized study plan
    for the student.
    """

    prompt = f"""
You are an AI Learning and Study Assistant.

Create a practical and personalized study plan
for a student.

Student information:

Subjects:
{subjects}

Exam date:
{exam_date}

Available study time per day:
{daily_hours}

Learning goal:
{learning_goal}

Create a clear plan that includes:

1. Topics to study
2. Daily study schedule
3. Revision sessions
4. Practice sessions
5. Important topics to prioritize

Keep the plan realistic for the available time.

Use simple language and organize the
answer clearly.
"""

    return generate_response(prompt)