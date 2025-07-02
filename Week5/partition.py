
import sys
sys.setrecursionlimit(10000)

# Global counter variable
counter = 0

def partition(A, p, r):  # Lomuto's partition scheme
    global counter
    x = A[r]
    i = p-1
    for j in range(p, r):
        counter += 1  # Count the most frequently executed line
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)  # Partition and get pivot index
        quicksort(A, p, q-1)    # Sort left subarray
        quicksort(A, q+1, r)    # Sort right subarray

def quick_sort(arr):
    if len(arr) <= 1:
        return
    quicksort(arr, 0, len(arr)-1)

if __name__ == "__main__":
    # Reset counter
    counter = 0
    
    input_line = sys.stdin.read().split()
    arr = list(map(int, input_line))
    
    quick_sort(arr)
    print("Quick sorted array:", arr)
    print("Counter: ", counter)


