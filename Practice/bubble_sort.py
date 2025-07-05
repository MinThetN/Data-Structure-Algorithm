# Bubble Sort
# Time : 0(n^2)
# Space : 0(1)

A = [-5, 1, -6, 7, 3, 5, 2, 4, 1]
def bubble_sort(arr):
    n = len(arr)
    run = True
    while run:
        run = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                run = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

bubble_sort(A)
print(A)