arr = [1, 2, 3, 4, 5, 6, 7, 8]
target=15
slow=0

for i in range(len(arr)):
    slow=i
    fast=slow+1
    right=len(arr)-1
    while(fast<right):
       current_sum=arr[slow]+arr[fast]+arr[right]
       if(current_sum<target):
               fast+=1
       elif(current_sum>target):
               right-=1
       else:
            if(current_sum==target):
                print(arr[slow],arr[fast],arr[right])
                print("true")
                break
