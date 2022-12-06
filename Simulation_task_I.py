import threading
import time
import os
from threading import Thread
from random import randint

#sycronus
# Lock Definition
threadLock = threading.Lock()

class MyThreadClass (Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    def run(self):
        #Acquire the Lock
        threadLock.acquire()
        print ("---> " + self.name + \
            " running, belonging to process ID "\
            + str(os.getpid()) + "\n")
        time.sleep(self.duration)
        print ("---> " + self.name + " over\n")
        #Release the Lock
        #setiap proses 1-9 proses dulu yang 1 baru berhenti ke proses ke 2, set time lebih lama
        threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ", randint(1,10))
    thread2 = MyThreadClass("Thread#2 ", randint(1,10))
    thread3 = MyThreadClass("Thread#3 ", randint(1,10))
    thread4 = MyThreadClass("Thread#4 ", randint(1,10))
    thread5 = MyThreadClass("Thread#5 ", randint(1,10))
    thread6 = MyThreadClass("Thread#6 ", randint(1,10))
    thread7 = MyThreadClass("Thread#7 ", randint(1,10))
    thread8 = MyThreadClass("Thread#8 ", randint(1,10))
    thread9 = MyThreadClass("Thread#9 ", randint(1,10))
    thread10 = MyThreadClass("Thread#10 ", randint(1,10))
    thread11 = MyThreadClass("Thread#11 ", randint(1,10))
    thread12 = MyThreadClass("Thread#12 ", randint(1,10))
    thread13 = MyThreadClass("Thread#13 ", randint(1,10))
    thread14 = MyThreadClass("Thread#14 ", randint(1,10))
    thread15 = MyThreadClass("Thread#15 ", randint(1,10))
    thread16 = MyThreadClass("Thread#16 ", randint(1,10))
    thread17 = MyThreadClass("Thread#17 ", randint(1,10))
    thread18 = MyThreadClass("Thread#18 ", randint(1,10))
    thread19 = MyThreadClass("Thread#19 ", randint(1,10))
    thread20 = MyThreadClass("Thread#20 ", randint(1,10))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()
    thread17.start()
    thread18.start()
    thread19.start()
    thread20.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()
    thread12.join()
    thread13.join()
    thread14.join()
    thread15.join()
    thread16.join()
    thread17.join()
    thread18.join()
    thread19.join()
    thread20.join()

    # End
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    main()