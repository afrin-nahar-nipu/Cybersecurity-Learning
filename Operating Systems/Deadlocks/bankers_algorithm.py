# ==========================================
#       BANKER'S ALGORITHM
# ==========================================


print("==========================================")
print("          BANKER'S ALGORITHM")
print("==========================================")


# ------------------------------------------
# Allocation Matrix
# ------------------------------------------

allocation = [
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1]
]


# ------------------------------------------
# Maximum Matrix
# ------------------------------------------

maximum = [
    [3, 2, 2],
    [2, 2, 2],
    [3, 1, 2]
]


# ------------------------------------------
# Available Resources
# ------------------------------------------

available = [3, 3, 2]


# ------------------------------------------
# Number of Processes and Resources
# ------------------------------------------

processes = len(allocation)
resources = len(available)


# ------------------------------------------
# Calculate Need Matrix
# Need = Maximum - Allocation
# ------------------------------------------

need = []

for i in range(processes):

    row = []

    for j in range(resources):

        value = maximum[i][j] - allocation[i][j]

        row.append(value)

    need.append(row)


# ------------------------------------------
# Display Matrices
# ------------------------------------------

print("\nAllocation Matrix:")

for i in range(processes):

    print(f"P{i}: {allocation[i]}")


print("\nMaximum Matrix:")

for i in range(processes):

    print(f"P{i}: {maximum[i]}")


print("\nNeed Matrix:")

for i in range(processes):

    print(f"P{i}: {need[i]}")


print("\nAvailable Resources:")
print(available)


# ------------------------------------------
# Banker's Algorithm
# ------------------------------------------

work = available.copy()

finish = [False] * processes

safe_sequence = []


print("\n==========================================")
print("        SAFETY ALGORITHM")
print("==========================================")


while len(safe_sequence) < processes:

    found = False

    for i in range(processes):

        # Check if process has already finished
        if finish[i]:
            continue


        # Check Need[i] <= Work
        possible = True

        for j in range(resources):

            if need[i][j] > work[j]:

                possible = False

                break


        # If process can execute
        if possible:

            print(f"\nP{i} can execute")

            print(f"Need  : {need[i]}")
            print(f"Work before: {work}")


            # After process finishes,
            # it releases its allocated resources

            for j in range(resources):

                work[j] = work[j] + allocation[i][j]


            finish[i] = True

            safe_sequence.append(i)

            found = True


            print(f"Work after : {work}")
            print(f"P{i} finished")


    # No process can execute
    if not found:

        break


# ------------------------------------------
# Check Final Result
# ------------------------------------------

print("\n==========================================")
print("              RESULT")
print("==========================================")


if len(safe_sequence) == processes:

    print("\n✅ System is in SAFE STATE")

    print("\nSafe Sequence:")

    for index, process in enumerate(safe_sequence):

        if index != len(safe_sequence) - 1:

            print(f"P{process} -> ", end="")

        else:

            print(f"P{process}")


else:

    print("\n❌ System is in UNSAFE STATE")

    print("No Safe Sequence Found")


# ------------------------------------------
# Final Work
# ------------------------------------------

print("\nFinal Work:")
print(work)