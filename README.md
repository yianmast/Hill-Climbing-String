# 🧠 Hill Climbing: String Matcher

A fun and educational Python script that uses the **hill climbing** optimization algorithm to evolve a random string into a **target string** through iterative mutation and selection.

---

## 📂 File

`hill_climb_string_matcher.py`

---

## 📌 Description

This script demonstrates a simple evolutionary technique known as **hill climbing** to match a given string. The algorithm:

- Generates a random string of the same length as the target
- Mutates it slightly (by changing one character)
- Accepts the new string if it's closer to the target
- Repeats the process until it finds an exact match

It’s a minimal yet powerful example of local search algorithms used in artificial intelligence and optimization problems.

---

## ⚙️ Features

- Randomized string generation using printable ASCII characters
- Mutation by changing one random character at a time
- Scoring based on character-by-character comparison with the target
- Output includes the number of evaluated and accepted solutions
- Progress updates every 500 evaluations

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.  
2. Download or clone this script.  
3. Run it in your terminal or IDE: python hill_climb_string_matcher.py
4. When prompted, enter a target string (e.g., hello world!).
5. Watch as the algorithm evolves the solution in real-time.

## Example Output  
Target String: hello  
Evaluations:  0  | Best score: 5  | Solution: l%90{  
Evaluations:  500  | Best score: 2  | Solution: he_lo  
Evaluations:  1000  | Best score: 0  | Solution: hello  

Evaluations: 1033 | Best score: 0 | Solution: hello  
Number of Solutions Evaluated: 1033  
Number of Solutions Accepted: 33  


## 🛠 Dependencies
Python Standard Library:

random

string

No external libraries are required.

## 👨‍💻 Author
Ioannis Mastoras  
Created: March 2020  
Updated: May 2025  

## 📘 License  
This project is open-source and free to use for educational or research purposes.


