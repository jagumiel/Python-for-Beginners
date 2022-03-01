# Parallel synced memory sharing example.
# We use a lock to prevent the other thread to get a non-updated value.
# After the value has been updated, we release the lock, so the other thread can work too.

import time
from threading import Thread, Condition

class StingySpendy:
    money=100
    cv=Condition()

    def stingy(self):
        for i in range(1000000):
            self.cv.acquire()
            self.money+=10
            self.cv.notify() #Variable changed. Warns that condition may have changed too.
            self.cv.release()
        print("Spendy Done")
    

    def spendy(self):
        for i in range(500000):
            self.cv.acquire()
            while (self.money<20):
                self.cv.wait()
            self.money-=20
            if (self.money<0):
                print("Money in bank: ", self.money)
            self.cv.release()
        print("Spendy Done")

ss=StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print("Money in the end", ss.money)