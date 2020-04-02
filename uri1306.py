R = 1
N = 1
x = 1
while (R != 0) and (N != 0):
    z = input()
    z = z.split(" ")
    z = [int(i) for i in z]
    R, N = z
    if (R != 0) and (N != 0):
        if N >= R:
            print("Case %d:"%x,0)
        else:
            if R > (N + (N * 26)):
                print("Case %d: impossible" %x)
            else:
                D = 1
                while D <= 26:
                    if R <= (N + (N * D)):
                        print("Case %d:"%x,D)
                        D = 26
                    D = D + 1
    x = x + 1
