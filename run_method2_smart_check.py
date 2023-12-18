# ====================================================================================================
# Python Experiment : Method 2 : Smart Sum : O(n)
# ----------------------------------------------------------------------------------------------------
# Logic

def find_sum_index(values: list, target: int) -> tuple:
	# Initialize the final answer as (m, n) | index start at 1
	i = 0
	m = 1
	n = 1
	limit = len(values)
	score = values[0] # Set the pointer at the first element as the initial sum of score
	print('input:', values, ' target:', target, ' limit:', limit, ' max_pointers_if_brute_force:', limit*(limit-1))
	# Loop to check score and target
	while True:
		i = i + 1
		print(f'pointer{i}: index=({m},{n}) score={score}', '<' if score < target else '>' if score > target else '=', 'target')
		# Case 1 : Sum the score with the next element (on the right)
		if score < target:
			n = n + 1
			if n > limit:
				return None
			score = score + values[n-1]
		# Case 2 : Deduct the score by dropping the first element (on the left)
		elif score > target:
			score = score - values[m-1]
			m = m + 1
			if m > limit:
				return None
		# Case 3 : Finish
		elif score == target:
			return (m, n)


# ----------------------------------------------------------------------------------------------------
# Test

print('\ntest_case_1')
print('output:', find_sum_index([1,2,5,9,10,13], 24)) # result = (3, 5)

print('\ntest_case_2')
print('output:', find_sum_index([1,5,10,13,15], 17)) # result = None

print('\ntest_case_3')
print('output:', find_sum_index([1,2,3,5,10,20,21,30], 51)) # result = (5, 7)

print('\ntest_case_4')
print('output:', find_sum_index([1,8,9,13,15,16,22,23], 38)) # result = (6, 7)

print('\ntest_case_5')
print('output:', find_sum_index([1,3,4,6], 15)) # result = None

