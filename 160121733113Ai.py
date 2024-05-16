def find_subarrays(arr, n, sum):
    current_sum = arr[0]
    start = 0

    # Iterate through the array
    for i in range(1, n):
        # Add the current element to the current sum
        current_sum += arr[i]

        # If the current sum is equal to the given sum,
        # print the subarray
        if current_sum == sum:
            print("Subarray found from index", start, "to index", i)

        # If the current sum is greater than the given sum,
        # remove elements from the start of the subarray
        # until the current sum is less than or equal to the given sum
        while current_sum > sum:
            current_sum -= arr[start]
            start += 1

# Driver code
arr = [1, 4, 2, 0, 5, 3]
n = len(arr)
sum = 7

find_subarrays(arr, n, sum)