#!/usr/bin/python3

import sys

def print_statistics(total_size, status_codes):
    """Prints the computed statistics."""
    print(f"File size: {total_size}")
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        count = status_codes[code]
        print(f"{code}: {count}")

def parse_log_entry(entry):
    """Parses a log entry and extracts the file size and status code."""
    parts = entry.split()
    if len(parts) >= 7:
        status_code = parts[-2]
        file_size = int(parts[-1])
        return status_code, file_size
    return None, None

def main():
    """Main function to read log entries and compute statistics."""
    count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_entry(line.strip())
