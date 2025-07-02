def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]
    left_arr = [val for val in arr[:len(arr)-1] if val <= pivot]
    right_arr = [val for val in arr[:len(arr)-1] if val > pivot]
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

import time
st = time.process_time()

import sys
input_line = sys.stdin.read().split()
arr = list(map(int, input_line))

print("Original array:", arr)
arr = quick_sort(arr)  # Assign the sorted result back to arr

et = time.process_time()
print("Quick sorted array:", arr)
print("Time:", et-st)
