#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics
Attributes:
    global variables: total_size, status_codes, line_cnt
        total_size: size of the file
        status_codes: dictionary with all status codes and count
        line_cnt: no of lines
    print_stats: function that prints the file size and the
                status code and count
The module uses try, except block that loops through the
stdin line and checks the status code of each GET request
Exists if interrupted by keyboard and prints the statistics
"""
import sys
import re
import signal

if __name__ == "__main__":
    total_file_size = 0
    status_code_cnt = {}
    line_count = 0

    pattern = r"(\S+) - \[(.+)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)"

    def print_metrics():
        """print the statistics of the metrix on status codes"""
        global total_file_size, status_code_cnt
        print("File size: {}".format(total_file_size))
        for status in sorted(status_code_cnt):
            print("{}: {}".format(status, status_code_cnt[status]))

    try:
        for line in sys.stdin:
            line_count += 1
            match = re.match(pattern, line)
            if match:
                ip, date, status, size = match.groups()
                size = int(size)
                total_file_size += size
                status_code_cnt[status] = status_code_cnt.get(
                    status, 0) + 1
                if line_count % 10 == 0:
                    print_metrics()
                    line_count += 1
    except KeyboardInterrupt:
        """if keyboard interrupt: print stats and exit"""
        print_metrics()
        sys.exit()
