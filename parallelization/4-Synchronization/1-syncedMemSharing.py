# Parallel version of letterCount.
# Careful. This code is wrong for learning purposes. It is fast, but it does not counts well.
# This is because threads are updating the global array without taking in count the work of the other threads. 

import time
from threading import Thread

class StingySpendy:
    money=100

    def stingy(self):
        for i in range(1000000):
            self.money+=10
        print("Spendy Done")
    

    def spendy(self):
        for i in range(1000000):
            self.money-=10
        print("Spendy Done")

ss=StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print("Money in the end", ss.money)