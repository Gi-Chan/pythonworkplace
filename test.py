import numpy as np

test = [[[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,0],[0,0,0],[0,0,0]]]

# test2에서 1인 부분만 test의 값으로 대체
test2 = [[[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,0],[0,1,0],[1,0,0]],
        [[0,0,0],[0,0,0],[1,1,1]]]
a = np.array(test)
b = np.array(test2)

# a[a==(0,0,0)]=b[a==(0,0,0)]

# print(b.shape)
# print(a)
mask_t = np.where(np.logical_and(a==(0,0,0), b !=(0,0,0)))
print(mask_t)
b[mask_t[:2]]= 10
print(b)