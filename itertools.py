import itertools
counter = itertools.count()
x = next(counter)
alpha = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','igloo','juliet']
frame = []
for x in range(len(alpha)):
    frame.append(x)
print(frame)

foo = zip(frame,alpha)
for x in foo:
    if x[0] % 2 == 0:
        print(x[1])

