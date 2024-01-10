import timeit
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

def jump_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)

def measure_search_time(search_func, dataset, target):
    return timeit.timeit(lambda: \
        jump_search_wrapper(search_func, dataset, target), number=1000)

small_dataset = list(range(100))
medium_dataset = list(range(1000))
large_dataset = list(range(10000))

target_small = 14
target_medium = 178
target_large = 2324

time_small = measure_search_time(jump_search, small_dataset, target_small)
time_medium = measure_search_time(jump_search, medium_dataset, target_medium)
time_large = measure_search_time(jump_search, large_dataset, target_large)

print(f"Jump Search Algorithm: Target {target_small} found in {time_small:.6f} seconds")
print(f"Jump Search Algorithm: Target {target_medium} found in {time_medium:.6f} seconds")
print(f"Jump Search Algorithm: Target {target_large} found in {time_large:.6f} seconds")
