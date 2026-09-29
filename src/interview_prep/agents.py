from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel

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


GROQ_MODEL_ID = "openai/gpt-oss-20b"


def groq_model() -> GroqModel:
    base = GroqModel(GROQ_MODEL_ID)
    return GroqModel(
        GROQ_MODEL_ID,
        profile={
            **base.profile,
            "supports_json_schema_output": True,
            "default_structured_output_mode": "native",
        },
    )


MODEL = groq_model()

question_preparation_agent = Agent(
    model=MODEL,
    system_prompt=QUESTION_PREPARATION_PROMPT,
    output_type=QuestionPreparationOutput,
    model_settings={
        "max_tokens": 32_000,
        "groq_reasoning_effort": "low",
    },
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
