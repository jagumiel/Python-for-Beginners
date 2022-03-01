# Parallel version of letterCount.
# This code has been corrected.


import json
from threading import Thread, Lock
import urllib.request
import time

from numpy import True_

finished_count=0    #Global Variable.

def count_letters(url, frequency, mutex):
    response=urllib.request.urlopen(url)
    txt = str(response.read())
    mutex.acquire()
    for l in txt:
        letter=l.lower()
        if letter in frequency:
            frequency[letter]+=1
    global finished_count
    finished_count+=1
    mutex.release()

def main():
    frequency={}
    mutex=Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c]=0
    start=time.time()
    for i in range(1000, 1020):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()
    while True:
        mutex.acquire()
        if (finished_count==20):
            break
        mutex.release()
        time.sleep(0.5)
    end=time.time()
    print(json.dumps(frequency, indent=4))
    print("Elapsed time", end-start)

main()