N = int(input())
x = 1
v = []
while x <= N:
    z = input()
    z = z.split(" ")
    z = [int(i) for i in z]
    H, M, O = z
    if O == 1:
        if H in range(10):
            if M in range(10):
                v.append(("0"+str(H)+":"+"0"+str(M)+" - A porta abriu!"))
            else:
                v.append(("0"+str(H)+":"+str(M)+" - A porta abriu!"))
        else:
            if M in range(10):
                v.append((str(H)+":"+"0"+str(M)+" - A porta abriu!"))
            else:
                v.append((str(H)+":"+str(M)+" - A porta abriu!"))
    else:
        if H in range(10):
            if M in range(10):
                v.append(("0"+str(H)+":"+"0"+str(M)+" - A porta fechou!"))
            else:
                v.append(("0"+str(H)+":"+str(M)+" - A porta fechou!"))
        else:
            if M in range(10):
                v.append((str(H)+":"+"0"+str(M)+" - A porta fechou!"))
            else:
                v.append((str(H)+":"+str(M)+" - A porta fechou!"))
    x = x + 1
for i in v:
    print(i)
