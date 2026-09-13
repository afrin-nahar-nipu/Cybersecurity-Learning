import time


cache = {}


def read_from_disk(filename):

    print(
        f"\nReading {filename} from DISK..."
    )

    # Simulate slow disk access
    time.sleep(2)

    data = (
        f"Contents of {filename}"
    )

    return data


def read_file(filename):

    # Check cache first

    if filename in cache:

        print(
            f"\n{filename} found in CACHE."
        )

        return cache[filename]

    # If not in cache
    # read from disk

    data = read_from_disk(
        filename
    )

    # Store data in cache

    cache[filename] = data

    return data


def clear_cache():

    cache.clear()

    print(
        "\nCache cleared."
    )


def show_cache():

    print(
        "\n========== CACHE =========="
    )

    if not cache:

        print("Cache is empty.")

    else:

        for filename, data in cache.items():

            print(
                f"{filename} -> {data}"
            )


def main():

    while True:

        print(
            "\n===== FILE CACHE SIMULATION ====="
        )

        print("1. Read File")
        print("2. Show Cache")
        print("3. Clear Cache")
        print("4. Exit")

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            filename = input(
                "Enter file name: "
            )

            start = time.time()

            data = read_file(
                filename
            )

            end = time.time()

            print(
                "\nData:",
                data
            )

            print(
                f"Time Taken: "
                f"{end - start:.2f} seconds"
            )

        elif choice == "2":

            show_cache()

        elif choice == "3":

            clear_cache()

        elif choice == "4":

            print(
                "\nProgram finished."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


main()