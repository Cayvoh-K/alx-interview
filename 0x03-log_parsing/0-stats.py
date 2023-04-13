#!/usr/bin/python3
""" a script that reads stdin line by line and computes metric"""


import sys
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0


try:
    for line in sys.stdin:
        line = line.strip()
        # parse the line
        try:
            ip_address, date, request, status_code, file_size = line.split()
            if request != "GET /projects/260 HTTP/1.1":
                continue
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        # print metrics every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: {total_file_size}')
            for status_code in sorted(status_code_counts.keys()):
                print(f'{status_code}: {status_code_counts[status_code]}')
            print()

except KeyboardInterrupt:
    # print final metrics on keyboard interrupt
    print(f'Total file size: {total_file_size}')
    for status_code in sorted(status_code_counts.keys()):
        print(f'{status_code}: {status_code_counts[status_code]}')
