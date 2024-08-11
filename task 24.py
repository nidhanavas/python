def find_second_smallest_and_third_largest(numbers):
    sorted_numbers = sorted(set(numbers))
    return sorted_numbers[1], sorted_numbers[-3]

numbers = [7, 10, 2, 8, 5, 6, 3, 9]
second_smallest, third_largest = find_second_smallest_and_third_largest(numbers)
print("Second smallest number:", second_smallest)
print("Third largest number:", third_largest)