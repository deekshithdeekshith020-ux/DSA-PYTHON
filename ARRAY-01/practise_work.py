arr = [4, 7, 2, 9, 5]
largest_element=arr[0]
index_of_large_element=0
for i in range(len(arr)):
    if(arr[i]>largest_element):
        largest_element=arr[i]
        index_of_large_element=i
print("largest_element",largest_element)
print("index_of_large_element",index_of_large_element)        