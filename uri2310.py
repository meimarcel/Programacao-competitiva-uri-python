N = int(input())
x = 1
nomes = []
somaS = 0
somaB = 0
somaA = 0
somaS1 = 0
somaB1 = 0
somaA1 = 0
while x <= N:
    nomes.append(input())
    z = input()
    z_n = z.split(" ")
    numerosz = [int(i) for i in z_n]
    S, B, A = numerosz
    somaS = somaS + S
    somaB = somaB + B
    somaA = somaA + A
    a = input()
    a_n = a.split(" ")
    numerosa = [int(i) for i in a_n]
    S1, B1, A1 = numerosa
    somaS1 = somaS1 + S1
    somaB1 = somaB1 + B1
    somaA1 = somaA1 + A1
    x = x + 1
pS = (somaS1 / somaS) * 100
pB = (somaB1 / somaB) * 100
pA = (somaA1 / somaA) * 100
print("Pontos de Saque: %.2f" %pS,"%.")
print("Pontos de Bloqueio: %.2f" %pB,"%.")
print("Pontos de Ataque: %.2f" %pA,"%.")


    
