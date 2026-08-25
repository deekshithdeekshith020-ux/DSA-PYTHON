##Find both
##The sum of all positive numbers
##The count of negative numbers
arr = [3, -2, 7, -5, 4, -1, 6]
sum_of_positive=0
negitive_count=0
for i in range(len(arr)):
    if(arr[i]>0):
        sum_of_positive+=arr[i]
    else:
        negitive_count+=1
print("sum_of_positive: ",sum_of_positive)
print("negitive_count: ",negitive_count)            