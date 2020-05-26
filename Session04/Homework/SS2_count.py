#Without_Count()_function
# numbers = [1, 6, 8, 1, 2, 1, 5, 6]
# input_number = int(input('Enter a number? '))
# count = 0
# for number in numbers:
#     if number == input_number:
#         count += 1
# print(input_number, 'appears', count, 'time(s) in my list')

# With_Count()_function
numbers = [1, 6, 8, 1, 2, 1, 5, 6]
input_number = int(input('Enter a number? '))
print(input_number, 'appears', numbers.count(input_number), 'time(s) in my list')
