import numpy as np


test_array_1 = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]], [[1, 2], [3, 4]]])
test_array_2 = np.array([[5, 6], [7, 8]])
a = np.array([[1, 2, 3], [4, 5, 6]])

# print(test_array_1)
# print(test_array_1.dtype)
# print(test_array_1.shape)
# print(test_array_2.shape)
# print(test_array_1.ndim)

print(a.shape)
print(a)
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
a.reshape(3, 2)
print(a.shape)
print(a)

print()
print(a[0:])
print(a[0: 1])
print(a[1:])

print()
print(a[1:].reshape((3, 1)))