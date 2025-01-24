def plusOne(digits: list[int]) -> list[int]:
    """
    You are given a large integer represented as an integer array digits, 
    where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. 
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
    """

    r = len(digits) - 1
    carry = 1

    if digits[r] < 9:
        digits[r] += 1
        return digits

    while r >= 0:
        if digits[r] == 9:
            digits[r] = 0
            carry = 1
        else:
            digits[r] += carry
            carry = 0
            break

        r -= 1

    if carry == 1:
            digits.insert(0, 1)

    return digits

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9, 9, 9, 9, 9]))