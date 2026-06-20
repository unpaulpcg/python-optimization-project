import json
from config import RunConfig

class NLPModel:
    """단일책임원칙 ( SRP ) 적용 : 상태 관리만 담당"""
    def __init__(self, config: RunConfig):
        self.config = config
        self._weights = {}

    @property
    def weights(self) -> dict:
        """캡슐화를 통한 내부 상태 보호"""
        return self._weights

    def set_initial_weight(self, word: str, weight: float):
        self._weights[word] = weight

    def update_weight(self, word: str, delta: float):
        if word in self._weights:
            self._weights[word] += delta

    def save_weights(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._weights, f)
            
    def load_weights(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            self._weights = json.load(f)