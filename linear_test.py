import timeit
from linear_search import linear_search, linear_search_wrapper

# Sample array and target value
small_set = range(1, 101)
target1 = 12
medium_set = range(1, 1001)
target2 = 524
large_set = range(1, 10001)
target3 = 6983

# Test interpolation_search
execution_time_small = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": small_set, "target": target1}, number=1) * 1000

execution_time_medium = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": medium_set, "target": target2}, number=1) * 1000

execution_time_large = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": large_set, "target": target3}, number=1) * 1000


result_linear = linear_search(small_set, target1)
print(f"Linear Search: Target {target1} found at index {result_linear} in {execution_time_small: .6f} milliseconds")

result_linear = linear_search(medium_set, target2)
print(f"Linear Search: Target {target2} found at index {result_linear} in {execution_time_medium: .6f} milliseconds")

result_linear = linear_search(large_set, target3)
print(f"Linear Search: Target {target3} found at index {result_linear} in {execution_time_large: .6f} milliseconds")
