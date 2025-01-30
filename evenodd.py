def check_odd_even(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(f"{num} is Even")
        else:
            result.append(f"{num} is Odd")
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
odd_even_result = check_odd_even(numbers)
for result in odd_even_result:
    print(result)
