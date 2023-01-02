'''
01 knapsack recursive solution with memoization
runtime: O(n * w), where n is the number of items and w is the capacity of the knapsack

weight (array) - the weight of an item i is located at weight[i]
profit (array) - the profit gained from item i is located at profit[i]
capacity (int) - the capacity of the knapsack
n (int) - the number of items to choose from
'''

def zero_one_knapsack(weight, profit, capacity, n):
	mem = [[-1] * n for i in range(capacity + 1)]
	
	def helper(capacity, n):
		result = -1
		if n == 0 or capacity == 0:
			return 0
		elif mem[capacity][n] != -1:
			return mem[capacity][n]
		elif weight[n] > capacity:
			result = helper(capacity, n - 1)
		else:
			result = max(helper(capacity, n - 1), profit[n] + helper(capacity - weight[n], n - 1))

		mem[capacity][n] = result
		return result 