"""Command-line entrypoint: `interview-prep` or `python -m interview_prep`."""

import json
import sys

from interview_prep.graph import workflow
from interview_prep.models import InterviewConversationState

INITIAL_STATE: InterviewConversationState = {
    "role": "backend engineer",
    "experience_level": "mid",
    "interview_type": "technical",
    "input_questions": [],
    "prepared_questions": [],
    "current_question_index": 0,
    "current_question": None,
    "current_answer": "",
    "evaluations": [],
    "conversation_history": [],
    "status": "preparing",
    "overall_score": None,
    "final_feedback": None,
}


def main() -> int:
    """Print the graph diagram and run it once against a blank state."""
    print(workflow.get_graph().draw_mermaid())
    result = workflow.invoke(dict(INITIAL_STATE))
    print(json.dumps(result["conversation_history"], indent=2))
    assert result["status"] == "preparing", "working node did not run"
    return 0


if __name__ == "__main__":
    sys.exit(main())
