import os


SERVER_FOLDER = "shared_files"


def list_server_files():

    print(
        "\n===== REMOTE FILES ====="
    )

    files = os.listdir(
        SERVER_FOLDER
    )

    for file in files:

        print(file)


def read_remote_file():

    filename = input(
        "\nEnter remote file name: "
    )

    path = os.path.join(
        SERVER_FOLDER,
        filename
    )

    if not os.path.exists(path):

        print(
            "Remote file not found."
        )

        return

    with open(
        path,
        "r"
    ) as file:

        data = file.read()

    print(
        "\nData received from server:"
    )

    print(data)


def main():

    print(
        "===== NFS CLIENT SIMULATION ====="
    )

    while True:

        print("\n1. List Remote Files")
        print("2. Read Remote File")
        print("3. Exit")

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            list_server_files()

        elif choice == "2":

            read_remote_file()

        elif choice == "3":

            print(
                "Client stopped."
            )

            break

        else:

            print(
                "Invalid choice."
            )


main()