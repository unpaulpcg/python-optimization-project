import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import RunConfig
from model import NLPModel
from data_handler import DataHandler
from inferencer import Inferencer
from decorators import timer_decorator

@timer_decorator
def main():
    print("==================================================")
    print("         🧠 Starting Optimized Inference Pipeline  ")
    print("==================================================")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    weights_path = os.path.join(base_dir, "data_utils", "model_weights.json")
    
    if not os.path.exists(weights_path):
        print("모델 가중치 파일이 없습니다! 먼저 train.py를 실행하세요.")
        return
        
    config = RunConfig()
    model = NLPModel(config)
    model.load_weights(weights_path)
    
    data_handler = DataHandler("", config)
    inferencer = Inferencer(model, data_handler)
    
    test_sentences = [
        "deep learning is a subset of machine learning",
        "gradient descent optimizes the loss function",
        "random sentence with no keywords"
    ]
    
    print("\n[추론 결과]")
    for sentence in test_sentences:
        score = inferencer.infer(sentence)
        print(f"문장: '{sentence[:20]}...' -> 예측 점수: {score:.4f}\n")

if __name__ == "__main__":
    main()