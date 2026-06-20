from dataclasses import dataclass

@dataclass(frozen=True)
class RunConfig:
    learning_rate: float = 0.001
    epochs: int = 3
    batch_size: int = 1000
    top_k_words: int = 20