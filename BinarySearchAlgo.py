def BinarySearch(array, target):

    sorted_arr = sorted(array)

    L = 0
    R = len(sorted_arr) - 1

    while L<=R:
        
        M = (L + R)//2

        if sorted_arr[M] == target:
            return True
        
        elif sorted_arr[M] < target:
            L = M + 1
        
        else:
            R = M - 1

    return False


