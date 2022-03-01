import os
from os.path import isdir, join
from threading import Thread, Lock, Condition

mutex=Lock()
matches=[]

class WaitGroup:
    wait_count=0
    cv=Condition()

    def add(self, count):
        self.cv.acquire()
        self.wait_count+=count
        self.cv.release()
    
    def done(self):
        self.cv.acquire()
        if (self.wait_count>0):
            self.wait_count-=1
        if (self.wait_count==0):
            self.cv.notify_all()
        self.cv.release()

    def wait(self):
        self.cv.acquire()
        while (self.wait_count>0):
            self.cv.wait()
        self.cv.release()

def file_search(root, filename, wait_group):
    print("Searching in:", root)
    for file in os.listdir(root):
        full_path=join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            wait_group.add(1)
            t=Thread(target=file_search, args=([full_path, filename, wait_group]))
            t.start()
    wait_group.done()
    


def main():
    wait_group=WaitGroup()
    wait_group.add(1)
    t=Thread(target=file_search, args=(["/home/oem/", "cat.jpg", wait_group]))
    t.start()
    wait_group.wait()
    for m in matches:
        print("Matched:", m)

main()