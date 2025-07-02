def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        print("Iteration:", i)
        for j in range(n-i-1):
            print("Comparing:", arr[j], "and", arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [ 6, 7, 3, 2, 5, 4, 1]
bubble_sort(arr)
print("Sorted array:", arr)