# 🧪 Incubyte TDD Assessment - String Calculator

This repository contains solution for the Incubyte **TDD (Test Driven Development) assessment**.  
The task was to build a **String Calculator** by following proper **TDD practices** using Python and `pytest`.

---

## ✅ Features Implemented

- [x] Returns `0` for empty string input
- [x] Handles one or two comma-separated numbers
- [x] Handles unknown number of inputs
- [x] Accepts newline `\n` as delimiter along with commas
- [x] Custom single-character delimiters using `//;\n1;2` format
- [x] Throws exception for negative numbers (shows all negatives)
- [x] Ignores numbers greater than `1000`
- [x] Supports delimiters of any length — e.g. `//[***]\n1***2***3`
- [x] Supports multiple delimiters — e.g. `//[*][%]\n1*2%3`
- [x] Supports multiple delimiters of any length — e.g. `//[***][%%]\n1***2%%3`

---

## 🧪 How to Run Tests

Make sure you have `pytest` installed:
```bash
pip install pytest

Then simply run:
```bash
pytest

All tests are located in the tests/test_calculator.py file.

## 🗂️ Project Structure

```bash
incubyte-tdd/
│
├── src/
│   └── calculator.py        # Main implementation
│
├── tests/
│   └── test_calculator.py   # Unit tests using pytest
│
├── README.md
└── .gitignore

## 🧠 Thought Process

This project was built using the TDD cycle:
✅ Write a failing test
✅ Make it pass with minimum code
✅ Refactor and repeat
Commits were made frequently to demonstrate the evolution of the code, following each step of the kata.

## 📸 Sample Screenshots

## 💻 Tech Stack
Python 3.12
pytest 8.4.1
Git, GitHub
VS Code

## 👩‍💻 Author
Vidhi Kothia
Computer Engineering
Dharmsinh Desai University
Incubyte Assessment – July 2025

## 🙌 Thank You
Thanks to Incubyte for the opportunity and for promoting clean code, quality, and software craftsmanship!
