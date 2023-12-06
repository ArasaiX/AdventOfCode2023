import regex

def extract_digits_and_words(input_string):
    pattern = regex.compile(r'(?:one|two|three|four|five|six|seven|eight|nine|zero|twone|\d+)')
    matches = pattern.findall(input_string, overlapped=True)
    return matches

def convert_spelled_numbers(list_of_numbers):
    number_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    converted_string = ''

    for number in list_of_numbers:
        if number.isdigit():
            converted_string += number
        if number.lower() in number_dict:
            converted_string += number_dict[number.lower()]
    return converted_string

def count_values(list_digits):
    sum_calibration_values = 0
    for digits in list_digits:
        first_digit = digits[0]
        last_digit = digits[-1]
        calibration_value = first_digit + last_digit
        sum_calibration_values = sum_calibration_values + int(calibration_value)
    return sum_calibration_values

file = open("../input.txt", "r")
converted_list_digits = []
for line in file:
    input_string = line
    matches = extract_digits_and_words(input_string)
    list_of_numbers = list(matches)
    converted_list_digits.append(convert_spelled_numbers(list_of_numbers))
result = count_values(converted_list_digits)
file.close()
print("The sum of calibration values is: " + str(result))
