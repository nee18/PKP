import multiprocessing

def square(n):
    return n ** 2

if __name__ == '__main__':
    inputs = list(range(0,329))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(square, inputs)
    pool.close()
    pool.join()
    print ('Pool :', pool_outputs)
