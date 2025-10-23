"""
Stripe Practice Problem 7 — Rate Limiter

Implement a rate limiter that allows at most 3 requests
per 1000 milliseconds (1 second) per user.

You are given a sorted list of events (timestamp_in_ms, user_id).
For each event, return "allow" or "block" depending on whether
the request should be processed.

Example 1:
Input:
events = [(100, "A"), (200, "A"), (250, "A"), (900, "A"), (950, "A")]
Output:
["allow", "allow", "allow", "allow", "block"]

Example 2:
Input:
events = [(0, "u1"), (100, "u1"), (200, "u1"), (1200, "u1")]
Output:
["allow", "allow", "allow", "allow"]

Constraints:
- timestamps are non-decreasing
- 1 <= len(events) <= 10^5
"""

def rate_limiter(events):
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    events = [(100, "A"), (200, "A"), (250, "A"), (900, "A"), (950, "A")]
    print(rate_limiter(events))
