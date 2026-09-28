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
    """Build the Groq model with native JSON-schema output forced on.

    PydanticAI's built-in profile has `supports_json_schema_output = False` for
    this model, so `output_type` falls back to tool calls. gpt-oss in harmony
    mode then wraps the payload in a {"name":..., "arguments":...} envelope,
    renames fields (original_question -> original), and returns lists as plain
    strings, which Groq rejects with `tool_use_failed`. Groq's own JSON Schema
    Mode handles the same schema correctly, so use it.

    ponytail: drop this if pydantic-ai enables native output for groq gpt-oss.
    """
    base = GroqModel(GROQ_MODEL_ID)
    return GroqModel(
        GROQ_MODEL_ID,
        profile={
            **base.profile,
            "supports_json_schema_output": True,
            "default_structured_output_mode": "native",
        },
    )


# Shared by every agent: the harmony tool-call bug is a property of the model,
# not of any one prompt, so every output_type= agent needs the same override.
MODEL = groq_model()

question_preparation_agent = Agent(
    model=MODEL,
    system_prompt=QUESTION_PREPARATION_PROMPT,
    output_type=QuestionPreparationOutput,
    # Only this agent writes a whole question bank in one shot, so it is the only
    # one that can outrun the budget. Groq defaults to ~8k when max_tokens is
    # omitted, which cut the JSON off mid-list.
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
