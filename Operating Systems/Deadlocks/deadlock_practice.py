import threading
import time

resource_A = threading.Lock()
resource_B = threading.Lock()


def process_1():
    print("Process 1: Trying to acquire Resource A")
    resource_A.acquire()
    print("Process 1: Acquired Resource A")

    time.sleep(1)

    print("Process 1: Trying to acquire Resource B")
    resource_B.acquire()
    print("Process 1: Acquired Resource B")

    resource_B.release()
    resource_A.release()


def process_2():
    print("Process 2: Trying to acquire Resource B")
    resource_B.acquire()
    print("Process 2: Acquired Resource B")

    time.sleep(1)

    print("Process 2: Trying to acquire Resource A")
    resource_A.acquire()
    print("Process 2: Acquired Resource A")

    resource_A.release()
    resource_B.release()


p1 = threading.Thread(target=process_1)
p2 = threading.Thread(target=process_2)

p1.start()
p2.start()

p1.join()
p2.join()

print("Program finished")