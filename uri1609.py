T = int(input())
x = 1
while x <= T:
    N = int(input())
    a = []
    z = input()
    z = [int(i) for i in z.split(" ")]
    z = set(z)
    print(len(z))
    x = x + 1
