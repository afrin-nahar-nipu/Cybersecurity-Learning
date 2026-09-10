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
    print("P1: Waiting for B (maximum 2 seconds)...")

    if resource_B.acquire(timeout=2):
        print("P1: Acquired Resource B")

        resource_B.release()
        resource_A.release()

        print("P1: Released A and B")
        print("P1: Finished")

    else:
        print("P1: Could not acquire B")
        print("P1: Releasing Resource A")

        resource_A.release()

        print("P1: Aborted safely")


def process_2():
    print("\nP2: Requesting Resource B")

    resource_B.acquire()
    print("P2: Acquired Resource B")

    time.sleep(1)

    print("P2: Requesting Resource A")
    print("P2: Waiting for A (maximum 2 seconds)...")

    if resource_A.acquire(timeout=2):
        print("P2: Acquired Resource A")

        resource_A.release()
        resource_B.release()

        print("P2: Released A and B")
        print("P2: Finished")

    else:
        print("P2: Could not acquire A")
        print("P2: Releasing Resource B")

        resource_B.release()

        print("P2: Aborted safely")


p1 = threading.Thread(target=process_1)
p2 = threading.Thread(target=process_2)

p1.start()
p2.start()

p1.join()
p2.join()

print("\nProgram Finished!")