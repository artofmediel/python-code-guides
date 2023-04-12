# --------------------------
# Python multiprocessing
# --------------------------

# multiprocessing - running task in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing - better for cpu bound tasks (heavy cpu usage)
#                   multithreading - better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    #check how many cpu cores you have
    #print(cpu_count())

    a = Process(target=counter,args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("Finished in : ", time.perf_counter(), " seconds")
    # speed will depend on how many cpu cores you currently have

if __name__ == '__main__':
    main()