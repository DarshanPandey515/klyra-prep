from typing import Literal, TypedDict

from pydantic import BaseModel, Field

InterviewStatus = Literal[
    "preparing",
    "asking",
    "listening",
    "evaluating",
    "follow_up",
    "completed",
]


class PreparedQuestion(BaseModel):
    """A single question prepared for the candidate."""

    original_question: str
    interview_question: str
    expected_answer: str
    evaluation_criteria: list[str] = Field(default_factory=list)
    follow_up_questions: list[str] = Field(default_factory=list)


class QuestionPreparationOutput(BaseModel):
    questions: list[PreparedQuestion]


class AnswerEvaluation(BaseModel):
    """Scored result for one candidate answer."""

    score: int = Field(ge=0, le=10)
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    feedback: str

    should_follow_up: bool
    follow_up_reason: str | None = None


class FollowUpOutput(BaseModel):
    question: str
    reason: str


class FinalEvaluation(BaseModel):
    overall_score: float = Field(ge=0, le=10)
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    feedback: str


class InterviewConversationState(TypedDict):
    """State threaded through the interview graph."""

    role: str
    experience_level: str
    interview_type: str
    input_questions: list[str]
    prepared_questions: list[PreparedQuestion]
    current_question_index: int
    current_question: PreparedQuestion | None
    current_answer: str
    evaluations: list[AnswerEvaluation]
    conversation_history: list[dict[str, str]]
    status: InterviewStatus
    overall_score: float | None
    final_feedback: str | None
