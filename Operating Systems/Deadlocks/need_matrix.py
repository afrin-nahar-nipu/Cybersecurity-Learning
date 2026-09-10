# Need Matrix Calculator

print("================================")
print("       NEED MATRIX")
print("================================")


# Allocation Matrix
allocation = [
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1]
]


# Maximum Matrix
maximum = [
    [3, 2, 2],
    [2, 2, 2],
    [3, 1, 2]
]


# Number of processes
processes = len(allocation)

# Number of resources
resources = len(allocation[0])


# Create Need Matrix
need = []

for i in range(processes):

    row = []

    for j in range(resources):

        value = maximum[i][j] - allocation[i][j]

        row.append(value)

    need.append(row)


# Display Allocation Matrix

print("\nAllocation Matrix:")

for i in range(processes):

    print(f"P{i}: {allocation[i]}")


# Display Maximum Matrix

print("\nMaximum Matrix:")

for i in range(processes):

    print(f"P{i}: {maximum[i]}")


# Display Need Matrix

print("\nNeed Matrix:")

for i in range(processes):

    print(f"P{i}: {need[i]}")


print("\nFormula:")
print("Need = Maximum - Allocation")