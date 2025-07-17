nums = [1, 3, 1, 3, 2, 1]
frequency = {}

# Count frequencies
for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Find the most frequent number
most_frequent = None
max_count = 0

for num, count in frequency.items():
    if count > max_count:
        most_frequent = num
        max_count = count

print(f"{most_frequent} appears {max_count} times")
