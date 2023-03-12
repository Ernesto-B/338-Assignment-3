import random
import time

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




startTest = time.perf_counter()

for i in range(1000):
    test = testArray
    startSearch = time.perf_counter()
    linear_search(test, random(0, 10000))
    endSearch = time.perf_counter()

    searchTimes.append(endSearch-startSearch)

endTest = time.perf_counter()


print(str(testArray()))