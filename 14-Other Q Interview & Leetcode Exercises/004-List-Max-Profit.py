"""
Instructions: 
List: Max Profit (⚡Interview Question)
You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day.

You are allowed to buy one share of the stock on one day and sell it on a later day.

Your task is to write a function called max_profit that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

Constraints:



Each element of the input list is a positive integer representing the stock price for a specific day.



Function signature: def max_profit(prices):

Example:

Input: prices = [7, 1, 5, 3, 6, 4]
Function call: profit = max_profit(prices)
Output: profit = 5

Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.
"""


def max_profit(prices: list[int]) -> int:
    # Initialize min_price to positive infinity
    min_price = float('inf')
    # Initialize max_profit to 0
    max_profit = 0
 
    # Iterate through the list of stock prices
    for price in prices:
        # Update min_price with the lowest price so far
        min_price = min(min_price, price)
        # Calculate profit by selling at the current price
        profit = price - min_price
        # Update max_profit with the highest profit so far
        max_profit = max(max_profit, profit)
 
    # Return the maximum profit after iterating
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Maximum profit:", profit)


"""
    EXPECTED OUTPUT:
    ----------------
    Maximum profit: 5

"""
