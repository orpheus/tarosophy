ncDict = {
    'a': 1,
    'b': 2,
    'g': 3,
    'd': 4,
    'e': 5,
    'u': 6,
    'v': 6,
    'w': 6,
    'z': 7,
    'h': 8,
    'th': 9,
    'i': 1,
    'j': 1,
    'y': 1,
    'c': 2,
    'k': 2,
    'l': 3,
    'm': 4,
    'n': 5,
    'x': 6,
    'o': 7,
    'f': 8,
    'p': 8,
    'tz': 9,
    'q': 1,
    'r': 2,
    's': 3,
    't': 4
}


def calculateNamePath(name):
    sum = 0
    for letter in name:
        sum += ncDict.get(letter, 0)
    return sum


def numberfy(num):
    num_str = str(num)

    max = 9
    sum = 0

    for i in num_str:
        sum += int(i)

    while sum > max:
        tmp = str(sum)
        sum = 0
        for i in tmp:
            sum += int(i)
    return sum


if __name__ == "__main__":
    name = raw_input("Type your full name:\n")
    birthday = raw_input("Type your birthday: dd/mm/yyyy ***WITHOUT SLASHES***\n")
    soul_path = numberfy(birthday)
    name_path = numberfy(calculateNamePath(name.lower()))
    print "Soul path: %s \nName path: %s" % (soul_path, name_path)

