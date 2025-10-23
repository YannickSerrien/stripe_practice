"""
Stripe Practice Problem 6 — Log Compression

Given a list of log strings, compress consecutive duplicates
by adding a count after each unique entry.

Example 1:
Input:
["OK", "OK", "ERROR", "ERROR", "ERROR", "OK"]
Output:
["OK x2", "ERROR x3", "OK x1"]

Example 2:
Input:
["INFO", "INFO", "INFO"]
Output:
["INFO x3"]

Constraints:
- 1 <= len(logs) <= 10^5
"""

def compress_logs(logs):
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    logs = ["OK", "OK", "ERROR", "ERROR", "ERROR", "OK"]
    print(compress_logs(logs))
