# Indexed Allocation with User Input

file_name = input(
    "Enter File Name: "
)


blocks_input = input(
    "Enter Data Blocks separated by space: "
)


index_block = list(
    map(
        int,
        blocks_input.split()
    )
)


print(
    f"\n{file_name} Index Block:"
)


for position in range(
    len(index_block)
):

    print(
        f"Index {position} "
        f"→ Block {index_block[position]}"
    )