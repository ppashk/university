arr1 = [1, 2, 3]
arr2 = ['H', 'e', 'l', 'l', 'o', '!']
print(arr1[2])
arr2[len(arr2) - 1] = 'user'
print(arr2)
sum_arr = arr1 + arr2
print(sum_arr)
concat_arr = sum_arr[1:8]
print(concat_arr)
concat_arr += ['user', '!']
print(concat_arr)