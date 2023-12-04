def print_items(n: int) -> None:
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(n=10)  # O(2n) == O(n)
