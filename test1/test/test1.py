all_in_list=[
    1,              #整数
    1.0,            #浮点数
    'a word',       #字符串
    print(1),       #函数
    True,           #布尔值
    [1,2],          #列表中套列表
    (1,2),          #元组
    {'key':'value'} #字典
]
#元组(Tuple)
letters = ('a','b','c','d','e','f','g')
print(letters[0])
#列表(list)
list1 = ['a','b','c','d','e','f','g']
print(list1[0])
#字典(Dictionary)
code = {
    '1':'first',
    '2':'double'
}
print(code['1'])
#集合(Set)
a_set = {1,2,3,4}
a_set.add(5)        #添加
a_set.discard(5)    #删除
print(a_set)

num_list = [6,2,7,4,1,3,5]
print(sorted(num_list))
print(sorted(num_list,reverse=True))   #reverse参数为True反排序

num=[1,2,3,4,5,6,3,2,1,2]
str=[2,1,3,4,5,7,54,3,2,1]
for a,b in zip(num,str):
    print(b,'is',a)

#列表一般循环添加
a = []
for i in range(1,11):
    a.append(i)
print(a)
#列表解析式添加
b = [i for i in range(1,11)]
print(b)



