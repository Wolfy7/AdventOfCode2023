
# Part 1
with open('Day_01/input_1.txt') as f:
    data = f.read().splitlines()

sum = 0
for line in data:
    digits = [digit for digit in line if digit.isdigit()]
    # print(digits)
    if len(digits) > 2:
        calibration_value = digits[::len(digits)-1]
    elif len(digits) == 1:
        calibration_value = [digits[0], digits[0]]
    else:
        calibration_value = digits
    # print(calibration_value)
    sum += int(''.join(calibration_value))

print(sum)

# Part Two
import regex as re

with open('Day_01/input_1.txt') as f:
    data = f.read().splitlines()

letters = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

sum = 0
pattern = re.compile('(one|two|three|four|five|six|seven|eight|nine|\d+)')
for line in data:
    res = re.findall(pattern, line, overlapped=True)

    digits = ''.join([number if number.isdigit() else str(letters[number]) for number in res])

    if len(digits) > 2:
        calibration_value = digits[::len(digits)-1]
    elif len(digits) == 1:
        calibration_value = digits[0] + digits[0]
    else:
        calibration_value = digits
    sum += int(calibration_value)

print(sum)