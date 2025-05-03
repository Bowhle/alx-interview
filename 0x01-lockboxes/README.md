# Lockboxes

## Description
This project contains a function `canUnlockAll` that determines if all boxes can be opened given a list of lists where each sublist contains keys to other boxes.

## Usage
To use the function, import it and pass a list of lists representing the boxes and their keys.

## Example
```python
from 0-lockboxes import canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
