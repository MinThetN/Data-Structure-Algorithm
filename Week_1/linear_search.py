numbers = [13, 20, 9, 5, 7, 3, 8, 4]
find_number = 3

# start from the first item and check each one
for i in range(len(numbers)):
    if numbers[i] == find_number:
        print("Index of", find_number, "is", i)
        break
else:
    print(find_number, "is not in the list")
