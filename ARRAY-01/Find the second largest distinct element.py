arr = [4, 1, 7, 3, 9, 2]
largest=arr[0]
s_largest=float('-inf')
for i in range(len(arr)):
    if(arr[i]>largest and arr[i]!=largest):
        s_largest=largest
        largest=arr[i]
    
    elif(arr[i]> s_largest  and arr[i]!=largest):
        s_largest=arr[i]
        
print(s_largest)        