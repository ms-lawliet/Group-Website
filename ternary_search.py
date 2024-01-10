import timeit

def ternary_search(arr, target, left, right):
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1

def ternary_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)

def measure_search_time(search_func, dataset, target):
    return timeit.timeit(lambda: \
        ternary_search_wrapper(search_func, dataset, target, 0, len(dataset) - 1), number=1000)

# Create datasets
small_dataset = list(range(100))
medium_dataset = list(range(1000))
large_dataset = list(range(10000))

# Test the algorithm on each dataset
target_small = 23
target_medium = 12
target_large = 100

time_small = measure_search_time(ternary_search, small_dataset, target_small)
time_medium = measure_search_time(ternary_search, medium_dataset, target_medium)
time_large = measure_search_time(ternary_search, large_dataset, target_large)

print(f"Ternary Search: Target {target_small} found in {time_small:.6f} milliseconds")
print(f"Ternary Search: Target {target_medium} found in {time_medium:.6f} milliseconds")
print(f"Ternary Search: Target {target_large} found in {time_large:.6f} milliseconds")