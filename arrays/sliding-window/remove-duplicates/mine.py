def removeDuplicates(nums: list[int]) -> int:
    """
    Given an integer array`nums` sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. 
    Then return the number of unique elements in `nums`.

    Consider the number of unique elements of `nums` to be `k`, 
    to get accepted, you need to do the following things:
    - Change the array nums such that the first `k` elements of `nums` contain 
    the unique elements in the order they were present in `nums` initially. 
    The remaining elements of `nums` are not important as well as the size of nums.
    - Return `k`

    Possível solução: `Sliding Window` por que quero saber o tamanho do subarray
    """

    l, r = 0, 0
    k = 1
    current_num = nums[l]

    while r < len(nums) - 1:
        r += 1

        if current_num != nums[r]:
            del nums[l+1:r]
            
            l += 1
            r = l
            k += 1
            current_num = nums[l]
            
    return k
            
nums = [1, 1, 2]
print(removeDuplicates(nums), nums)