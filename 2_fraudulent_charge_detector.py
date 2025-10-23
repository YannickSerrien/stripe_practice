"""
Stripe Practice Problem 2 — Fraudulent Charge Detector

You are given a list of transactions in the form:
(timestamp_in_seconds, user_id, amount)

A transaction is considered fraudulent if a user performs
3 or more transactions within any 60-second window whose
combined total amount exceeds 1000.

Return a list of fraudulent user IDs.

Example 1:
Input:
transactions = [
    (1, "A", 200),
    (20, "A", 400),
    (30, "A", 500),
    (90, "B", 700),
    (100, "B", 400)
]
Output: ["A"]

Example 2:
Input:
transactions = [
    (1, "u1", 500),
    (20, "u1", 400),
    (70, "u1", 200),
    (130, "u1", 100)
]
Output: []

Constraints:
- 1 <= len(transactions) <= 10^5
- timestamps are non-decreasing
- amounts are positive integers
"""

def fraudulent_users(transactions):
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    transactions = [
        (1, "A", 200),
        (20, "A", 400),
        (30, "A", 500),
        (90, "B", 700),
        (100, "B", 400)
    ]
    print(fraudulent_users(transactions))
