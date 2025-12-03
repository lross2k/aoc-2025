import re

# even
# 6 char, can be 2x3, 3x2 or 1x6
# 10 char, can be 2x5, 5x2 or
# 14 char, can be 2x7 or 7x2
# uneven
# 9 char, can be 3x3
# 11 char
# 5 char is not possible unless 5x1
# prime numbers ex 2, 3, 5, 7, 11, 13
nums = ['222222',
'1188511885',
'21212121212121',
'824824824',
'99999999999',
'824824824',
'88888',
'13531355',
'111']

def detect_repeating(number: str):
    num_len = len(number)
    if num_len % 2 == 0:
        half_len = int(num_len / 2)
        first_half = number[0:half_len]
        last_half = number[half_len:]
        if first_half == last_half:
            return first_half
        else:
            for n in range(1, half_len):
                semi_number = number[0:n]
                regex = re.findall(semi_number, number)
                if len(regex) == num_len/n:
                    return semi_number
    else:
        half_len = int(num_len / 2)
        for n in range(1, half_len+1):
            semi_number = number[0:n]
            regex = re.findall(semi_number, number)
            if len(regex) == num_len/n:
                return semi_number

def main():
    for num in nums:
        print(detect_repeating(num))

if __name__ == "__main__":
    main()
