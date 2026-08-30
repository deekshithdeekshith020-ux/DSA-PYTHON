arr = [2, 1, 5, 1, 3, 2]
k = 3

initial_sum=arr[0]+arr[1]+arr[2]
minimum_sum=initial_sum

left=0
right=k

while(right<len(arr)):
    initial_sum=initial_sum-arr[left]+arr[right]

    if(initial_sum < minimum_sum):
        minimum_sum=initial_sum

    left+=1
    right+=1

print(minimum_sum)        