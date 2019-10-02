import numpy as np

a=np.arange(1,13).reshape((3,4))

print(a)

sub_a=a[:2,:2]
print(sub_a)

sub_a[0][0]=100
print(sub_a)
print(a)
#深拷贝会影响到原数组
sub_aa=np.copy(a[:2,:2])
print(sub_aa)
print(a)