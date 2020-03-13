
def mode(data):

    d = {}
    for i in data:
        if i not in d:

            d[i] = 1
        else:
            d[i] += 1

        Key_max = max(d, key=d.get)

    return Key_max
