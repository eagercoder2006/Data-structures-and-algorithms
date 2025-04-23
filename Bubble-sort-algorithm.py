#Bubble sort algorithm

A = [-5,3,2,1,-3,-3,7,2,2]

def bubble_sort(arr):

    flag = True

    while flag==True:
        flag = False
        i = 1
        while i < len(A): 
            if arr[i] < arr[i-1]:
                flag = True
                switch1 = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = switch1
            i = i+1
    
    return(arr)

print(bubble_sort(A))