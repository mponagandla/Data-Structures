arr = [4, 3, 8, 9, 0, 1]
arr1 = [9, 8, 6, 4, 3, 1]
arr2 = [1, 2, 3, 4, 10, 6, 9, 8, 7, 5]
k = 3

def sliding_window(k, rem_array):
    result = []
    if len(rem_array) <= k:
        result = [max(rem_array)]
    else:
        result += [max(rem_array[:3])] + sliding_window(k, rem_array[1:])

    return result


res = sliding_window(k, arr2)
print(res)