def find_unique_number(lst):
    result = 0
    for num in lst:
        result ^= num  
    return result
numbers = [1, 1, 2, 2, 3, 3, 8, 5, 5, 6, 6, 7, 7]
unique_number = find_unique_number(numbers)
print(f"The unique number is: {unique_number}")
