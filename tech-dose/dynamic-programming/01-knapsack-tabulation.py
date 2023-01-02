'''
01 knapsack iterative solution with tabulation
runtime: O(n * capacity)

weight (array) - the weight of an item i is located at weight[i]
profit (array) - the profit gained from item i is located at profit[i]
capacity (int) - the capacity of the knapsack
n (int) - the number of items to choose from
'''

def zero_one_knapsack(weight, profit, capacity, n):
	mem = [[-1] * (n + 1) for i in range(capacity + 1)]
	for i in range(n):
		for j in range(capacity):
			if i == 0 or j == 0:
                # if there are no items or the knapsack has no capacity, the max profit is 0
				mem[i][j] = 0
			elif weight[i - 1] > j:
				# if the current item does not fit in knapsack take the max profit for the last item that did fit
				mem[i][j] = mem[i-1][j]
			else:
                # either take the item or don't take the item, take option which yields the greater profit
				mem[i][j] = max(mem[i-1][j], profit[i-1] + mem[i-1][capacity - weight[i - 1]])