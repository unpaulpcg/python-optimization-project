import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import RunConfig
from model import NLPModel
from data_handler import DataHandler
from trainer import Trainer
from decorators import timer_decorator

@timer_decorator
def main():
    print("==================================================")
    print("         🚀 Starting Optimized Training Pipeline   ")
    print("==================================================")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data_utils", "dataset.txt")
    weights_path = os.path.join(base_dir, "data_utils", "model_weights.json")
    
    config = RunConfig()
    model = NLPModel(config)
    data_handler = DataHandler(data_path, config)
    trainer = Trainer(model, data_handler, config)
    
    trainer.run_training()
    model.save_weights(weights_path)

if __name__ == "__main__":
    main()