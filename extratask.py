class Solution:
    def maximum_wealth(self, account):
        accounts = max([sum(num) for num in account])
        print(accounts)
solution = Solution()
solution.maximum_wealth([[2,3],[2,9]])