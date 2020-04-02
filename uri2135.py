k = 1
try:
    while True:
        n = int(input())
        z = [int(i) for i in input().split()]
        x = 0
        soma = 0
        while x < n:
            if z[x] == soma:
                print("Instancia %d" %k)
                print(z[x])
                x = n
            else:
                soma = soma + z[x]
                if x == (n - 1):
                    print("Instancia %d" %k)
                    print("nao achei")
            x = x + 1
        print("")
        k = k + 1
except EOFError:
    pass
