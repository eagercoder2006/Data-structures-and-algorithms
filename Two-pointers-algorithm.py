#Reversing an array with Two Pointers algorithm

A = [100,16,9,1,0]

def reverse_array(arr):

    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer <= right_pointer:
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
        left_pointer+=1
        right_pointer-=1

    return arr



