def funcThree() -> None:
    print('Three')


def funcTwo() -> None:
    funcThree()
    print('Two')


def funcOne() -> None:
    funcTwo()
    print('One')


funcOne()
