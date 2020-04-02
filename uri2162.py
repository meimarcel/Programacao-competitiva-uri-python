N = int(input())
z = input()
z = z.split(" ")
z = [int(i) for i in z]
x = 0
if N == 2:
  if (z[0] < z[1]):
    S = 1
  elif(z[0] > z[1]):
    S = 1
  else:
    S = 0
else:
    if (N % 2) == 0:
        x = 1
        if (z[0] < z[1]):
            while x <= (N - 1):
                if (x == (N - 1)):
                    x = N
                elif (z[x] > z[x + 1] < z[x + 2]):
                    S = 1
                else:
                    S = 0
                    x = N
                x = x + 2
        elif (z[0] > z[1]):
            while x <= (N - 1):
                if (x == (N - 1)):
                    x = N
                elif (z[x] < z[x + 1] > z[x + 2]):
                    S = 1
                else:
                    S = 0
                    x = N
                x = x + 2
        else:
            S = 0
    else:
        if (z[0] < z[1]):
            while x <= (N - 1):
                if (x == (N - 1)):
                    x = N
                elif (z[x] < z[x + 1] > z[x + 2]):
                    S = 1
                else:
                    S = 0
                    x = N
                x = x + 2
        elif (z[0] > z[1]):
            while x <= (N - 1):
                if (x == (N - 1)):
                    x = N
                elif (z[x] > z[x + 1] < z[x + 2]):
                    S = 1
                else:
                    S = 0
                    x = N
                x = x + 2
        else:
            S = 0
print(S)
