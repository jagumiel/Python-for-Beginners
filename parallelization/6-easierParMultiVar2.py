# The same as 5. But in this code, with map function, we can print the results in the order they were called, and not in the order they were finished.
import concurrent.futures
import time

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done in {seconds} seconds... Hello World!'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs) # map() will run do_something function with every value from the secs array.
    
    for result in results:
        print(result)

finish=time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')