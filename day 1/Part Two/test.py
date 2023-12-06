import re

def extract_calibration_values(input_text):
    # Regular expression to find digits or spelled-out numbers
    pattern = re.compile(r'\b(?:one|two|three|four|five|six|seven|eight|nine|\d)\w*\b')
    
    # Function to convert spelled-out numbers to digits
    def convert_to_digit(match):
        word = match.group(0)
        digit_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                      'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        return digit_dict.get(word, word)
    
    # Extract and convert numbers from each line
    calibration_values = []
    for line in input_text:
        numbers = pattern.findall(line)
        digits = ''.join(map(convert_to_digit, numbers))
        if digits:
            calibration_values.append(int(digits))
    
    return calibration_values

# Example calibration document
calibration_document = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

# Extract calibration values and calculate the sum
calibration_values = extract_calibration_values(calibration_document)
sum_calibrations = sum(calibration_values)

print("Sum of calibration values:", sum_calibrations)
