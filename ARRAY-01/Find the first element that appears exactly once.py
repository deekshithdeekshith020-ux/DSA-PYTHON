arr = [1, 3, 2, 3, 1, 3, 5]
n=len(arr)


for i in range (0,n):
        occurance=0
        for j in range(n):
                if(arr[i]==arr[j]):
                            occurance+=1
                            
        if(occurance==1):
                print(arr[i])
                break
                        
                                           
   

        