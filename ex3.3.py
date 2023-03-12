import sys

# loop that grows a list from 0 to 63 integers, printing out a message when the capacity of the list changes
def grow_list():
    lst = []
    cap = sys.getsizeof(lst)
    i = 0
    for i in range(63):
        lst.append(i)
        if sys.getsizeof(lst) != cap:
            cap = sys.getsizeof(lst)
            print(f"Capacity changed to {cap} bytes ({cap/4} entries)\n")
        
grow_list()