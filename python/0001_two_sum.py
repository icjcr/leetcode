import typing
import unittest


def two_sum(nums: typing.Iterable[int], target: int) -> tuple[int, int]:
    prev_nums = {}
    for i, num in enumerate(nums):
        difference = target - num
        try:
            return prev_nums[difference], i
        except KeyError:
            prev_nums[num] = i
    return -1, -1


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        nums_collection = ((3, 4, 6, 10, 15), (2, 7, 11, 15), (3, 2, 4), (3, 3), (6, 11, 5), ())
        target_collection = (13, 9, 6, 6, 18)
        expected_output_collection = ((0, 3), (0, 1), (1, 2), (0, 1), (-1, -1), (-1, -1))
        for nums, target, expected_output in zip(nums_collection, target_collection, expected_output_collection):
            self.assertEqual(expected_output, two_sum(nums, target))
