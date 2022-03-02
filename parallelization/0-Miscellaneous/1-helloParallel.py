import multiprocessing
import time

start=time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done... Hello World!')
    
p1=multiprocessing.Process(target=do_something)
p2=multiprocessing.Process(target=do_something)

p1.start()
p2.start()
print(f'Parallelization started. As I want to know the execution time, I need a join(). The code wont continue after the join until the processes have been ended.')

p1.join()
p2.join()

finish=time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')