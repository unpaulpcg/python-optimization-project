from model import NLPModel
from data_handler import DataHandler
from decorators import timer_decorator

class Inferencer:
    """추론 기능만 담당 ( SRP 및 DRY 원칙 준수 )"""
    def __init__(self, model: NLPModel, data_handler: DataHandler):
        self.model = model
        self.data_handler = data_handler

    @timer_decorator
    def infer(self, sentence: str) -> float:
        score = 0.0
        words = self.data_handler.preprocess_line(sentence)
        
        for word in words:
            if word in self.model.weights:
                score += self.model.weights[word]
        return score