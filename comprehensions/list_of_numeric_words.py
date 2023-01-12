# def contains_digit(words):
#     """
#     Returns a list containing only the strings that have at least one numeric digit.
#     """
#     digits = "0123456789"
#     return [word for word in words if any(c in digits for c in word)]
#
# words = ["hello", "world", "1st", "2nd", "3rd"]
# print(contains_digit(words)) # should print ["1st", "2nd", "3rd"]


# def divisible_sum(numbers):
#     """
#     Returns the sum of all integers that are divisible by 3 or 5
#     """
#     result = sum([number for number in numbers if number % 3 == 0 or number % 5 == 0])
#     integers = [str(number) for number in numbers if number % 3 == 0 or number % 5 == 0]
#     integers_string = " + ".join(integers)
#     return f"{result} ({integers_string} = {result})"
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(divisible_sum(numbers))  # should print 60 (3 + 5 + 6 + 9 + 10 + 12 + 15 = 60)


# def starts_with(words, letter):
#     """
#     Returns a new list containing only the words that starts with the given letter
#     """
#     return [word for word in words if word.startswith(letter)]
#
# words = ["apple", "banana", "cherry", "date", "elderberry"]
# letter = "a"
# print(starts_with(words, letter)) # should print ["apple"]
#
# def starts_with(words, letter):
#     """
#     Returns a new list containing only the words that starts with the given letter
#     """
#     return list(filter(lambda x: x.startswith(letter), words))
#
# words = ["apple", "banana", "cherry", "date", "elderberry"]
# letter = "a"
# print(starts_with(words, letter)) # should print ["apple"]

# def long_strings(strings):
#     """
#     Returns a new list containing only the strings with more than 5 characters
#     """
#     return list(filter(lambda x: len(x) > 5, strings))
#
#
# words = ["short", "medium", "not_that_long", "this_one_is_long", "this_is_a_long_one"]
# print(long_strings(words))  # should print ["not_that_long", "this_one_is_long", "this_is_a_long_one"]


# def recent_cars(cars):
#     """
#     Returns a new list containing only the dictionaries where the value of the 'year' key is greater than 2015
#     """
#     return [car for car in cars if car['year'] > 2015]
#             # list(filter(lambda x: x['year'] > 2015, cars))
#
#
# cars = [{'make': 'Toyota', 'model': 'Camry', 'year': 2018},
#         {'make': 'Honda', 'model': 'Accord', 'year': 2012},
#         {'make': 'Ford', 'model': 'Fusion', 'year': 2019},
#         {'make': 'Chevy', 'model': 'Cruze', 'year': 2015}]
# print(recent_cars(cars))
#
# # should print [{'make': 'Toyota', 'model': 'Camry', 'year': 2018}, {'make': 'Ford', 'model': 'Fusion', 'year': 2019}]


# def multiply_by_two(numbers):
#     """
#     Returns a new list where each element is multiplied by 2
#     """
#     return list(map(lambda x: x * 2, numbers))
#     # return [x * 2 for x in numbers]
#
#
# numbers = [1, 2, 3, 4, 5]
# print(multiply_by_two(numbers)) # should print [2, 4, 6, 8, 10]


# def double_values(dictionary):
#     """
#     Returns a new dictionary where each value is multiplied by 2
#     """
#     return {key: value * 2 for key, value in dictionary.items()}
#
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(double_values(my_dict))  # should print {'a': 2, 'b': 4, 'c': 6}
