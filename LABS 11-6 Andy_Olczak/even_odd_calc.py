def even_odd_calc(nums):
    odd_count = 0
    even_count = 0

    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count

# Ask user to input multiple integers separated by spaces
nums = input("Enter multiple integers separated by spaces: ").split()

# Convert the input strings to integers
nums = [int(num) for num in nums]

# Count odd and even numbers
odd_count, even_count = even_odd_calc(nums)

# Print the counts
print(f"Amount of odd numbers: {odd_count}")
print(f"Amount of even numbers: {even_count}")