import random
import time
import matplotlib.pyplot as plt

searchTimes = []

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def testArray():
    n = 1000
    arr = sorted(random.sample(range(n*10), n))
    return arr

def totalTime (inputTime):
    # combinding the times
    totalTime = []
    index = 0
    for i in searchTimes:
        timeStamp = 0
        for x in range(index):
            timeStamp += inputTime[x]
        totalTime.append(timeStamp)
        index += 1
    
    return totalTime

for i in range(1000):
    test = testArray()
    startSearch = time.perf_counter()
    binary_search(test, random.randint(0, 10000))
    endSearch = time.perf_counter()

    searchTimes.append(endSearch-startSearch)

timeStamps = totalTime(searchTimes)

plt.scatter(timeStamps, searchTimes)
plt.xlabel('Time Elapsed')
plt.ylabel('Search Time')
plt.title('Time it took to search for input')
plt.show()