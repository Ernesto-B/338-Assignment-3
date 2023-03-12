import json

# load the array
with open('ex3.2-array.json', 'r') as f:
    data = json.load(f)

# load the list of search tasks
with open('ex3.2-search-tasks.py', 'r') as f:
    tasks = json.load(f)

# binary search where the midpoint for the first iteration is configurable
def binary_search(array: list, search: int, start: int, end: int) -> bool:
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == search:
        return True
    elif array[mid] < search:
        return binary_search(array, search, mid + 1, end)
    else:
        return binary_search(array, search, start, mid - 1)
    
print(binary_search(data, int(input("What number to search for? ")), 0, len(data) - 1))