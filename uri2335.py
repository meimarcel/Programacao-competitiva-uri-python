from math import acos,degrees
def formula_Bhaskara(a,b,z):
    x1 = (-(1/2*b)+(((1/2*b)**2)-(4*1/2)*(- a))**(1/2))
    angulo = (x1 + b) / z
    if angulo>1 or angulo<-1 or b>z+2*x1 or z>b+2*x1:
        print("Nao existe tal triangulo.")
    else:
        angulo1 = degrees(acos(angulo))
        if int(angulo1) == 0:
            print("Nao existe tal triangulo.")
        else:
            print(int(angulo1))
    return

try:
    while True:
        N = [float(i) for i in input().split(" ")]
        L1, L2 = N
        if L1 == L2:
            print("Nao existe tal triangulo.")
        elif L1 > L2:
            z = L1
            y = L2
            a = ((z ** 2) - (y ** 2))/4
            formula_Bhaskara(a,y,z)
        elif L2 > L1:
            z = L2
            y = L1
            a = ((z ** 2) - (y ** 2))/4
            formula_Bhaskara(a,y,z)
except EOFError:
    pass
