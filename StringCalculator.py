def add(input):
  if is_empty_string(input):
    return 0
  return return sum_numbers(number_string.split(","))

def is_empty_string(input):
  return input == ""

def sum_numbers(numbers):
    return sum(map(int, numbers))
