C = int(input())
for i in range(C):
    a, b = input().split(" ")
    if a == b:
        print("empate")
    elif (a == "tesoura") and (b == "papel" or b =="lagarto"):
        print("rajesh")
    elif (b == "tesoura") and (a == "papel" or a == "lagarto"):
        print("sheldon")
    elif (a == "papel") and (b == "pedra" or b == "spock"):
        print("rajesh")
    elif (b == "papel") and (a == "pedra" or a == "spock"):
        print("sheldon")
    elif (a == "pedra") and (b == "lagarto" or b == "tesoura"):
        print("rajesh")
    elif (b == "pedra") and (a == "lagarto" or a == "tesoura"):
        print("sheldon")
    elif (a == "lagarto") and (b == "spock" or b == "papel"):
        print("rajesh")
    elif (b == "lagarto") and (a == "spock" or a == "papel"):
        print("sheldon")
    elif (a == "spock") and (b == "tesoura" or b == "pedra"):
        print("rajesh")
    elif (b == "spock") and (a == "tesoura" or a == "pedra"):
        print("sheldon")
