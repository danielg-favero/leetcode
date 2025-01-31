def numberOfSteps(num: int) -> int:
        """
        Given an integer num, return the number of steps to reduce it to zero.

        In one step, if the current number is even, you have to divide it by 2, 
        otherwise, you have to subtract 1 from it.
        """
        steps = 0
        
        while num:
            if num & 1:
                num -= 1
            else:
                num = num >> 2

            steps += 1

        return steps

print(numberOfSteps(14))