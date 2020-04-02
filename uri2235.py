z = input()
z = z.split(" ")
numerosz = [int(i) for i in z]
A, B, C = numerosz
if (A == B) or (A == C) or (B == C):
    print("S")
elif (A == B + C) or (B == A + C) or (C == A + B):
    print("S")
else:
    print("N")
