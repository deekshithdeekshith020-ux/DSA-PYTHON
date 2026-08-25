arr = [5, 2, 8, 2, 9, 2, 4]
target=2
appearance=0
appearance_index=0
for i in range(len(arr)):
    if(arr[i]==target):
        appearance=arr[i]
        appearance_index=i
        break
print("appearance",appearance)
print("appearance_index: ",appearance_index)