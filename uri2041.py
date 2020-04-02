try:
    while True:
        N = int(input())
        a = 0
        v = 1
        s = [3]
        s1 = []
        if N == 1:
            print(3)
        else:
            while v < N:
                while a < len(s):
                    if a + 2 <= (len(s)-1):
                        if s[a] == s[a+1] == s[a+2] == 1:
                            s1.append(3)
                            s1.append(1)
                            a = a + 3
                        elif s[a] == s[a+1] == s[a+2] == 2:
                            s1.append(3)
                            s1.append(2)
                            a = a + 3
                        elif s[a] == s[a+1] == s[a+2] == 3:
                            s1.append(3)
                            s1.append(3)
                            a = a + 3
                    if a + 1 <= (len(s)-1):
                        if s[a] == s[a+1] == 1:
                            s1.append(2)
                            s1.append(1)
                            a = a + 2
                        elif s[a] == s[a+1] == 2:
                            s1.append(2)
                            s1.append(2)
                            a = a + 2
                        elif s[a] == s[a+1] == 3:
                            s1.append(2)
                            s1.append(3)
                            a = a + 2
                    if a + 1 <= (len(s) - 1):
                        if s[a] != s[a + 1] and s[a] == 1:
                            s1.append(1)
                            s1.append(1)
                            a = a + 1
                        elif s[a] != s[a + 1] and s[a] == 2:
                            s1.append(1)
                            s1.append(2)
                            a = a + 1
                        elif s[a] != s[a + 1] and s[a] == 3:
                            s1.append(1)
                            s1.append(3)
                            a = a + 1
                    elif a <= (len(s) - 1):
                        if s[a - 1] != s[a] and s[a] == 1:
                            s1.append(1)
                            s1.append(1)
                            a = a + 1
                        elif s[a - 1] != s[a] and s[a] == 2:
                            s1.append(1)
                            s1.append(2)
                            a = a + 1
                        elif s[a - 1] != s[a] and s[a] == 3:
                            s1.append(1)
                            s1.append(3)
                            a = a + 1
                        elif s[a] == 1:
                            s1.append(1)
                            s1.append(1)
                            a = a + 1
                        elif s[a] == 2:
                            s1.append(1)
                            s1.append(2)
                            a = a + 1
                        elif s[a] == 3:
                            s1.append(1)
                            s1.append(3)
                            a = a + 1
                a = 0
                s = s1
                s1 = []
                v = v + 1
            print("".join([str(k) for k in s]))
except EOFError:
  pass
