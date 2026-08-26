arr = [0, 1, 0, 3, 12, 0, 5]
unique_storer=0
scanner=unique_storer+1
while(scanner<len(arr)):
    if(arr[unique_storer]==0 and arr[scanner]!=0):
        arr[unique_storer],arr[scanner]=arr[scanner],arr[unique_storer]
        scanner+=1
        unique_storer+=1
    elif(arr[unique_storer]==0 and arr[scanner]==0):
        scanner+=1
    elif(arr[unique_storer]!=0 and arr[scanner]!=0):
        scanner+=1        
        
print(arr)