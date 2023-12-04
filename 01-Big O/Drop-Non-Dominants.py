def print_items(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)


print_items(10)  # (O(n^2) + O(n)) -> O(n^2)
