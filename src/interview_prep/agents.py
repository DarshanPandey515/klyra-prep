from pydantic_ai import Agent
from dotenv import load_dotenv
from interview_prep.models import (
    AnswerEvaluation,
    FinalEvaluation,
    FollowUpOutput,
    QuestionPreparationOutput,
)
from interview_prep.prompts import (
    ANSWER_EVALUATION_PROMPT,
    FINAL_EVALUATION_PROMPT,
    FOLLOW_UP_PROMPT,
    QUESTION_PREPARATION_PROMPT,
)


load_dotenv()


MODEL = "groq:openai/gpt-oss-20b"


question_preparation_agent = Agent(
    model=MODEL,
    system_prompt=QUESTION_PREPARATION_PROMPT,
    output_type=QuestionPreparationOutput,
)


answer_evaluation_agent = Agent(
    model=MODEL,
    system_prompt=ANSWER_EVALUATION_PROMPT,
    output_type=AnswerEvaluation,
)


follow_up_agent = Agent(
    model=MODEL,
    system_prompt=FOLLOW_UP_PROMPT,
    output_type=FollowUpOutput,
)


final_evaluation_agent = Agent(
    model=MODEL,
    system_prompt=FINAL_EVALUATION_PROMPT,
    output_type=FinalEvaluation,
)