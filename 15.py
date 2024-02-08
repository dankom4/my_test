from itertools import combinations


def default():
    for a in range(0, 300):
        k = 0
        for x in range(1, 301):
            for y in range(1, 301):
                if (x**2 - 10 * x + 16 >0) or (y**2 - 10 * y + 21 >0) or (x * y < 2 *a) == 1:
                    k += 1
        if k == 90_000:
            print(a)
            break


def segments():
    def f(x):
        D = 17 <= x <= 58
        C = 29 <= x <= 80
        A = a1 <= x <= a2
        return (D <= (((not(C)) and (not A)) <= (not D)))

    ox = [i/4 for i in range(24*4, 76*4)]
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
        return (a % 7 == 0) and ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))

    for a in range(1, 30000):
        if all(f(x, a) == 1 for x in range(1, 30000)):
            print(a)


def conjunction():
    def f(x, a):
        return (x & 107 == 0) <= ((x & 55 != 0) <= (x & a != 0))

    for a in range(1, 10000):
        if all(f(x, a) for x in range(1, 10000)):
            print(a)


def sets():
    d = set()
    a = set(range(1000))
    p = {1, 2, 4, 8}
    q = {1, 2, 3, 4, 5, 6}

    def f(x):
        A = x in d
        P = x in p
        Q = x in q
        return (not A) <= (not(P or Q))

    for x in range(1000):
        if f(x) == 0:
            a.remove(x)
            d.add(x)
    print(len(d), d)

sets()























