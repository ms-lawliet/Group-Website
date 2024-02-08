import timeit
def binary_search(arr, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, n) - 1)


def exponential_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)



# def binary_search_recursive(arr, target, left, right):
#     if left > right:
#         return -1

#     mid = left + (right - left) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, target, mid + 1, right)
#     else:
#         return binary_search_recursive(arr, target, left, mid - 1)

# def exponential_search_recursive(arr, target, i=1):
#     n = len(arr)
#     if arr[0] == target:
#         return 0
#     if i < n and arr[i] < target:
#         return exponential_search_recursive(arr, target, i * 2)
#     return binary_search_recursive(arr, target, i // 2, min(i, n) - 1)


# Sample array and target value
small_set = list(range(1, 101))
small_target = 29
medium_set = list(range(1, 1001))
medium_target = 998
large_set = list(range(1, 10001))
large_target = 7898

# Test iterative Exponential Search
result_iterative = exponential_search(small_set, small_target)
print(f"Iterative Exponential Search: Target {small_target} found at index {result_iterative}")
result_iterative = exponential_search(medium_set, medium_target)
print(f"Iterative Exponential Search: Target {medium_target} found at index {result_iterative}")
result_iterative = exponential_search(large_set, large_target)
print(f"Iterative Exponential Search: Target {large_target} found at index {result_iterative}")

