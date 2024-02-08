# Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        done = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                done = False
        if done:
            break
    return arr


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while arr[j] > arr[j+1] and j >= 0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr


# Selection Sort
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


# Quick Sort
def quick_sort(arr, threshold=10):
    quick_sort_helper(arr, 0, len(arr) - 1, threshold)
    return arr


def quick_sort_helper(arr, low, hi, threshold):
    if hi - low < threshold and low < hi:
        quick_selection(arr, low, hi)
    elif low < hi:
        p = partition(arr, low, hi)
        quick_sort_helper(arr, low, p - 1, threshold)
        quick_sort_helper(arr, p + 1, hi, threshold)


def get_pivot(arr, low, hi):
    mid = (hi + low) // 2
    s = sorted([arr[low], arr[mid], arr[hi]])

    if s[1] == arr[low]:
        return low
    elif s[1] == arr[mid]:
        return mid
    return hi


def partition(arr, low, hi):
    pivot_index = get_pivot(arr, low, hi)
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, hi + 1):
        if arr[i] < pivot_value:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]

    return border


def quick_selection(arr, low, hi):
    for i in range(low, hi):
        min_index = i
        for j in range(i + 1, hi + 1):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
