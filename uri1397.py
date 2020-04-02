N = int(input())
while N != 0:
    soma1 = 0
    soma2 = 0
    x = 1
    while x <= N:
        z = input()
        z = [float(i) for i in z.split(" ")]
        A, B = z
        if A > B:
            soma1 = soma1 + 1
        elif B > A:
            soma2 = soma2 + 1
        x = x + 1
    print(soma1,soma2)
    N = int(input())
