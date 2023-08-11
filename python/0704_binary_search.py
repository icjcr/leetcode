def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        middle = (right + left) // 2
        val = nums[middle]
        if val < target:
            left = middle + 1
        elif val > target:
            right = middle
        else:
            return middle

    return -1
