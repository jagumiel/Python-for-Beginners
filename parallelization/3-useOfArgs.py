import multiprocessing
import time

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done... Hello World!')

processes = []

for _ in range(10):
    p=multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

#print(f'Parallelization started. As I want to know the execution time, I need a join(). The code wont continue after the join until the processes have been ended.')


finish=time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')