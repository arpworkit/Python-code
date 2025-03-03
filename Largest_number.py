def find_largest(numbers):
    if not numbers:
        return "The list is empty."
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


largest_number = find_largest(numbers)
print("The largest number is:", largest_number)

