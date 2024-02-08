from itertools import product

count = 0
for i in product('012345678', repeat=5):
    if i.count('5') == 1 and '00' not in i and '11' not in i and '22' not in i and '33' not in i and '44' not in i and '55' not in i and '66' not in i and '77' not in i and '88' not in i:
        pass
    if i.count('5') == 1 and i[0] != i[1] and i[1] != i[2] and i[2] != i[3] and i[3] != i[4] and i[0] != '0':
        count += 1

print(count)
