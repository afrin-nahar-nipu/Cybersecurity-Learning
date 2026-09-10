# ==========================================
#       DEADLOCK DETECTION ALGORITHM
# ==========================================

print("==========================================")
print("      DEADLOCK DETECTION ALGORITHM")
print("==========================================")


# ------------------------------------------
# Available Resources
# ------------------------------------------

available = [0, 0, 0]


# ------------------------------------------
# Allocation Matrix
# ------------------------------------------
# Current resources held by each process

allocation = [
    [0, 1, 0],   # P0
    [2, 0, 0],   # P1
    [3, 0, 3],   # P2
    [2, 1, 1],   # P3
]


# ------------------------------------------
# Request Matrix
# ------------------------------------------
# Resources each process is waiting for

request = [
    [0, 0, 0],   # P0
    [2, 0, 2],   # P1
    [0, 0, 0],   # P2
    [1, 0, 0],   # P3
]


# ------------------------------------------
# Number of Processes and Resources
# ------------------------------------------

processes = len(allocation)
resources = len(available)


# ------------------------------------------
# Display Input
# ------------------------------------------

print("\nAvailable Resources:")
print(available)


print("\nAllocation Matrix:")

for i in range(processes):
    print(f"P{i}: {allocation[i]}")


print("\nRequest Matrix:")

for i in range(processes):
    print(f"P{i}: {request[i]}")


# ------------------------------------------
# Deadlock Detection Algorithm
# ------------------------------------------

work = available.copy()

finish = [False] * processes


print("\n==========================================")
print("        DETECTION PROCESS")
print("==========================================")


# Step 1:
# If Allocation[i] is all zeros,
# the process is considered finished

for i in range(processes):

    if allocation[i] == [0] * resources:
        finish[i] = True


# Step 2:
# Continue checking processes

while True:

    found = False

    for i in range(processes):

        # Skip already finished process
        if finish[i]:
            continue


        # Check Request[i] <= Work
        possible = True

        for j in range(resources):

            if request[i][j] > work[j]:

                possible = False
                break


        # If process can finish
        if possible:

            print(f"\nP{i} can complete")

            print(f"Work Before: {work}")


            # Release allocated resources

            for j in range(resources):

                work[j] += allocation[i][j]


            print(f"Work After : {work}")


            finish[i] = True

            print(f"P{i} Finished")

            found = True


    # If no process can continue
    if not found:
        break


# ------------------------------------------
# Find Deadlocked Processes
# ------------------------------------------

deadlocked = []


for i in range(processes):

    if not finish[i]:

        deadlocked.append(f"P{i}")


# ------------------------------------------
# Final Result
# ------------------------------------------

print("\n==========================================")
print("              RESULT")
print("==========================================")


if len(deadlocked) == 0:

    print("\n✅ No Deadlock Detected")

else:

    print("\n❌ DEADLOCK DETECTED!")

    print("\nDeadlocked Processes:")

    print(" -> ".join(deadlocked))


print("\nFinal Work:")
print(work)


print("\nProcess Status:")

for i in range(processes):

    if finish[i]:
        print(f"P{i}: Finished")

    else:
        print(f"P{i}: DEADLOCKED")