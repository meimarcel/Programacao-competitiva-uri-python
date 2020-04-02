import math

try:
    while(True):
        PI = 3.14159
        G = 9.80665
        h1 = float(input())
        p1, p2 = [int(i) for i in input().split(" ")]
        n = int(input())
        for i in range(n):
            a, v = [float(s) for s in input().split(" ")]
            vx = math.cos((PI / 180) * a) * v
            vy = math.sin((PI / 180) * a) * v
            t1 = vy / G
            h2 = (vy ** 2) / (2 * G)
            hf = h1 + h2
            t2 = math.sqrt((2 * hf) / G)
            distancia = vx * (t1 + t2)
            if distancia > p1 and distancia < p2:
                print("%.5f -> DUCK"%(distancia))
            else:
                print("%.5f -> NUCK"%(distancia))
except EOFError:
    pass
