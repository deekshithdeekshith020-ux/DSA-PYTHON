##Find the Smallest Element IN THE ARRAY
arr=[54,65,32,21,11,76]
n=len(arr)
smallest_element = arr[0]

for i in range(n):
    if arr[i] < smallest_element:
        smallest_element = arr[i]

print(smallest_element)
           