arr = [1, 2, 3, 4, 10, 6, 9, 8, 7, 5]

def recursive_linear_search(item,arr):
    if len(arr) >= 1:
        if item == arr[0]:
            print("Found")
        else:
            recursive_linear_search(item, arr[1:])


recursive_linear_search(1, arr)