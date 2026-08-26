arr = [4, 2, 7, 4, 2, 7]
n=len(arr)
for i in range(n):
    first_occurance=0
    for j in range(n):
            if(arr[i]==arr[j]):
                first_occurance+=1
                    
    if(first_occurance==2):
        print(arr[i])
        break
        