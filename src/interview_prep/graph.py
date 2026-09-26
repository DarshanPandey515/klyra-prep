"""The interview graph: agent definition, node functions, and assembly."""

from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph
from pydantic_ai import Agent

from interview_prep.models import InterviewConversationState

load_dotenv()

MODEL = "groq:openai/gpt-oss-20b"

agent = Agent(model=MODEL)


def working(state: InterviewConversationState) -> dict[str, object]:
    """Placeholder node; returns state updates instead of mutating in place."""
    return {
        "status": "preparing",
        "conversation_history": state["conversation_history"]
        + [{"role": "system", "content": "working"}],
    }


def build_graph():
    """Compile the interview workflow."""
    graph = StateGraph(InterviewConversationState)
    graph.add_node("working", working)
    graph.add_edge(START, "working")
    graph.add_edge("working", END)
    return graph.compile()


workflow = build_graph()
