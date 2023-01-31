from threading import Thread
from queue import Queue
import time
import random

class Producer(Thread):
  
  def __init__(self, queue):
    Thread.__init__(self)
    self.queue = queue

  def run(self):
    for i in range(5):
      item = random.randint(0, 256)
      self.queue.put(item)
      print('Producer notify : item N°%d appended to queue by %s\n'\
            % (item, self.name))
time.sleep(1)

class Consumer(Thread):
    def __init__(self, queue):
      Thread.__init__(self)
      self.queue = queue
    
    def run(self):
      while True:
        item = self.queue.get()
        print('Consumer notify : %d popped from queue by %s'\
              % (item, self.name))
        self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()

    producers = []
    for i in range(25):
        producers.append(Producer(queue))
        
    consumers = []
    for i in range(25):
        consumers.append(Consumer(queue))
    
    for t in producers:
        t.start()
    for t in consumers:
        t.start()

    for t in producers:
        t.join()
    for t in consumers:
        t.join()
