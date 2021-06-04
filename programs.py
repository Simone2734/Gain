
print("...:::Kasa z pompy:::...")

a = int(input("Ilość kasy puszczonej (w dolarach):"))
b = int(input("Nastawiony zysk w procentach:"))
c = input("Naciśnij * aby policzyć zarobioną kase:")
operators = {"*": (a*b/100)}
if c == "*":
    print("Zarobek to:" + str(operators["*"]))






