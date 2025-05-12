#!/usr/bin/python3

import sys
import re
from collections import defaultdict

def print_stats(status_counts, total_file_size):
    """
    Prints the accumulated statistics.

    Args:
        status_counts (dict): Dictionary storing the count of each status code.
        total_file_size (int): The total size of all processed files.

    Returns:
        None
    """
    # Print the total file size and the counts of each status code
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

total_file_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        match = re.match(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
            r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)',
            line
        )
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))
            total_file_size += file_size
            status_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats(status_counts, total_file_size)

except KeyboardInterrupt:
    print_stats(status_counts, total_file_size)

finally:
    print_stats(status_counts, total_file_size)
    