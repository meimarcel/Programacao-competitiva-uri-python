C = int(input())
x = 1
while x <= C:
    soma = 0
    total = 0
    z = input()
    z = z.split(" ")
    z = [int(i) for i in z]
    s = 1
    while s <= z[0]:
        total = total + z[s]
        s = s + 1
    a = 1
    while a <= z[0]:
        if z[a] > (total / z[0]):
            soma = soma + 1
        a = a + 1
    media = (soma / z[0]) * 100
    print("%.3f" %media+"%")
    x = x + 1
