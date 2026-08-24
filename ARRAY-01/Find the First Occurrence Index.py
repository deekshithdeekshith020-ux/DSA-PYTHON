arr = [5, 8, 2, 8, 10, 8]
target = 8
target_index=0
n=len(arr)
for i in range(n):
    if(arr[i]==target):
        print(i)
        break