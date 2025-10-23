"""
Stripe Practice Problem 3 — Charge Aggregator

You are given a list of string records representing charges:
"{user: 'A', charge: 20}"

Return a dictionary mapping each user to their total charge.

Example 1:
Input:
records = ["{user: 'A', charge: 20}", "{user: 'B', charge: 10}", "{user: 'A', charge: 5}"]
Output:
{"A": 25, "B": 10}

Example 2:
Input:
records = ["{user: 'X', charge: 100}", "{user: 'Y', charge: 100}", "{user: 'Z', charge: 100}"]
Output:
{"X": 100, "Y": 100, "Z": 100}

Constraints:
- 1 <= len(records) <= 10^4
- Each record string is properly formatted
"""

def charge_aggregator(records):
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    records = ["{user: 'A', charge: 20}", "{user: 'B', charge: 10}", "{user: 'A', charge: 5}"]
    print(charge_aggregator(records))
