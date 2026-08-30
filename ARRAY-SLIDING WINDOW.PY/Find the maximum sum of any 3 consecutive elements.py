arr = [2, 3, 1, 5, 6, 2, 4]
k = 3

current_sum=arr[0]+arr[1]+arr[2]
max_sum=current_sum

left=0
right=k
while(right<len(arr)):
    current_sum=current_sum+arr[right]-arr[left]

    if(current_sum>max_sum):
        max_sum=current_sum

    left+=1
    right+=1

print(max_sum)        