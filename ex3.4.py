import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            self.lock()
            if (self.tail + 1) % self.size == self.head:
                self.unlock()
                print("queue is full")
                time.sleep(1)
            else:
                if self.head == -1:
                    self.head = 0
                    self.tail = 0
                    self.queue[self.tail] = data
                else:
                    self.tail = (self.tail + 1) % self.size
                    self.queue[self.tail] = data
                    self.unlock()
                    return

    
    def dequeue(self):
        while True:
            self.lock()
            if self.head == -1:
                self.unlock()
                print("queue is empty")
                time.sleep(1)
            else:
                if self.head == self.tail:
                    temp = self.queue[self.head]
                    self.head = -1
                    self.tail = -1
                    self.unlock()
                    return temp
                else:
                    temp = self.queue[self.head]
                    self.head = (self.head + 1) % self.size
                    self.unlock()
                    return temp

def producer():
    while True:
        data = random.randint(1, 10)
        time.sleep(data)
        q.enqueue(data)
        print('Produced', data)

def consumer():
    while True:
        data = random.randint(1, 10)
        time.sleep(data)
        item = q.dequeue()
        print('Consumed', item)

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()