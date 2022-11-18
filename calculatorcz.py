num1 = float(input("zadej prvni čislo: "))
num2 = float(input("zadej druhe čislo: "))
cobudechtit =(input("zadej * pro krat / pro deleni + pro scitani - pro odcitani: "))


if cobudechtit == "*":
    print(num1 * num2)

elif cobudechtit == "/":
    print(num1 / num2)

elif cobudechtit == "+":
    print(num1 + num2)

elif cobudechtit== "-":
    print(num1 - num2)

else:
    print("si asi idiot a asi si udelal neco blbe")

input("zmačknete enter pro ukonceni")

