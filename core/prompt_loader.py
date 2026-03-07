from pathlib import Path

class PromptLoader:
    def __init__(self, prompt_dir="templates"):
        self.prompt_dir = Path(prompt_dir)

    def load(self, name: str):
        path = self.prompt_dir / f"{name}.md"
        if not path.exists():
            raise FileNotFoundError(f"Prompt {name} not found")
        return path.read_text(encoding="utf-8")