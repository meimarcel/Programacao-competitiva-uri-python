x = 1
try:
    while True:
        N1 = input()
        N2 = input()
        Q = N2.count(N1)
        P = N2.rfind(N1) + 1
        if Q == 0:
            print("Caso #%d:" %x)
            print("Nao existe subsequencia")
        else:
            print("Caso #%d:" %x)
            print("Qtd.Subsequencias: %d" %Q)
            print("Pos: %d" %P)
        print("")
        x = x + 1
except EOFError:
    pass
        
