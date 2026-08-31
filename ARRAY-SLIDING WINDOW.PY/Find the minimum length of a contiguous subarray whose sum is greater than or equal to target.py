arr = [2, 1, 5, 2, 3, 2]
target = 7

left = 0
right = 0
current_sum = 0
min_length = len(arr)

while right < len(arr):

    if current_sum < target:
        current_sum += arr[right]
        right += 1

    elif current_sum >= target:

        length = right - left

        if length < min_length:
            min_length = length

        current_sum -= arr[left]
        left += 1

print(min_length)