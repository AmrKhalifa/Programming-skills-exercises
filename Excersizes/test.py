import numpy as np 



arr = np.array([[1,2,4], [2,4,6], [4,6,8]])

u, _ = np.linalg.eigh(arr)
u = list(reversed(u))

print(u)


print(arr.shape[0])
print(np.eye(arr.shape[0]))