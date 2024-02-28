import copy
for nums in [48]:
    s = ''
    num = copy.copy(nums)
    while num != 0:
        s += str(num % 4)
        num //= 4
    s = s[::-1]
    s = s.replace('0', '')
    print(s)

