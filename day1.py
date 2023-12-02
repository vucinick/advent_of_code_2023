import re

def main(filename):
    calibration = []

    numbers_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }

    numbers = list(numbers_dict.keys()) + list(numbers_dict.values())

    digits_string = re.compile("|".join(numbers)).pattern

    # Capturing group is necessary for finding overlapping matches
    pattern ="(?=("+ digits_string + "))"

    with open(filename) as file:
        for line in file:
            # find all numbers ina a string (either words or digits)
            results = re.findall(pattern, line)

            
            if len(results) == 1:
                results = results[0] + results[0]
            else:
                results = results[0] + results[-1]

            
            for dig_str, dig_int in numbers_dict.items():
                results = re.sub(dig_str, dig_int, results)
            digits = re.findall("\d", results)
            
            calibration.append(int(digits[0] + digits[-1]))

    print('Sum is: ', sum(calibration))

main('day1_test_pt1.txt')
main('day1_test_pt2.txt')
main('day1_input.txt')
