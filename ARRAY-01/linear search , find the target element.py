arr = [10, 25, 7, 40, 15]
target = 40
n=len(arr)

for i in range (n):
    found=arr[i]==target
    found=True
    break
if(found):
    print("target found")

else:
    print("target not in the array")    