def parse(data):
    data = list(data)
    box = []
    value = 5
    for char in data:
        if char == "i":
            value = value + 1
            box.append(value)
        elif char == "d":
            value = value - 1
            box.append(value)
        elif char == "s":
            value = value ** 2
            box.append(value)
        elif char == "o":
            if len(box) == 0:
                box.append(0)
                return box
    return box
parse("ii22ds")