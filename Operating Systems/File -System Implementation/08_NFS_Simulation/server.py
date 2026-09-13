import os


SHARED_FOLDER = "shared_files"


def show_files():

    print(
        "\n===== SERVER FILES ====="
    )

    files = os.listdir(
        SHARED_FOLDER
    )

    if not files:

        print("No files available.")

    else:

        for file in files:

            print(file)


def read_file():

    filename = input(
        "\nEnter file name: "
    )

    path = os.path.join(
        SHARED_FOLDER,
        filename
    )

    if not os.path.exists(path):

        print(
            "File not found."
        )

        return

    with open(
        path,
        "r"
    ) as file:

        data = file.read()

    print(
        "\nFile Content:"
    )

    print(data)


def main():

    print(
        "===== NFS SERVER SIMULATION ====="
    )

    while True:

        print("\n1. Show Files")
        print("2. Read File")
        print("3. Exit")

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            show_files()

        elif choice == "2":

            read_file()

        elif choice == "3":

            print(
                "Server stopped."
            )

            break

        else:

            print(
                "Invalid choice."
            )


main()