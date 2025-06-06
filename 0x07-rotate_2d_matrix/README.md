# 0x07. Rotate 2D Matrix

This project involves implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The challenge focuses on matrix manipulation and in-place operations in Python.

## Project Overview

The goal of this project is to rotate a given 2D matrix in place, which means you should not use an additional matrix to perform the rotation. This task requires a solid understanding of matrix operations and efficient use of nested loops.

## Concepts Needed

1. **Matrix Representation in Python**:
   - Understanding how 2D matrices are represented using lists of lists in Python.
   - Accessing and modifying elements in a 2D matrix.

2. **In-place Operations**:
   - Performing operations on data without creating a copy of the data structure.
   - Minimizing space complexity by modifying the matrix in place.

3. **Matrix Transposition**:
   - Understanding the concept of transposing a matrix (swapping rows and columns).
   - Implementing matrix transposition as a step in the rotation process.

4. **Reversing Rows in a Matrix**:
   - Manipulating rows of a matrix by reversing their order as part of the rotation process.

5. **Nested Loops**:
   - Using nested loops to iterate through 2D data structures like matrices.
   - Modifying elements within nested loops to achieve the desired rotation.

## Resources

- [Python Official Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Official Documentation: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [GeeksforGeeks: Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [GeeksforGeeks: Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- [TutorialsPoint: Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `pycodestyle` style (version 2.8.0)
- No module imports are allowed
- All modules and functions must be documented
- All files must be executable

## Task

### 0. Rotate 2D Matrix

**Objective**: Given an n x n 2D matrix, rotate it 90 degrees clockwise in-place.

**Prototype**: `def rotate_2d_matrix(matrix):`

**Requirements**:
- Do not return anything. The matrix must be edited in-place.
- Assume the matrix will have 2 dimensions and will not be empty.

**Example**:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

**Output**:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Repository

- GitHub repository: `alx-interview`
- Directory: `0x07-rotate_2d_matrix`
- File: `0-rotate_2d_matrix.py`

## Additional Resources

- [Mock Technical Interview](https://www.pramp.com/)

## Acknowledgments

- ALX Interview Preparation
- Python Documentation
- GeeksforGeeks
