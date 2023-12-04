def print_items(a: int, b: int) -> None:
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


print_items(1, 10)  # O(a + b)

# ---------------------------------


def print_items2(a: int, b: int) -> None:
    for i in range(a):
        for j in range(b):
            print(i, j)


print_items2(1, 10)  # O(a * b)
