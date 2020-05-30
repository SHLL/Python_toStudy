#第二种方法
#使用字典来做（应该是，方法很巧妙）
#在for循环中通过对与nums数组的操作，以及hashmap的使用
#利用两数相和同等于两数相减来完成两数的匹配
class Soultion():
    def twoSum(self, nums, target):
        n = len(nums)
        hashmap = {}
        for x in range(n):
            a = target - nums[x]
            if nums[x] in hashmap:
                return hashmap[nums[x]], x
            else:
                hashmap[a] = x
                 

test1 = [2, 7, 11, 15]
test2 = 9
test3 = Soultion()
print(test3.twoSum(test1,test2))

