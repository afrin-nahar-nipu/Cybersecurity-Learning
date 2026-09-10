import threading
import time

resource_A = threading.Lock()
resource_B = threading.Lock()


def process_1():
    print("\n[P1] Starting...")

    print("[P1] Requesting Resource A")
    resource_A.acquire()
    print("[P1] Resource A acquired")

    time.sleep(2)

    print("[P1] Requesting Resource B")
    print("[P1] Waiting for Resource B...")

    resource_B.acquire()

    print("[P1] Resource B acquired")

    resource_B.release()
    resource_A.release()

    print("[P1] Finished")


def process_2():
    print("\n[P2] Starting...")

    print("[P2] Requesting Resource B")
    resource_B.acquire()
    print("[P2] Resource B acquired")

    time.sleep(2)

    print("[P2] Requesting Resource A")
    print("[P2] Waiting for Resource A...")

    resource_A.acquire()

    print("[P2] Resource A acquired")

    resource_A.release()
    resource_B.release()

    print("[P2] Finished")


p1 = threading.Thread(target=process_1)
p2 = threading.Thread(target=process_2)

p1.start()
p2.start()

p1.join()
p2.join()

print("\nProgram Finished")