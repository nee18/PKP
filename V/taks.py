import asyncio
import time
import random

max_threads = 30
active_threads = 0

def Memproses_Komputasi_A(end_time, loop):
    global active_threads
    active_threads += 1
    print("Komputasi_A Dipanggil ")
    time.sleep(random.randint(0, 1))
    active_threads -= 1
    if (loop.time() + 1.0) < end_time:
        if active_threads < max_threads:
            loop.call_later(1, Memproses_Komputasi_B, end_time, loop)
        else:
            loop.call_soon(Memproses_Komputasi_B, end_time, loop)
    else:
        loop.stop()

def Memproses_Komputasi_B(end_time, loop):
    global active_threads
    active_threads += 1
    print("Komputasi_B Dipanggil ")
    time.sleep(random.randint(0, 1))
    active_threads -= 1
    if (loop.time() + 1.0) < end_time:
        if active_threads < max_threads:
            loop.call_later(1, Memproses_Komputasi_C, end_time, loop)
        else:
            loop.call_soon(Memproses_Komputasi_C, end_time, loop)
    else:
        loop.stop()

def Memproses_Komputasi_C(end_time, loop):
    global active_threads
    active_threads += 1
    print("Komputasi_C Dipanggil")
    time.sleep(random.randint(0, 1))
    active_threads -= 1
    if (loop.time() + 1.0) < end_time:
        if active_threads < max_threads:
            loop.call_later(1, Memproses_Komputasi_A, end_time, loop)
        else:
            loop.call_soon(Memproses_Komputasi_A, end_time, loop)
    else:
        loop.stop()

loop = asyncio.get_event_loop()
end_loop = loop.time() + 60
loop.call_soon(Memproses_Komputasi_A, end_loop, loop)
loop.run_forever()
loop.close()

