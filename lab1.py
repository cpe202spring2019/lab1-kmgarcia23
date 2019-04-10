def max_list_iter(int_list):
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    max = int_list[0]
    index = 0
    for i in range(0, len(int_list)):
        cur = int_list[i]
        if cur > max:
            max = cur
            index = i
    return index

def reverse_rec(int_list):
    if int_list == None:
        raise ValueError
    if len(int_list) == 1:
        return [int_list[0]]
    else:
        length = len(int_list)
        return [int_list[length -1]] + (reverse_rec(int_list[:length-1]))

def bin_search(target, low, high, int_list):
    mid = (low + high) // 2
    if int_list == None:
        raise ValueError
    if low > high:
        return None
    if int_list[mid] == target:
        return mid
    else:
        if int_list[mid] > target:
            return bin_search(target, low, mid - 1, int_list)
        elif int_list[mid] < target:
            return bin_search(target, mid + 1, high, int_list)