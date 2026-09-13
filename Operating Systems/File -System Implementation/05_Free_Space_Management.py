TOTAL_BLOCKS = 20

# 0 = Free
# 1 = Used
disk = [0] * TOTAL_BLOCKS


def show_disk():
    print("\n========== DISK STATUS ==========")

    for i in range(TOTAL_BLOCKS):

        status = "FREE" if disk[i] == 0 else "USED"

        print(
            f"Block {i:2} : {status}"
        )

    print("=================================")


def show_free_blocks():

    free_blocks = []

    for i in range(TOTAL_BLOCKS):

        if disk[i] == 0:
            free_blocks.append(i)

    print("\nFree Blocks:")

    if free_blocks:

        print(free_blocks)

    else:

        print("No free blocks available.")


def allocate_blocks():

    try:

        number = int(
            input(
                "\nHow many blocks do you want? "
            )
        )

    except ValueError:

        print("Please enter a valid number.")
        return

    if number <= 0:

        print("Number must be greater than 0.")
        return

    free_blocks = []

    for i in range(TOTAL_BLOCKS):

        if disk[i] == 0:
            free_blocks.append(i)

    if len(free_blocks) < number:

        print(
            "\nNot enough free space!"
        )

        return

    allocated = free_blocks[:number]

    for block in allocated:

        disk[block] = 1

    print(
        "\nAllocated Blocks:",
        allocated
    )


def free_blocks():

    try:

        block_input = input(
            "\nEnter block numbers to free "
            "(example: 2 5 8): "
        )

        blocks = list(
            map(
                int,
                block_input.split()
            )
        )

    except ValueError:

        print(
            "Invalid block number."
        )

        return

    for block in blocks:

        if block < 0 or block >= TOTAL_BLOCKS:

            print(
                f"Block {block} does not exist."
            )

        elif disk[block] == 0:

            print(
                f"Block {block} is already free."
            )

        else:

            disk[block] = 0

            print(
                f"Block {block} released."
            )


def show_bitmap():

    print("\n========== BIT MAP ==========")

    print(
        "Block:",
        " ".join(
            f"{i:2}"
            for i in range(TOTAL_BLOCKS)
        )
    )

    print(
        "Bit  :",
        " ".join(
            str(bit)
            for bit in disk
        )
    )

    print("\n0 = Free")
    print("1 = Used")


def main():

    while True:

        print("\n\n===== FREE SPACE MANAGEMENT =====")

        print("1. Show Disk")
        print("2. Show Free Blocks")
        print("3. Allocate Blocks")
        print("4. Free Blocks")
        print("5. Show Bit Map")
        print("6. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            show_disk()

        elif choice == "2":

            show_free_blocks()

        elif choice == "3":

            allocate_blocks()

        elif choice == "4":

            free_blocks()

        elif choice == "5":

            show_bitmap()

        elif choice == "6":

            print(
                "\nProgram finished."
            )

            break

        else:

            print(
                "\nInvalid choice!"
            )


main()