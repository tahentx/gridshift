def multiplication_table(row: int,column: int) -> list:
    x = 0
    foo = []
    for row in range(row):
        x = x + 1
        foo.append(x)
    print(foo)


multiplication_table(5,4)
