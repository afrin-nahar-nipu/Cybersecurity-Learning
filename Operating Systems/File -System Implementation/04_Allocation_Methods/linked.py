# Linked Allocation with User Input

file_name = input("Enter File Name: ")

blocks_input = input(
    "Enter Blocks separated by space: "
)


blocks = list(
    map(
        int,
        blocks_input.split()
    )
)


linked_blocks = {}


for i in range(len(blocks)):

    if i == len(blocks) - 1:

        linked_blocks[
            blocks[i]
        ] = None

    else:

        linked_blocks[
            blocks[i]
        ] = blocks[i + 1]


print(
    f"\n{file_name} Allocation:"
)


current = blocks[0]


while current is not None:

    print(
        f"Block {current}",
        end=" → "
    )

    current = linked_blocks[current]


print("End")