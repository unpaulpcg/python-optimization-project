import time
from config import RunConfig
from data_handler import DataHandler
from model import NLPModel
from decorators import timer_decorator

class Trainer:
    """학습 루프만 담당 ( 의존성 주입 )"""
    def __init__(self, model: NLPModel, data_handler: DataHandler, config: RunConfig):
        self.model = model
        self.data_handler = data_handler
        self.config = config

    @timer_decorator
    def run_training(self):
        vocab = self.data_handler.build_vocab()
        for word in vocab:
            self.model.set_initial_weight(word, 0.5)
            
        epochs = self.config.epochs
        lr = self.config.learning_rate
        
        for epoch in range(epochs):
            epoch_start = time.time()
            total_loss = 0.0
            
            for batch in self.data_handler.batch_generator():
                loss_step = sum(len(line) for line in batch) * lr
                total_loss += loss_step
                
                for word in self.model.weights:
                    self.model.update_weight(word, 0.001)
                    
            epoch_end = time.time()
            print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss:.4f} - 소요시간: {epoch_end - epoch_start:.2f}초")