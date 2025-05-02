# Minimum Operations

## Description
This project contains a Python module that calculates the minimum number of operations needed to result in exactly `n` H characters in a text file using only Copy All and Paste operations.

## Usage
To use the module, import the `minOperations` function and call it with the desired number of H characters.

## Example
```python
from minOperations import minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
