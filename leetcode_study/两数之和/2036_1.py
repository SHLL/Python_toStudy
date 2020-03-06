class Solution:
    def twoSum(self,nums,target):
        # 将输入的nums数组通过sorted方法来转换为一个新的列表，该列用来存储nums数组的地址值
        # python中四种数据结构：列表，字典，集合，元组
        id = sorted(range(len(nums)),key = lambda k:nums[k])
        head = 0
        tail = len(nums) - 1
        # head用来作为开始的标记   head从逐渐增大
        # tail用来作为末尾的标记   tail逐渐减小
        # 以此，来达到数组中的每个数据遍历一遍
        # 在通过sum_result的值来完成数值的循序相加 两两相和
        sum_result = nums[id[head]] + nums[id[tail]]
        # 将id中存储的地址值所对应的数值进行相加运算

        while sum_result != target:
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
            sum_result = nums[id[head]] + nums[id[tail]]
        # 通过while循环来筛选出满足条件的id列表的地址值

        return [id[head],id[tail]]
        # 将满足的地址值对应的数值返回