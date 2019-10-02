import time

a = []
t0 = time.clock()
for i in range(1,20000):
    a.append(i)
print(time.clock() - t0,"seconds process time")

t0 = time.clock()
b = [i for i in range(1,20000)]
print(time.clock() - t0,"Seconds process time")

print('################################################################################')
#列表推导式
print("列表推导式")
a = [i**2 for i in range(1,10)]
print(a)

c = [j+1 for j in range(1,10)]
print(c)

k = [n for n in range(1,10) if n % 2 ==0]
print(k)

z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
print(z)
#字典推导式
print("字典推导式")
d = {i:i+1 for i in range(4)}
print(d)

g = {i:j for i,j in zip(range(1,6),'abcde')}
print(g)

g1 = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(g1)

#循环列表时获取元素的索引
print('\n')
print('循环列表时获取元素的索引')
letters = ['a','b','c','d','e','f','g']
for num,letter in enumerate(letters):       #enumerate函数用于循环时获取元素的索引
    print(letter,'is',num+1)

#split函数用来将字符串中的每个单词分开
print('\n')
print('split函数用来将字符串中的每个单词分开')
lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()
print(words)

print('\n')
print('上网搜索词频统计')
