
import time

a = list(map(int, input().split()))
# a = [13, 7, 9, 5, 8, 6, 10]

n = len(a)

st = time.process_time()

# write the insertion sort code into this segment
for i in range(1, n): # start from second element ( index 1 )
    key = a[i] # store the current element
    j = i - 1 # initialize to check before current position
    while j >= 0 and a[j] > key: # while the previous element is greater than the current element
        a[j + 1] = a[j] # move the previous element to the right
        j -= 1 # move to the previous element
    a[j + 1] = key # insert the current element to the right position

et = time.process_time()

print(a)
print(et-st)
