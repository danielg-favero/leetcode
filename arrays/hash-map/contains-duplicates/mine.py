def containsDuplicate(nums: list[int]) -> bool:
        hash = {}

        for num in nums:
            if hash.get(num):
                return True
            else:
                hash[num] = 1

        return False