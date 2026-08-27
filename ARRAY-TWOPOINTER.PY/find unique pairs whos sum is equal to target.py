arr = [1, 2, 3, 3, 4, 4, 6, 7, 7]
target = 10

left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum < target:
        left += 1

    elif current_sum > target:
        right -= 1

    else:
        print(arr[left], arr[right])

        left += 1
        right -= 1
        
        while left < right and arr[left] == arr[left - 1]:
            left += 1
        while left < right and arr[right] == arr[right + 1]:
            right -= 1