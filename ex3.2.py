import json
import time
import matplotlib.pyplot as plt

searchTime = []

# load the array
with open('ex3.2-array.json', 'r') as f:
    data = json.load(f)

# load the list of search tasks
with open('ex3.2-search-tasks.py', 'r') as f:
    tasks = json.load(f)

# binary search where the midpoint for the first iteration is configurable
def binary_search(array: list, search: int, start: int, end: int) -> bool:
    #starting timer
    start_timer = time.perf_counter()

    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == search:
        #ending timer and calculating the time taken
        end_timer = time.perf_counter()
        searchTime.append(end_timer-start_timer)

        return True
    elif array[mid] < search:
        #ending timer and calculating the time taken
        end_timer = time.perf_counter()
        searchTime.append(end_timer-start_timer)

        return binary_search(array, search, mid + 1, end)
    else:
        #ending timer and calculating the time taken
        end_timer = time.perf_counter()
        searchTime.append(end_timer-start_timer)
        
        return binary_search(array, search, start, mid - 1)
    
print(binary_search(data, int(input("What number to search for? ")), 0, len(data) - 1))

# combinding the times
totalTime = []
index = 0
for i in searchTime:
    timeStamp = 0
    for x in range(index):
        timeStamp += searchTime[x]
    totalTime.append(timeStamp)
    index += 1

plt.scatter(totalTime, searchTime)
plt.xlabel('Time Elapsed')
plt.ylabel('Search Time')
plt.title('Time it took to search for input')
plt.show()
