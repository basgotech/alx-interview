#!/usr/bin/python3
"""
 script that reads stdin line by line and computes metrics:
"""

import sys

if __name__ == '__main__':

    total_file_size, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_stats = {code: 0 for code in status_codes}

    def display_stats(statistics: dict, total_size: int) -> None:
        print("File size: {:d}".format(total_size))
        for code, count in sorted(statistics.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for input_line in sys.stdin:
            line_count += 1
            data_elements = input_line.split()
            try:
                status_code = data_elements[-2]
                if status_code in status_stats:
                    status_stats[status_code] += 1
            except BaseException:
                pass
            try:
                total_file_size += int(data_elements[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                display_stats(status_stats, total_file_size)
        display_stats(status_stats, total_file_size)
    except KeyboardInterrupt:
        display_stats(status_stats, total_file_size)
        raise
