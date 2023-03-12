import random
import time
import matplotlib.pyplot as plt

searchTimes = []

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def testArray():
    n = 1000
    arr = sorted(random.sample(range(n*10), n))
    return arr

def totalTime (inputTime):
    # combinding the times
    totalTime = []
    index = 0
    for i in inputTime:
        timeStamp = 0
        for x in range(index):
            timeStamp += inputTime[x]
        totalTime.append(timeStamp)
        index += 1
    
    return totalTime

startTest = time.perf_counter()

for i in range(1000):
    test = testArray()
    startSearch = time.perf_counter()
    linear_search(test, random.randint(0, 10000))
    endSearch = time.perf_counter()

    searchTimes.append(endSearch-startSearch)

endTest = time.perf_counter()

timeStamps = totalTime(searchTimes)

plt.scatter(timeStamps, searchTimes)
plt.xlabel('Time Elapsed')
plt.ylabel('Search Time')
plt.title('Time it took to search for input')
plt.show()