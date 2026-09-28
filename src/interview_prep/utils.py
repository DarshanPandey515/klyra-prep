from typing import Any

def build_prompt(instruction: str | None = None ,**kwargs: Any) -> str:
    parts = []
    
    if instruction:
        parts.append(instruction.strip())
    if kwargs:
        parts.append(
            "\n".join(
                f"{k.replace("_", " ").title()}: {v}"
                for k, v in kwargs.items()
                if v is not None
            )
        )
        
    return "\n\n".join(parts)