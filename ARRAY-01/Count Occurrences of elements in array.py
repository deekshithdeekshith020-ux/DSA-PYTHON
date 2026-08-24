arr = [1, 2, 3, 2, 2, 2, 5]
target = 2
occurance=0
n=len(arr)
for i in range (n):
    if(arr[i]==target):
        occurance+=1
print(occurance)         