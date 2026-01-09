from typing import List

arr = list([5, 2, 10, 1, 4])
print(arr)
arr_sorted = sorted(enumerate(arr), key=lambda x: x[0])
print(arr_sorted)
