# Contiguous Allocation with User Input

disk = [None] * 10

file_name = input("Enter File Name: ")

start_block = int(
    input("Enter Starting Block: ")
)

size = int(
    input("Enter Number of Blocks: ")
)


# Check if space is available

available = True

for i in range(
    start_block,
    start_block + size
):

    if i >= len(disk) or disk[i] is not None:
        available = False
        break


# Allocate blocks

if available:

    for i in range(
        start_block,
        start_block + size
    ):

        disk[i] = file_name

    print("\nFile Allocated Successfully!")

else:

    print(
        "\nContiguous Space Not Available!"
    )


# Show Disk

print("\nDisk Status:")

for i in range(len(disk)):

    print(
        f"Block {i}: {disk[i]}"
    )