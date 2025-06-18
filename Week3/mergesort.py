
def merge(A, p, q, r):
    # merge the sorted A[p:q+1] with the sorted A[q+1:r+1]
    # the result is a sorted A[p:r+1]
    # Hint: an auxiliary list is required
    # Complete the body of this function
    
    # create two subarrays
    left_size = q - p + 1
    right_size = r - q
    
    # Create temporary arrays
    left_array = [0] * left_size
    right_array = [0] * right_size
    
    # Copy data to temporary arrays
    for i in range(left_size):
        left_array[i] = A[p + i]
    
    for j in range(right_size):
        right_array[j] = A[q + 1 + j]
    
    # Merge the temporary arrays back into A[p:r+1]
    i = 0  # Initial index of left subarray
    j = 0  # Initial index of right subarray
    k = p  # Initial index of merged subarray
    
    # Compare elements and merge in sorted order
    while i < left_size and j < right_size:
        if left_array[i] <= right_array[j]:
            A[k] = left_array[i]
            i += 1
        else:
            A[k] = right_array[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_array, if any
    while i < left_size:
        A[k] = left_array[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right_array, if any
    while j < right_size:
        A[k] = right_array[j]
        j += 1
        k += 1

def mergesort(A, p, r):
    if p < r:
        # Find the middle point to divide the array into two halves
        q = (p + r) // 2
        
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        
        merge(A, p, q, r)

a = list(map(int, input().split()))

import time

st = time.process_time()

mergesort(a, 0, len(a)-1)

et = time.process_time()

print(a)
print(et-st)
