arr = [12, 5, 89, 34, 67]

largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)