class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1] * n;
        suffixProd = [1] * n;

        for i in range(1, n):
            prefixProd[i] = prefixProd[i - 1] * nums[i - 1]
            suffixProd[n - i - 1] = suffixProd[n - i] * nums[n - i]
        ans = []

        for i in range(0, n):
            ans.append(prefixProd[i] * suffixProd[i])

        return ans


        