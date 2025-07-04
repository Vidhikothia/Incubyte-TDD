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
