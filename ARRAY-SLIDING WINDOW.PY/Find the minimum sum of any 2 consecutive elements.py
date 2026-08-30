arr = [4, 2, 1, 7, 8, 1, 2]
k = 2

initial_diff=arr[0]+arr[1]
minimum=initial_diff

left=0
right=k

while(right<len(arr)):
    initial_diff=initial_diff-arr[left]+arr[right]

    if(initial_diff<minimum):
        minimum=initial_diff

    left+=1
    right+=1

print(minimum)        