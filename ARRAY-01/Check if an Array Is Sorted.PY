##Check if an Array Is Sorted
arr = [1, 2, 3, 4, 5]
n = len(arr)

sorted = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        sorted = False
        break

if sorted:
    print("Sorted")
else:
    print("Not Sorted")