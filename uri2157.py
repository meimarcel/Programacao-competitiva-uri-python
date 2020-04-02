C = int(input())
for i in range(C):
    B, E = [int(i) for i in input().split(" ")]
    z = []
    while B <= E:
        z.append(B)
        B = B + 1
    z = "".join([str(x) for x in z])
    a = z[::-1]
    a = "".join([str(x) for x in a])
    print(z+a)    
