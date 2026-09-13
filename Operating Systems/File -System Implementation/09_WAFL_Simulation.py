disk = {}

current_file = {}

snapshot = None


def show_disk():

    print(
        "\n========== DISK =========="
    )

    if not disk:

        print(
            "Disk is empty."
        )

        return

    for block, data in disk.items():

        print(
            f"{block} -> {data}"
        )


def create_file():

    filename = input(
        "\nEnter file name: "
    )

    data = input(
        "Enter file data: "
    )

    block_number = len(disk)

    block_name = (
        f"Block-{block_number}"
    )

    disk[block_name] = data

    current_file.clear()

    current_file[
        filename
    ] = block_name

    print(
        f"\nFile created."
    )

    print(
        f"{filename} -> {block_name}"
    )


def update_file():

    if not current_file:

        print(
            "\nNo file exists."
        )

        return

    filename = list(
        current_file.keys()
    )[0]

    old_block = current_file[
        filename
    ]

    new_data = input(
        "\nEnter new data: "
    )

    # WAFL does not overwrite
    # the old block.

    new_block_number = len(disk)

    new_block = (
        f"Block-{new_block_number}"
    )

    disk[new_block] = new_data

    # Update file pointer

    current_file[
        filename
    ] = new_block

    print(
        "\nFile updated."
    )

    print(
        "Old Block:",
        old_block
    )

    print(
        "New Block:",
        new_block
    )


def create_snapshot():

    global snapshot

    snapshot = {

        "disk":
        disk.copy(),

        "file":
        current_file.copy()
    }

    print(
        "\nSnapshot created."
    )


def show_current_file():

    print(
        "\n===== CURRENT FILE ====="
    )

    if not current_file:

        print(
            "No file."
        )

        return

    for filename, block in current_file.items():

        print(
            f"{filename} -> {block}"
        )

        print(
            f"Data: {disk[block]}"
        )


def show_snapshot():

    print(
        "\n===== SNAPSHOT ====="
    )

    if snapshot is None:

        print(
            "No snapshot available."
        )

        return

    snapshot_disk = snapshot[
        "disk"
    ]

    snapshot_file = snapshot[
        "file"
    ]

    for filename, block in snapshot_file.items():

        print(
            f"{filename} -> {block}"
        )

        print(
            f"Data: {snapshot_disk[block]}"
        )


def restore_snapshot():

    global disk
    global current_file

    if snapshot is None:

        print(
            "\nNo snapshot available."
        )

        return

    disk = snapshot[
        "disk"
    ].copy()

    current_file = snapshot[
        "file"
    ].copy()

    print(
        "\nSnapshot restored."
    )


def main():

    while True:

        print(
            "\n========== WAFL SIMULATION =========="
        )

        print("1. Create File")
        print("2. Update File")
        print("3. Show Disk")
        print("4. Show Current File")
        print("5. Create Snapshot")
        print("6. Show Snapshot")
        print("7. Restore Snapshot")
        print("8. Exit")

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            create_file()

        elif choice == "2":

            update_file()

        elif choice == "3":

            show_disk()

        elif choice == "4":

            show_current_file()

        elif choice == "5":

            create_snapshot()

        elif choice == "6":

            show_snapshot()

        elif choice == "7":

            restore_snapshot()

        elif choice == "8":

            print(
                "\nProgram finished."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


main()