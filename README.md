# Final Project: Python Code Optimization (Student Starter Project)

Welcome to the Final Project Starter Code! 

This repository contains a mock NLP data processing and training pipeline. The code inside `src/train.py` **runs perfectly fine and will not crash**, but it is **extremely inefficient and poorly structured**. 

Your goal is to apply the optimization and refactoring techniques you learned in class to significantly improve the performance, memory usage, and maintainability of this code.

## 🎯 Your Mission

The `train.py` script violates several best practices we discussed in class. You must identify these bottlenecks and fix them. Specifically, try to apply at least **3 out of the 5** core concepts from the assignment instructions:

1. **A. 자료구조 및 복잡도 기반 개선:** Is the code using the right data structures? Are there hidden $O(N^2)$ operations?
2. **B. Iterator, Generator, Lazy Evaluation:** Is the code loading massive amounts of data into memory at once? Can you make it lazy?
3. **C. Class 기반 구조 개선 (SRP):** Is this just one giant function doing everything? Can you split it into a `Config`, `DataProcessor`, and `Trainer` class?
4. **D. Decorator 기반 개선:** Are logging and execution time measurements cluttering the core logic? Can you abstract them into decorators?
5. **E. 딥러닝·LLM 연구 코드 최적화:** (If applicable to your specific domain, though A~D are heavily featured here).

## 🚀 How to Run the Baseline

1. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate the Synthetic Dataset:**
   Because this is a mock project, you need to generate the dataset first. This will create a large text file in the `data_utils/` folder.
   ```bash
   python data_utils/generate_dataset.py
   ```

3. **Run the Inefficient Baseline:**
   ```bash
   python src/train.py
   ```
   *Note: Pay close attention to how long it takes and how much memory it uses! You may want to use a tool like `memory_profiler` to measure the peak memory usage of your baseline and compare it to your optimized version.*

## 📝 Submission Guidelines
Please refer to the `instruction.txt` provided in the LMS for the full submission guidelines, including how to structure your GitHub repository (e.g., `before/` and `after/` folders) and what to include in your final PDF report.

Good luck!
