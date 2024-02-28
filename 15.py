from itertools import combinations


def default():
    for a in range(0, 300):
        k = 0
        for x in range(1, 301):
            for y in range(1, 301):
                if ((39 != (y + (2 * x))) or (a < x) or (a < y)) == 1:
                    k += 1
        if k == 90_000:
            print(a)


def segments():
    def f(x):
        P = 3 <= x <= 13
        Q = 7 <= x <= 17
        A = 1 <= x <= a2
        return (A <= P) or (not Q)

    ox = [i/4 for i in range(2*4, 18*4)]
    m = []
    d = dict()
    for a1, a2 in combinations(ox, 2):
        if all(f(x) for x in ox):
            m.append(a2-a1)
            if a2-a1 not in d.keys():
                d[a2-a1] = (a1, a2)

    print(d.get(min(m)), min(m))


def divider():
    def f(x, a):
        return ((x + a) >= 150) or ((x % 3 != 0) <= (x % 7 != 0))

    for a in range(1, 30000):
        if all(f(x, a) == 1 for x in range(1, 30000)):
            print(a)


def conjunction():
    def f(x, a):
        return (x & a != 0) <= (((x & 17 == 0) and (x & 5 == 0)) <= (x & 3 != 0))

    for a in range(1, 10000):
        if all(f(x, a) for x in range(1, 10000)):
            print(a)


def sets():
    d = set()
    a = set(range(1000))
    p = {2, 4, 6, 8, 10, 12}
    q = {3, 6, 9, 12, 15}

    def f(x):
        A = x in d
        P = x in p
        Q = x in q
        return P <= ((Q and (not A)) <= (not P))

    for x in range(1000):
        if f(x) == 0:
            a.remove(x)
            d.add(x)
    print(len(d), d)


segments()
