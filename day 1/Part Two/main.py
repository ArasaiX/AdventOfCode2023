
def main():
    file = open("../input.txt", "r")
    sum_calibration_values = 0
    for line in file:
        print(line)
        digit_line = []
        calibration_value = ''
        for char in line:
           if char.isdigit():
               digit_line.append(char)
        first_digit = get_first_digit(line, digit_line[0])
        last_digit = get_last_digit(line, digit_line[-1])
        calibration_value = first_digit + last_digit
        print("The calibration value is: " + str(calibration_value))
        sum_calibration_values = sum_calibration_values + int(calibration_value)
    print("The sum of calibration values is: " + str(sum_calibration_values)) 
    file.close()

def get_first_digit(line, digit):
    index = line.index(digit)   
    if index == 0 or index == 1:
        return str(digit)
    else:
        start_line = line[:index]
        return check_if_str_is_digit(start_line)

def get_last_digit(line, digit):
    index = line.index(digit)
    print(index)
    if index == len(line) or index == len(line) - 1:
        return str(digit)
    else:
        end_line = line[index:]
        return check_if_str_is_digit(end_line)

def check_if_str_is_digit(line):
    if 'one' in line:
        return '1'
    elif 'two' in line:  
        return '2'
    elif 'three' in line:
        return '3'
    elif 'four' in line:
        return '4'
    elif 'five' in line:
        return '5'
    elif 'six' in line:
        return '6'
    elif 'seven' in line:
        return '7'
    elif 'eight' in line:
        return '8'
    elif 'nine' in line:
        return '9'
    else:  
        return '0'

main()
