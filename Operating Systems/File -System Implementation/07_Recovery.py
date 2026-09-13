JOURNAL_FILE = "journal.txt"
DATA_FILE = "data.txt"


def write_journal(message):

    with open(
        JOURNAL_FILE,
        "a"
    ) as file:

        file.write(
            message + "\n"
        )


def show_journal():

    print(
        "\n========== JOURNAL =========="
    )

    try:

        with open(
            JOURNAL_FILE,
            "r"
        ) as file:

            content = file.read()

        if content:

            print(content)

        else:

            print("Journal is empty.")

    except FileNotFoundError:

        print("Journal does not exist.")


def clear_journal():

    open(
        JOURNAL_FILE,
        "w"
    ).close()

    print(
        "\nJournal cleared."
    )


def start_transaction():

    print(
        "\nStarting transaction..."
    )

    write_journal(
        "START"
    )

    print(
        "START recorded."
    )


def write_data():

    data = input(
        "Enter data to write: "
    )

    with open(
        DATA_FILE,
        "w"
    ) as file:

        file.write(data)

    write_journal(
        "WRITE"
    )

    print(
        "Data written."
    )


def commit_transaction():

    write_journal(
        "COMMIT"
    )

    print(
        "Transaction committed."
    )


def simulate_crash():

    print(
        "\nSYSTEM CRASH SIMULATED!"
    )

    recover()


def recover():

    print(
        "\n========== RECOVERY =========="
    )

    try:

        with open(
            JOURNAL_FILE,
            "r"
        ) as file:

            logs = file.read()

    except FileNotFoundError:

        print(
            "No journal found."
        )

        return

    print(
        "\nJournal found:"
    )

    print(logs)

    if "START" in logs:

        if "COMMIT" in logs:

            print(
                "Transaction was completed."
            )

            print(
                "No recovery needed."
            )

        else:

            print(
                "Incomplete transaction detected!"
            )

            print(
                "Recovery is required."
            )

    else:

        print(
            "No active transaction."
        )


def main():

    while True:

        print(
            "\n===== FILE SYSTEM RECOVERY ====="
        )

        print("1. Start Transaction")
        print("2. Write Data")
        print("3. Commit Transaction")
        print("4. Simulate Crash")
        print("5. Show Journal")
        print("6. Clear Journal")
        print("7. Exit")

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            start_transaction()

        elif choice == "2":

            write_data()

        elif choice == "3":

            commit_transaction()

        elif choice == "4":

            simulate_crash()

        elif choice == "5":

            show_journal()

        elif choice == "6":

            clear_journal()

        elif choice == "7":

            print(
                "\nProgram finished."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


main()