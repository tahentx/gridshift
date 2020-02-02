# def multiplication_table(row: int,column: int) -> list:
#     scalar = 1
#     for i in range(len(column)):
#         row = list(map(lambda x: x * scalar, column))
#         scalar = scalar + 1
#         print(row)

# multiplication_table(5,4)

def tester(n):
    z = range(n)
    inc = 1
    foo = []
    for i in z:
        boo = list(map(lambda x: x * inc, z))
        foo.append(boo)
        inc = inc + 1
    for a in foo:
        a.remove(0)
    print(foo)

tester(8)