# ==========================================
#       BANKER'S ALGORITHM - UNSAFE
# ==========================================


print("==========================================")
print("       BANKER'S ALGORITHM")
print("          UNSAFE TEST")
print("==========================================")


allocation = [
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1]
]


maximum = [
    [3, 2, 2],
    [2, 2, 2],
    [3, 1, 2]
]


# Intentionally small available resources
available = [0, 0, 0]


processes = len(allocation)
resources = len(available)


# ------------------------------------------
# Calculate Need
# ------------------------------------------

need = []

for i in range(processes):

    row = []

    for j in range(resources):

        row.append(maximum[i][j] - allocation[i][j])

    need.append(row)


print("\nNeed Matrix:")

for i in range(processes):

    print(f"P{i}: {need[i]}")


print("\nAvailable:")
print(available)


# ------------------------------------------
# Safety Algorithm
# ------------------------------------------

work = available.copy()

finish = [False] * processes

safe_sequence = []


while len(safe_sequence) < processes:

    found = False

    for i in range(processes):

        if finish[i]:
            continue


        possible = True

        for j in range(resources):

            if need[i][j] > work[j]:

                possible = False

                break


        if possible:

            print(f"\nP{i} can execute")

            for j in range(resources):

                work[j] += allocation[i][j]


            finish[i] = True

            safe_sequence.append(i)

            found = True


    if not found:

        break


# ------------------------------------------
# Result
# ------------------------------------------

print("\n==========================================")
print("                RESULT")
print("==========================================")


if len(safe_sequence) == processes:

    print("\n✅ SAFE STATE")

    print("Safe Sequence:")

    print(" -> ".join(f"P{i}" for i in safe_sequence))

else:

    print("\n❌ UNSAFE STATE")

    print("No Safe Sequence Exists.")


print("\nFinished Status:")

for i in range(processes):

    if finish[i]:

        print(f"P{i}: Finished")

    else:

        print(f"P{i}: Not Finished")