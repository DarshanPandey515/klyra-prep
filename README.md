# interview-prep

AI mock-interview agent. It generates interview questions from a role and
experience level, evaluates each answer against a rubric, and produces an
overall score with feedback.

Built on [LangGraph](https://langchain-ai.github.io/langgraph/) for the
conversation flow and [Pydantic AI](https://ai.pydantic.dev/) for the model
calls, with Groq (`openai/gpt-oss-20b`) as the default inference provider.

## Status

Early scaffold. The graph compiles and runs end to end, but `working` is a
placeholder node — question generation, evaluation, and follow-up nodes are
not implemented yet.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- A Groq API key (free tier is enough)

## Setup

```bash
git clone https://github.com/DarshanPandey515/klyra-prep.git
cd klyra-prep
uv sync
cp .env.example .env      # then paste your GROQ_API_KEY into .env
```

## Usage

```bash
uv run interview-prep              # console script
uv run python -m interview_prep    # equivalent
```

This prints the Mermaid diagram of the compiled graph and runs it once
against a blank state, so you can confirm wiring and your API key are good.

## Layout

```
interview-prep/
├── src/interview_prep/
│   ├── __init__.py      public API re-exports
│   ├── __main__.py      CLI entrypoint + initial state
│   ├── graph.py         agent, node functions, graph assembly
│   └── models.py        Pydantic schemas + graph state
├── notebooks/           scratch notebooks
└── pyproject.toml
```

`models.py` holds the data contract, `graph.py` holds the flow. Everything the
graph needs is a plain function over `InterviewConversationState`, so nodes can
be added and tested one at a time.

## Development

```bash
uv sync                        # install with dev dependencies
uv run ruff check .             # lint
uv run ruff format .            # format
uv add <package>                # add a runtime dependency
uv add --dev <package>          # add a dev dependency
```

## Roadmap

- Question-generation node (`preparing`)
- Answer-evaluation node with rubric scoring (`evaluating`)
- Conditional follow-up edges
- Interactive CLI loop with streamed output

## License

MIT — see [LICENSE](LICENSE).
