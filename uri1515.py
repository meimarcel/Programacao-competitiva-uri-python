N = int(input())
while N != 0:
    menor = 10000000
    k = "a"
    for i in range(N):
        z = input().split(" ")
        X = z[0]
        A = int(z[1])
        T = int(z[2])
        S = A - T
        if S < menor:
            menor = S
            k = X
    print(k)
    N = int(input())
