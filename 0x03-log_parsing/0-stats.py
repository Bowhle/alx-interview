#!/usr/bin/python3
"""
Read stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>, skip line if not this format
After every 10minutes or keyboard interrupt (CTRL + C)
print these from beginning: number of lines by status code
possible status codes: 200, 301, 400, 401, 404, 405, and 500
if status code isn't an integer, do not print it
format: <status code>: <number>
Status code must be printed in ascending order
"""
import sys
import time

def print_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))

file_size = 0
codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_count = 0
try:
    for line in sys.stdin:
        line_count += 1
        # parse the line and extract the status code and file size
        # (assuming the input format is correct)
        status_code = int(line.split()[-2])
        file_size += int(line.split()[-1])
        codes[status_code] += 1

        if line_count % 10 == 0:
            print_msg(codes, file_size)
            codes = {k: 0 for k in codes.keys()}
            file_size = 0

except KeyboardInterrupt:
    print_msg(codes, file_size)
