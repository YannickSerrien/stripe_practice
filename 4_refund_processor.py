"""
Stripe Practice Problem 4 — Refund Processor

You are given two lists:
- charges = list of tuples (charge_id, amount)
- refunds = list of tuples (refund_id, charge_id, amount)

Each refund applies to its charge if the refund amount
is less than or equal to the remaining charge amount.
If the refund exceeds the charge, ignore it.

Return a dictionary mapping charge_id to the remaining amount
after valid refunds.

Example 1:
Input:
charges = [("c1", 100), ("c2", 200)]
refunds = [("r1", "c1", 50), ("r2", "c2", 300)]
Output:
{"c1": 50, "c2": 200}

Example 2:
Input:
charges = [("x", 150)]
refunds = [("r1", "x", 100), ("r2", "x", 30)]
Output:
{"x": 20}

Constraints:
- 1 <= len(charges), len(refunds) <= 10^4
- All charge_ids are unique
"""

def refund_processor(charges, refunds):
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    charges = [("c1", 100), ("c2", 200)]
    refunds = [("r1", "c1", 50), ("r2", "c2", 300)]
    print(refund_processor(charges, refunds))
