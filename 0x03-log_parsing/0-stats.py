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

if __name__ == "__main__":
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }
    line_cnt = 0


    def print_stats():
        """print the statistics of the metrix on status codes"""
        # total_size
        # status_codes
        print("File size: {}".format(total_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code]:
                print("{}: {}".format(code, status_codes[code]))


    try:
        """split the inputs in stdin into a list"""
        for line in sys.stdin:
            list_ln = line.split()
        if len(list_ln) >= 7 and list_ln[2].startswith("GET"):
            status_code = int(list_ln[-2])
            file_size = int(list_ln[-1])
            total_size += file_size
            """increment the count of status_code"""
            if status_code in status_codes:
                status_codes[status_code] += 1
        """increment line count"""
        if line_cnt % 10 == 0:
            print_stats()
        line_cnt += 1
    except KeyboardInterrupt:
        """if keyboard interrupt: print stats and exit"""
        print_stats()
        sys.exit()
