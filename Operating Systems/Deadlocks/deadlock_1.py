import threading
import time

# Two resources
resource_A = threading.Lock()
resource_B = threading.Lock()


def process_1():
    print("P1: Trying to acquire Resource A")
    resource_A.acquire()

    print("P1: Acquired Resource A")

    time.sleep(1)

    print("P1: Trying to acquire Resource B")
    resource_B.acquire()

    print("P1: Acquired Resource B")

    resource_B.release()
    resource_A.release()


def process_2():
    print("P2: Trying to acquire Resource B")
    resource_B.acquire()

    print("P2: Acquired Resource B")

    time.sleep(1)

    print("P2: Trying to acquire Resource A")
    resource_A.acquire()

    print("P2: Acquired Resource A")

    resource_A.release()
    resource_B.release()


# Create two processes/threads
p1 = threading.Thread(target=process_1)
p2 = threading.Thread(target=process_2)

# Start them
p1.start()
p2.start()

# Wait for both
p1.join()
p2.join()

print("Program finished")