numbers = [1, 2, 3, 4, 5, 9, 10, 13]
target = 10

# Binary search
left = 0
right = len(numbers) - 1
found = False

while left <= right:
    mid = (left + right) // 2  # Find the middle index
    if numbers[mid] == target:
        print("Index of", target, "is", mid)
        found = True
        break
    elif numbers[mid] < target:
        left = mid + 1  # Search in the right half
    else:
        right = mid - 1  # Search in the left half
