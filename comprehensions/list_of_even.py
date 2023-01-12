def even_numbers(numbers):
    """
    Returns a list containing only the even numbers from the original list.
    """
    return [number for number in numbers if number % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers(numbers)) # should print [2, 4, 6, 8, 10]