def read_text(file: str) -> str:
    with open(file) as f:
        return f.read()
