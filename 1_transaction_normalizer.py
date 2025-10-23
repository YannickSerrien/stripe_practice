"""
Stripe Practice Problem 1 — Transaction Normalizer

You are given a list of transactions between users in the format:
"sender,receiver,amount,currency"

You must compute each user's net balance in USD using the provided
exchange rates dictionary.

Example 1:
Input:
transactions = ["alice,bob,50,USD", "bob,charlie,100,EUR", "charlie,alice,1000,JPY"]
rates = {"USD": 1.0, "EUR": 1.1, "JPY": 0.006}
Output:
{"alice": 56.0, "bob": -55.0, "charlie": -1.0}

Example 2:
Input:
transactions = ["x,y,10,USD", "y,z,5,USD", "z,x,15,USD"]
Output:
{"x": 5.0, "y": 5.0, "z": -10.0}

Constraints:
- 1 <= len(transactions) <= 10^4
- Each transaction is valid and well formatted
"""

def transaction_normalizer(transactions, rates):
    # TODO: Implement your solution here
    pass


if __name__ == "__main__":
    # Example test case
    transactions = [
        "alice,bob,50,USD",
        "bob,charlie,100,EUR",
        "charlie,alice,1000,JPY"
    ]
    rates = {"USD": 1.0, "EUR": 1.1, "JPY": 0.006}
    print(transaction_normalizer(transactions, rates))
