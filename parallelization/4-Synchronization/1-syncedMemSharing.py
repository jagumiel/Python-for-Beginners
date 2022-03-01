# Parallel synced memory sharing example.
# We use a lock to prevent the other thread to get a non-updated value.
# After the value has been updated, we release the lock, so the other thread can work too.

import time
from threading import Thread, Lock

class StingySpendy:
    money=100
    mutex=Lock()

    def stingy(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money+=10
            self.mutex.release()
        print("Spendy Done")
    

    def spendy(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money-=10
            self.mutex.release()
        print("Spendy Done")

ss=StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print("Money in the end", ss.money)