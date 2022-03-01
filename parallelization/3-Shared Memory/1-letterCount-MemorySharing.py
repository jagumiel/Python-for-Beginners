# Parallel version of letterCount.
# Careful. This code is wrong for learning purposes. It is fast, but it does not counts well.
# This is because threads are updating the global array without taking in count the work of the other threads. 

import json
from threading import Thread
import urllib.request
import time

finished_count=0    #Global Variable.

def count_letters(url, frequency):
    response=urllib.request.urlopen(url)
    txt = str(response.read())
    for l in txt:
        letter=l.lower()
        if letter in frequency:
            frequency[letter]+=1
    global finished_count
    finished_count+=1

def main():
    frequency={}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c]=0
    start=time.time()
    for i in range(1000, 1020):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)).start()
    while (finished_count<20):
        time.sleep(0.5)
    end=time.time()
    print(json.dumps(frequency, indent=4))
    print("Elapsed time", end-start)

main()