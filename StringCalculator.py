import re

def add(input):
    if is_empty_string(input):
        return 0
    numbers = filter_numbers(input)
    return sum_numbers(numbers)

def filter_numbers(input):
  numbers = re.findall(r'-?\d+', input)
  return numbers
  
def is_empty_string(number_string):
    return number_string == ""

def sum_numbers(numbers):
    number_list = []
    for number in numbers:
        if int(number) < 1000:
            number_list.append(int(number))
    return sum(number_list)
