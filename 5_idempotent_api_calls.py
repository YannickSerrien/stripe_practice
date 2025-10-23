"""
Stripe Practice Problem 5 — Idempotent API Calls

Each API call is represented as a tuple:
(idempotency_key, user_id, amount)

If multiple calls share the same idempotency_key,
only the first should be processed.

Return a dictionary mapping user_id to their total processed amount.

Example 1:
Input:
calls = [
    ("x1", "alice", 50),
    ("x1", "alice", 50),
    ("x2", "bob", 100)
]
Output:
{"alice": 50, "bob": 100}

Example 2:
Input:
calls = [
    ("k1", "a", 10),
    ("k2", "a", 20),
    ("k1", "a", 10)
]
Output:
{"a": 30}

Constraints:
- 1 <= len(calls) <= 10^5
- idempotency_key values are strings
"""

def idempotent_totals(calls):
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    calls = [
        ("x1", "alice", 50),
        ("x1", "alice", 50),
        ("x2", "bob", 100)
    ]
    print(idempotent_totals(calls))
