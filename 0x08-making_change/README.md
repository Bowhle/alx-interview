# ALX Interview: 0x08 - Making Change

This project, part of the ALX Interview curriculum, focuses on solving the classic **coin change problem** using algorithmic strategies. The goal is to determine the minimum number of coins needed to meet a given amount, leveraging greedy and/or dynamic programming techniques.

---

## 🧠 Learning Objectives

- Understand the coin change problem and its real-world relevance
- Differentiate between greedy and dynamic programming approaches
- Recognize the limitations of greedy algorithms in optimization problems
- Apply dynamic programming principles:
  - Overlapping subproblems
  - Optimal substructure
- Analyze and improve algorithmic time and space complexity
- Implement efficient Python functions
- Write and interpret test cases for algorithmic correctness

---

## ⚙️ Requirements

- **Environment**: Ubuntu 20.04 LTS
- **Python**: Version 3.4.3
- **Editors**: `vi`, `vim`, `emacs`
- All files must end with a new line
- First line of all files must be: `#!/usr/bin/python3`
- Code must follow **PEP 8** style (version 1.7.x)
- All files must be executable
- `README.md` file at the root of the project is mandatory

---

## ✅ Tasks

### 0. Change comes from within (mandatory)

- Implement `makeChange(coins, total)`
- Return the **fewest number of coins** needed to meet `total`
- Return `0` if `total` is `0` or less
- Return `-1` if the total **cannot be made** with the available coins
- Assume:
  - `coins` is a list of positive integers
  - You have an **infinite** number of each coin

**Files**:
- `0-making_change.py`
- `0-main.py` (for testing)

**Example**:
```python
makeChange([1, 2, 25], 37) => 7
makeChange([1256, 54, 48, 16, 102], 1453) => -1

Run the program with ./0-main.py

📁 Repository
GitHub: alx-interview
Directory: 0x08-making_change

👩🏾‍💻 Author - Samantha B Mkwananzi – @bowhle