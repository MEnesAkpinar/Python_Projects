"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

"""


def plusOne(digits):

    total = 0

    x = len(digits)

    for i in digits:

        total = total + (i)*(10**(x-1))

        x -= 1

    return list(map(int, str(total + 1)))


digits = [9]

print(plusOne(digits))
    

