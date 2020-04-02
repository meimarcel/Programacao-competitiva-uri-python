C = int(input())
x = 1
while x <= C:
    R = input()
    F = []
    for i in R:
        F.append(i)
    if "." in F:
        F.remove(".")
    F = "".join([str(i) for i in F])
    F = int(F)
    a = []
    b = []
    s = []
    k = 0
    if "." in R:
        a = []
        l = R.split(".")
        for i in l[0]:
            a.append(i)
        for i in l[1]:
            b.append(i)
    else:
        for i in R:
            a.append(i)
    g = []
    for i in R:
        g.append(i)
    for i in g:
        if "." in g:
            g.remove(".")
    v = len(a)-1
    while v >= 0:
        s.append(a[v])
        v = v - 1
    if len(b) != 0:
        b1 = "".join([str(x) for x in b])
        b1 = int(b1)
    s1 = "".join([str(x) for x in s])
    s1 = int(s1)
    if len(b) >= len(a):
        while b1 != s1:
            if len(b) == 1:
                k = k + 0.1
                k = round(k,1)
                b1 = b1 + 1
            elif len(b) == 2:
                k = k + 0.01
                k = round(k,2)
                b1 = b1 + 1
            elif len(b) == 3:
                k = k + 0.001
                k = round(k,3)
                b1 = b1 + 1
            elif len(b) == 4:
                k = k + 0.0001
                k = round(k,4)
                b1 = b1 + 1
            elif len(b) == 5:
                k = k + 0.00001
                k = round(k,5)
                b1 = b1 + 1
            elif len(b) == 6:
                k = k + 0.000001
                k = round(k,6)
                b1 = b1 + 1
    else:
        if len(b) ==  0:
            if len(a) == 1:
                k = 0
            if len(a) == 2:
                while g[0] != g[-1]:
                    F = F + 0.1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 3:
                while g[0] != g[-1]:
                    F = F + 0.1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 4:
                while g[0] != g[-1] or g[1] != g[-2]:
                    F = F + 0.1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 5:
                while g[0] != g[-1] or g[1] != g[-2]:
                    F = F + 0.1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 6:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3]:
                    F = F + 0.1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
        elif len(b) == 1:
            if len(a) == 1:
                while g[0] != g[-1]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 2:
                while g[0] != g[-1]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 3:
                while g[0] != g[-1] or g[1] != g[-2]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 4:
                while g[0] != g[-1] or g[1] != g[-2]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 5:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 6:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.1
                    k = round(k,1)
                    g = []
                    v = [g.append(i) for i in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
        elif len(b) == 2:
            if len(a) == 3:
                while g[0] != g[-1] or g[1] != g[-2]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.01
                    k = round(k,2)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 4:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.01
                    k = round(k,2)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 5:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.01
                    k = round(k,2)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 6:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3] or g[3] != g[-4]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.01
                    k = round(k,2)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
        elif len(b) == 3:
            if len(a) == 4:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.001
                    k = round(k,3)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 5:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3] or g[3] != g[-4]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.001
                    k = round(k,3)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 6:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3] or g[3] != g[-4]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.001
                    k = round(k,3)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
        elif len(b) == 4:
            if len(a) == 5:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3] or g[3] != g[-4]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.0001
                    k = round(k,4)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
            elif len(a) == 6:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3] or g[3] != g[-4] or g[4] != g[-5]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.0001
                    k = round(k,4)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")
                    if g[-1] == "0":
                        g = g[:-1]
        elif len(b) == 5:
            if len(a) == 6:
                while g[0] != g[-1] or g[1] != g[-2] or g[2] != g[-3] or g[3] != g[-4] or g[4] != g[-5]:
                    F = F + 1
                    m = str(F)
                    k = k + 0.00001
                    k = round(k,5)
                    g = []
                    v = [g.append(x) for x in m]
                    for i in g:
                        if "." in g:
                            g.remove(".")

    print(k)
    x = x + 1
