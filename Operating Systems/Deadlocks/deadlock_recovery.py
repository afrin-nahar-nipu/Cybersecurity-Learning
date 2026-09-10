# ==========================================
#       DEADLOCK RECOVERY SIMULATION
# ==========================================

print("==========================================")
print("       DEADLOCK RECOVERY SIMULATOR")
print("==========================================")


# ------------------------------------------
# Processes and Resources
# ------------------------------------------

available = [0, 0]


allocation = {
    "P1": [1, 0],
    "P2": [0, 1]
}


request = {
    "P1": [0, 1],
    "P2": [1, 0]
}


# ------------------------------------------
# Display Initial State
# ------------------------------------------

print("\nInitial Available Resources:")
print(available)


print("\nProcess Information:")

for process in allocation:

    print(f"\n{process}")

    print("Allocated:", allocation[process])

    print("Request  :", request[process])


# ------------------------------------------
# Deadlock Situation
# ------------------------------------------

print("\n==========================================")

print("Checking System...")

print("==========================================")


print("\nDeadlock Situation:")

print("P1 holds Resource A and waits for Resource B")

print("P2 holds Resource B and waits for Resource A")


print("\n❌ DEADLOCK DETECTED!")


# ------------------------------------------
# Select Victim Process
# ------------------------------------------

victim = "P2"


print("\n==========================================")

print("RECOVERY PROCESS")

print("==========================================")


print(f"\nSelected Victim Process: {victim}")


print(f"\nTerminating {victim}...")


# ------------------------------------------
# Release Resources
# ------------------------------------------

for i in range(len(available)):

    available[i] += allocation[victim][i]


print(f"\nResources released by {victim}")

print("Available Resources Now:")

print(available)


# ------------------------------------------
# Remove Victim
# ------------------------------------------

del allocation[victim]

del request[victim]


# ------------------------------------------
# Remaining Processes
# ------------------------------------------

print("\nRemaining Processes:")

for process in allocation:

    print(process)


# ------------------------------------------
# Recovery Result
# ------------------------------------------

print("\n==========================================")

print("RECOVERY RESULT")

print("==========================================")


print("\nDeadlock Broken!")

print("System can continue execution.")


print("\nP1 can now acquire Resource B")

print("\nP1 completes successfully")


print("\nAvailable Resources:")

print(available)