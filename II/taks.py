import threading
import time
import random

class QualityControl1:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
          self.total_items += value

    def diproses(self):
        with self.lock:
            self.execute(1)

class QualityControl2:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
          self.total_items += value

    def dipilah(self):
        with self.lock:
            self.execute(-1)

def pemroses(qualitycontrol, items):
    print("N° {} qualitycontrol1 memproses \n".format(items))
    while items:
        qualitycontrol.diproses()
        time.sleep(1)
        items -= 1
        print("Proses daging ayam sesuai produk rendah lemak {} proses daging ayam selesai \n".format(items))

def Pemilah(qualitycontrol, items):
    print("N° {} qualitycontrol2 memilah \n".format(items))
    while items:
        qualitycontrol.dipilah()
        time.sleep(1)
        items -= 1
        print("Pilah daging ayam ke mesin berbeda {} pemilahan daging selesai \n".format(items))

def main():
    items = 10
    box1 = QualityControl1()
    box2 = QualityControl2()

    t1 = threading.Thread(target=pemroses, \
                          args=(box1, random.randint(10,20)))
    t2 = threading.Thread(target=Pemilah, \
                          args=(box2, random.randint(1,10)))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

class QualityControl3:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
          self.total_items += value

    def diproses(self):
        with self.lock:
            self.execute(1)

class QualityControl4:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
          self.total_items += value

    def dipilah(self):
        with self.lock:
            self.execute(-1)

def pemroses(qualitycontrol, items):
    print("N° {} qualitycontrol1 memproses \n".format(items))
    while items:
        qualitycontrol.diproses()
        time.sleep(1)
        items -= 1
        print("Proses daging ayam sesuai produk rendah lemak {} proses daging ayam selesai \n".format(items))

def Pemilah(qualitycontrol, items):
    print("N° {} qualitycontrol2 memilah \n".format(items))
    while items:
        qualitycontrol.dipilah()
        time.sleep(1)
        items -= 1
        print("Pilah daging ayam ke mesin berbeda {} pemilahan daging selesai \n".format(items))

def main_2():
    items = 10
    box3 = QualityControl3()
    box4 = QualityControl4()

    t1 = threading.Thread(target=pemroses, \
                          args=(box3, random.randint(10,20)))
    t2 = threading.Thread(target=Pemilah, \
                          args=(box4, random.randint(1,10)))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main_2()

