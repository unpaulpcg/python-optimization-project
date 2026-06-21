import os
from collections import Counter
from typing import Dict, Iterator, List
from config import RunConfig
from decorators import timer_decorator

class DataHandler:
    """데이터 입출력 및 전처리 담당 ( Lazy Evaluation 및 시간복잡도 최적화 )"""
    def __init__(self, data_path: str, config: RunConfig):
        self.data_path = data_path
        self.config = config

    def preprocess_line(self, line: str) -> List[str]:
        """DRY 원칙 : 공통 전처리 파이프라인"""
        return line.strip().split()

    @timer_decorator
    def build_vocab(self) -> Dict[str, int]:
        """O(N) 단일 패스 탐색으로 어휘집 생성"""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Dataset not found at {self.data_path}")

        word_counter = Counter()
        with open(self.data_path, "r", encoding="utf-8") as f:
            for line in f:
                word_counter.update(self.preprocess_line(line))
        
        return dict(word_counter.most_common(self.config.top_k_words))

    def batch_generator(self) -> Iterator[List[str]]:
        """메모리 효율을 위한 제너레이터 기반 배치 스트리밍 ( Lazy Evaluation )"""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Dataset not found at {self.data_path}")
            
        batch = []
        with open(self.data_path, "r", encoding="utf-8") as f:
            for line in f:
                batch.append(line)
                if len(batch) == self.config.batch_size:
                    yield batch
                    batch = []
            if batch:
                yield batch