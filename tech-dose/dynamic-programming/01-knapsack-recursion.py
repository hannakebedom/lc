
'''
01 knapsack recursive solution

weight (array) - the weight of an item i is located at weight[i]
profit (array) - the profit gained from item i is located at profit[i]
capacity (int) - the capacity of the knapsack
n (int) - the number of items to choose from

runtime: O(2^n)
'''
	
def zero_one_knapsack(weight, profit, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    elif weight[n] > capacity:
        # item is too heavy to fit in knapsack
        return zero_one_knapsack(weight, profit, capacity, n - 1)
    else:
        # either take the item or don't take the item, take option which yields the greater profit
        # adjust capacity and n accordingly
        return max(zero_one_knapsack(weight, profit, capacity, n - 1), 
        profit[n] + zero_one_knapsack(weight, profit, capacity - weight[n], n - 1))