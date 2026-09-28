import json
import sys

from interview_prep.graph import workflow
from interview_prep.models import InterviewConversationState

INITIAL_STATE: InterviewConversationState = {
    "role": "backend engineer",
    "experience_level": "mid",
    "interview_type": "technical",
    "input_questions": [
        "What are mutable and immutable objects in Python?",
        "What is the difference between == and is in Python?",
        "What are Python's built-in data types?",
        "What is the difference between a list, tuple, set, and dictionary?",
        "What is the difference between shallow copy and deep copy?",
        "What are *args and **kwargs?",
        "What is variable scope in Python?",
        "What is the difference between local, global, and nonlocal variables?",
        "What are default arguments in Python?",
        "Why are mutable default arguments dangerous?"    
    ],
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
    result = workflow.invoke(dict(INITIAL_STATE))
    
    print(result)
        
    return 0


if __name__ == "__main__":
    sys.exit(main())
