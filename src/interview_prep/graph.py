from langgraph.graph import END, START, StateGraph

from interview_prep.agents import question_preparation_agent, answer_evaluation_agent, follow_up_agent
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
    result = response.output

    return {
        "prepared_questions": result.questions,
        "current_question_index": 0,
        "status": "asking",
    }
 

def answer_evaluate(state: InterviewConversationState) -> dict:
    prompt = build_prompt(
        prepared_questions=state["prepared_questions"],
        role=state["role"],
        experience=state["experience_level"],
        interview_type=state["interview_type"],
    )
    
    response = answer_evaluation_agent.run_sync(prompt)
    result = response.output
    
    return {
        "score": result.score,
        "strengths": result.strengths,
        "weaknesses": result.weaknesses,
        "feedback": result.feedback,
        "should_follow_up": result.should_follow_up,
        "follow_up_reason": result.follow_up_reason,
    }

def follow_up_agent(state: InterviewConversationState) -> dict:
    prompt = build_prompt(
        prepared_questions=state["prepared_questions"],
        expected_answer=state["expec"]
    )
    
    

def build_graph():
    graph = StateGraph(InterviewConversationState)

    graph.add_node("prepare_interview_questions", prepare_interview_questions)
    graph.add_node("answer_evaluate", answer_evaluate)

    graph.add_edge(START, "prepare_interview_questions")
    graph.add_edge("prepare_interview_questions", "answer_evaluate")
    graph.add_edge("answer_evaluate", END)

    return graph.compile()


workflow = build_graph()
