arr = [1, 2, 3, 4, 5, 6, 7, 8]
count_even=0
count_odd=0
n=len(arr)
for i in range (n):
    if(arr[i]%2==0):
        count_even+=1
    else:
        count_odd+=1
print(count_odd)
print(count_even)