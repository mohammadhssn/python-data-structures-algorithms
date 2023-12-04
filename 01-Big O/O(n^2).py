def print_items(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items(n=10)

# ------------------------------------------


def print_items2(n: int) -> None:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


print_items2(n=10)  # O(n^3) == O(n^2)
