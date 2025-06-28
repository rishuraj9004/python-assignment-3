# 🐍 Python Assignment 3 — Functions & Modules

Welcome to **Assignment 3** for **Module 4: Functions & Modules in Python**. This repository demonstrates core programming concepts through two practical scripts:

- Custom function implementation
- Python's built-in `math` module usage
- Robust input validation

---

## 📂 Contents

- `Task_1/main.py` — Factorial calculator with recursive fallback  
- `Task_2/main.py` — Advanced math operations using Python's `math` module  

---

## 🔢 Task 1: Factorial Calculator

### 🔧 Description:
A dual-mode factorial calculator that:
- Uses **iterative calculation** (loop) by default
- Handles edge cases:
  - Negative numbers (with auto-retry)
  - Non-integer inputs (with validation)
- Returns `1` for 0 and 1 (mathematically correct)

**Key Feature:** Self-healing input system that reprompts on invalid entries.

---

## ➕ Task 2: Math Module Powerhouse

### 🔧 Description:
Leverages Python's `math` module to compute:
- Square root (√x)
- Natural logarithm (ln x)  
- Sine function (in radians)

**Precision Handling:** Uses floating-point input for maximum flexibility with:
- Automatic retry on invalid inputs
- Clean formatted output

---

## 🚀 Getting Started

### Requirements:
- Python 3.x (Tested on 3.13.1)
- No external dependencies (uses built-in `math` module)

### How to Run:
```bash
# From repository root:
python Task_1/main.py
python Task_2/main.py
