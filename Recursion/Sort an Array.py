array = [3,2,7,6,4,5,9]


def recursive_sort(array):
    if len(array) == 1:
        return array
    last_ele = array.pop()
    recursive_sort(array)
    insert(last_ele, array)
    return array

def insert(temp, array):
    length = len(array)
    if length == 0 or array[length-1] <= temp:
        return array.append(temp)
    last_ele = array.pop()
    insert(temp,array)
    array.append(last_ele)
    return array

result = recursive_sort(array)

print(result)