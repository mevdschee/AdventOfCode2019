import os

#      |     |         |     |
#   A  |  B  |    C    |  D  |  E
#      |     |         |     |
# -----+-----+---------+-----+-----
#      |     |         |     |
#   F  |  G  |    H    |  I  |  J
#      |     |         |     |
# -----+-----+---------+-----+-----
#      |     |A|B|C|D|E|     |
#      |     |-+-+-+-+-|     |
#      |     |F|G|H|I|J|     |
#      |     |-+-+-+-+-|     |
#   K  |  L  |K|L|?|N|O|  N  |  O
#      |     |-+-+-+-+-|     |
#      |     |P|Q|R|S|T|     |
#      |     |-+-+-+-+-|     |
#      |     |U|V|W|X|Y|     |
# -----+-----+---------+-----+-----
#      |     |         |     |
#   P  |  Q  |    R    |  S  |  T
#      |     |         |     |
# -----+-----+---------+-----+-----
#      |     |         |     |
#   U  |  V  |    W    |  X  |  Y
#      |     |         |     |

neighbors = {
    "A": ["HL", "BF", ""],
    "B": ["H", "ACG", ""],
    "C": ["H", "BDH", ""],
    "D": ["H", "CEI", ""],
    "E": ["HN", "DJ", ""],
    "F": ["L", "AGK", ""],
    "G": ["", "BFHL", ""],
    "H": ["", "CGI", "ABCDE"],
    "I": ["", "DHJN", ""],
    "J": ["N", "EIO", ""],
    "K": ["L", "FLP", ""],
    "L": ["", "GKQ", "AFKPU"],
    "N": ["", "IOS", "EJOTY"],
    "O": ["N", "JNT", ""],
    "P": ["L", "KQU", ""],
    "Q": ["", "LPRV", ""],
    "R": ["", "QSW", "UVWXY"],
    "S": ["", "NRTX", ""],
    "T": ["N", "OSY", ""],
    "U": ["LR", "PV", ""],
    "V": ["R", "QUW", ""],
    "W": ["R", "RVX", ""],
    "X": ["R", "SWY", ""],
    "Y": ["NR", "TX", ""],
}

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    lines = f.read().rstrip().split("\n")
    width = len(lines[0])
    height = len(lines)
    bugs = {0: {}}
    for y in range(height):
        for x in range(width):
            if lines[y][x] == "#":
                bugs[0][(x, y)] = True
    for minutes in range(200):
        minlevel = min(bugs.keys())
        maxlevel = max(bugs.keys())
        new_bugs = {}
        for level in range(minlevel - 1, maxlevel + 2):
            for y in range(height):
                for x in range(width):
                    if (x, y) == (2, 2):
                        continue
                    count = 0
                    c = chr(ord("A") + y * width + x)
                    for dl in range(-1, 2):
                        for nc in list(neighbors[c][dl + 1]):
                            nx, ny = (
                                (ord(nc) - ord("A")) % width,
                                (ord(nc) - ord("A")) // width,
                            )
                            if level + dl in bugs and (nx, ny) in bugs[level + dl]:
                                count += 1
                    bug = level in bugs and (x, y) in bugs[level]
                    if bug:
                        new_bug = count == 1
                    else:
                        new_bug = count == 1 or count == 2
                    if new_bug:
                        if not level in new_bugs:
                            new_bugs[level] = {}
                        new_bugs[level][(x, y)] = new_bug
        bugs = new_bugs

    print(sum([len(x.values()) for x in bugs.values()]))
