#arr = [1, 2, 4, 6, 8, 10, 13]
arr=[1,2,4,6,8,9,13,14]
target = 14
left=0
right=len(arr)-1
sum=0

while(left<right):
    
    sum=arr[left]+arr[right]
    if(sum==target):
        print("true")
        break
    elif(sum<target):
        left+=1
    elif(sum>target):
        right-=1 
         

        