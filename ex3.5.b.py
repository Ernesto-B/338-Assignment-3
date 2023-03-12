import random
import time

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

def experiment():
    n = 1000
    arr = sorted(random.sample(range(n*10), n))
    target = random.randint(0, n*10-1)
    linear_times = []
    binary_times = []
    num_trials = 100