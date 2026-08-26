arr = [1, 2, 2, 3, 4, 4, 5, 6]
slow=0  ##acts as a container where we can store unique elements
fast=slow+1 #acts as a scanner where all the elements are scanned one by one
while( fast<len(arr)):
    if(arr[slow]==arr[fast]):
        
        fast+=1
        
    elif(arr[slow]!=arr[fast]):
        slow+=1
        arr[slow]=arr[fast]
        fast+=1
print(arr)        
        
           