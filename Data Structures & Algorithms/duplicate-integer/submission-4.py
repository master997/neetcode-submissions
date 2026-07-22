class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emptySet = set()

        for n in nums:
            if n in emptySet:
                return True
            emptySet.add(n)

        return False
        