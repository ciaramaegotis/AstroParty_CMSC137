from threading import Thread
import time
def someFunc():
    print("someFunc was called")
    time.sleep(10)
 
thread = Thread(target=someFunc, args=[])

thread.start()
thread.join()