arr = [-4, -1, -1, 0, 1, 2, 2, 3, 5]
target = 0
slow=0

for i in range(len(arr)):
    if((i>0) and arr[i]==arr[i-1]):
           continue
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
            print(arr[slow],arr[fast],arr[right])
            fast+=1
            right-=1

            while fast<right and arr[fast]==arr[fast-1]:
                fast+=1
            while fast<right and arr[right]==arr[right+1]:
                right-=1
