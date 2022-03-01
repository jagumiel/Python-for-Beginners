# This code just shows how a barrier works.
# Red thread waits in the barrier until thread Blue finishes. Then they continue running again.

from threading import Barrier
from threading import Thread
import time


barrier=Barrier(2)

def wait_on_barrier(name, time_to_sleep):
    for i in range(10):
        print(name,"running")
        time.sleep(time_to_sleep)
        print(name, "is waiting on barrier")
        barrier.wait()
    print(name, "is finished.")

red= Thread(target=wait_on_barrier, args=["red", 4])
blue= Thread(target=wait_on_barrier, args=["blue", 10])

red.start()
blue.start()

# Optional: I can decide when to abort a barrier.
time.sleep(25)
print("After 25 seconds of execution, I am aborting...")
barrier.abort()