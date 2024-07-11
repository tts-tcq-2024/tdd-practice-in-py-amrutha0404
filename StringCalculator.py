import re

def add(input):
    if is_empty_string(input):
        return 0
    numbers = filter_numbers(input)
    handle_negatives(numbers)
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
    
def handle_negatives(numbers):
    negative_numbers = find_negatives(numbers)
    if negative_numbers:
        raise_negatives_error(negative_numbers)

def find_negatives(numbers):
    return [num for num in numbers if int(num) < 0]

def raise_negatives_error(negative_numbers):
    raise ValueError(f"negatives not allowed: {', '.join(negative_numbers)}")
