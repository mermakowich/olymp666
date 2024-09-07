s = input()
m = []
for i in s:
    m.append(i)
d = int(input())
m2 = []
s = 0
zv = 0
for i in m:
    if i != "?" and i != "*":
        m2.append(i)
    if i == "*":
        zv += 1
    if i == "?":
        s += 1
if (zv == 0 and len(m2) < d) or (len(m2) > d and zv + s < len(m2) - d):
    print("Impossible")
else:
    inv = []
    inz = []
    for i in range(len(m)):
        if m[i] == "?":
            inv.append(i)
        if m[i] == "*":
            inz.append(i)

    rs = len(m2)

    if len(m2) == d:
        print(*m2, sep="")
    if len(m2) > d:
        for i in inv:
            if rs == d:
                break
            nn = i - 1
            m.pop(i)
            m.pop(nn)
            rs -= 1
        if rs != d:

            for i in inz:
                if rs == d:
                    break
                nn = i - 1
                m.pop(i)
                m.pop(nn)
                rs -= 1
        mv = []
        for i in m:
            if i != "?" and i != "*":
                mv.append(i)
        print(*mv, sep="")


    # if d > len(m2) and zv != 0:
    #     i = inz[0]
    #     mmm = m2[]
