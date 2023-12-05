
def main():
    file = open("../input.txt", "r")
    sum_calibration_values = 0
    for line in file:
        digit_line = []
        calibration_value = ''
        for char in line:
           if char.isdigit():
               digit_line.append(char)
        first_digit = digit_line[0]
        last_digit = digit_line[-1]
        calibration_value = first_digit + last_digit
        sum_calibration_values = sum_calibration_values + int(calibration_value)
    print("The sum of calibration values is: " + str(sum_calibration_values)) 
    file.close()

main()
