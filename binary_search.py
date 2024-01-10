
import timeit
def binary_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binary_search_wrapper1(array, target):
    return binary_search(arr, target)

def binary_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)

# def binary_search_recursive(arr, target, low, high):
#     if low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return binary_search_recursive(arr, target, mid + 1, high)
#         else:
#             return binary_search_recursive(arr, target, low, mid - 1)

#     return -1

#def binary_search
numbers = range(1, 10001)
test_data = ", ".join(map(str, numbers))
target = 11
arr = list(map(int, test_data.split(",")))
execution_time = timeit.timeit("binary_search_wrapper(binary_search, arr, target)", globals=globals(), number=1)   
result = binary_search_wrapper(binary_search, arr, target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Resoult found in index: {result} ")

# sample array and target value
small_numbers = range(1, 101)
test_data1 = ", ".join(map(str, small_numbers))
small_target = 31
small_set = list(map(int, test_data.split(",")))

medium_numbers = range(1, 1001)
test_data2 = ", ".join(map(str, medium_numbers))
medium_target = 889
medium_set = list(map(int, test_data.split(",")))

large_numbers = range(1, 10001)
test_data3 = ", ".join(map(str, large_numbers))
large_target = 9867
large_set = list(map(int, test_data.split(",")))

# execution time and result
small_result = binary_search_wrapper(binary_search, small_set, small_target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {small_result} ")

medium_result = binary_search_wrapper(binary_search, medium_set, medium_target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {medium_result} ")

large_result = binary_search_wrapper(binary_search, large_set, large_target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Result found in index: {large_result} ")


