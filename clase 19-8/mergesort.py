from threading import *
from time import *

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]


    sleft = []
    sright = []

   
    def sort_left():
        nonlocal sleft
        print("Sorting right part:", left)
        sleft = merge_sort(left)
        print("Sorted right part:", sright)
        sleep(1)


    def sort_right():
        nonlocal sright
        print("Sorting right part:", right)
        sright = merge_sort(right)
        print("Sorted right part:", sright)
        sleep(1)

    
    p = Thread(target=sort_left)
    q = Thread(target=sort_right)

    
    p.start()
    q.start()

    p.join()
    q.join()

    return merge(sleft, sright)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

lst = [38, 27, 43, 3, 9, 82, 10, 100, 140, 12, 5]
sorted_lst = merge_sort(lst)
print("Sorted list:", sorted_lst)