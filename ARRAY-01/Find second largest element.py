print("hello world")
arr = [12, 35, 1, 10, 34, 1]
largest=arr[0]
slargest=0
n=len(arr)
for i in range (n):
    if(arr[i]>largest):
        slargest=largest
        largest=arr[i]
    elif(arr[i]<largest and arr[i]>slargest):
        slargest=arr[i]

print(slargest)    


