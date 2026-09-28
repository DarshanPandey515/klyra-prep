from langgraph.graph import END, START, StateGraph

from interview_prep.agents import question_preparation_agent
from interview_prep.models import InterviewConversationState
from interview_prep.utils import build_prompt


def prepare_interview_questions(state: InterviewConversationState) -> dict:
    prompt = build_prompt(
        input_questions=state["input_questions"],
        role=state["role"],
        experience_level=state["experience_level"],
        interview_type=state["interview_type"],
    )

    response = question_preparation_agent.run_sync(prompt)

    print("=" * 20)
    print(response)
    print("=" * 20)

    result = response.output

    return {
        "prepared_questions": result.questions,
        "current_question_index": 0,
        "status": "asking",
    }


def build_graph():
    graph = StateGraph(InterviewConversationState)

    graph.add_node("prepare_interview_questions", prepare_interview_questions)

    graph.add_edge(START, "prepare_interview_questions")
    graph.add_edge("prepare_interview_questions", END)

    return graph.compile()


workflow = build_graph()
