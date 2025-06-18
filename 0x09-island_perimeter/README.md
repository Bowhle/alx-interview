# Island Perimeter - ALX Interview Project

This is a Python implementation I wrote to compute the perimeter of an island in a 2D grid.

---

## Problem Description

Given a rectangular grid of integers where:
- `0` represents **water**
- `1` represents **land**

I'm tasked with calculating the perimeter of a single contiguous island. Cells are connected **horizontally** and **vertically** only.

> The problem guarantees there's at most one island, and it doesn't include any internal lakes.

### Example:
```python
# Example grid
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# Expected output: 12
print(island_perimeter(grid))
```

---

## File Structure
```
0x09-island_perimeter/
├── 0-island_perimeter.py   # My main implementation
├── 0-main.py               # Test script I use to check the output
└── README.md               # This documentation
```

---

3. **Run the script**:
   - I make sure the Python extension is installed in VS Code
   - Then I either use the terminal or click `Run Python File` from the editor:
   ```bash
   python3 0-main.py
   ```

> I also ensure scripts are executable on Unix systems with:
> ```bash
> chmod +x 0-island_perimeter.py 0-main.py
> ```

---

## How the Algorithm Works
When I iterate through each cell in the grid, I check if the cell is land (`1`). For every land cell, I examine its four sides—top, bottom, left, and right. If a side is either at the grid boundary or touches water, I count it as part of the perimeter.

| Side     | Condition                            |
|----------|----------------------------------------|
| Top      | `i == 0` or `grid[i-1][j] == 0`         |
| Bottom   | `i == rows-1` or `grid[i+1][j] == 0`    |
| Left     | `j == 0` or `grid[i][j-1] == 0`         |
| Right    | `j == cols-1` or `grid[i][j+1] == 0`    |

### Complexity
- **Time:** O(R × C) — I go through each cell once
- **Space:** O(1) — No extra space is used

---

## Test Cases I Use
```python
from 0-island_perimeter import island_perimeter

# A single land cell
print(island_perimeter([[1]]))  # 4

# A square block of land
print(island_perimeter([[1, 1], [1, 1]]))  # 8

# An L-shaped island
print(island_perimeter([[0, 1, 0, 0], [1, 1, 1, 0]]))  # 14
```

---

## Environment & Constraints
- Python 3.4+
- No imports or external libraries allowed
- Meant to run on Ubuntu 20.04 LTS
- I follow [PEP 8](https://pep8.org) (v1.7) coding style
- All Python files start with `#!/usr/bin/python3` and are made executable

---

## Author
I'm **Bowhle Mkwananzi**, the developer behind this solution.  
Contact: <bowhlem@gmail.com>