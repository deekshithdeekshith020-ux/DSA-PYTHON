## TO REVERSE AN ARRAY
arr = [11, 12, 13, 14, 15]
left=0
right=len(arr)-1
while (left < right):
    arr[right],arr[left]=arr[left],arr[right]


    left+=1
    right-=1
print(arr)    
    
      
      