
print("A media necessária para passar é 7.0")
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

media = ((n1 + n2 + n3) /3)

if (media >= 7.0):
    print(f"sua média é {media}, você está aprovado!")
else:
    print(f"sua média é {media}, você está reprovado!")