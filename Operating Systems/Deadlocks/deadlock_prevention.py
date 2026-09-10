import threading
import time

resource_A = threading.Lock()
resource_B = threading.Lock()


def process_1():
    print("\nP1: Requesting Resource A")
    resource_A.acquire()
    print("P1: Acquired Resource A")

    time.sleep(1)

    print("P1: Requesting Resource B")
    resource_B.acquire()
    print("P1: Acquired Resource B")

    print("P1: Using both resources...")
    time.sleep(1)

    resource_B.release()
    resource_A.release()

    print("P1: Released A and B")
    print("P1: Finished")


def process_2():
    print("\nP2: Requesting Resource A")
    resource_A.acquire()
    print("P2: Acquired Resource A")

    time.sleep(1)

    print("P2: Requesting Resource B")
    resource_B.acquire()
    print("P2: Acquired Resource B")

    print("P2: Using both resources...")
    time.sleep(1)

    resource_B.release()
    resource_A.release()

    print("P2: Released A and B")
    print("P2: Finished")


p1 = threading.Thread(target=process_1)
p2 = threading.Thread(target=process_2)

p1.start()
p2.start()

p1.join()
p2.join()

print("\nProgram Finished Successfully!")