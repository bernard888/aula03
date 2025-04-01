nome = input("Digite o seu nome completo: ")
idade = int(input("digite a sua idade: "))
salario = float(input("digite seu salario atual: "))
aumento = float(input("qual o percentual de aumento salarial: "))
print(" ")

resultado = float(salario + salario * aumento / 100)

print(f"Olá, {nome}! Sua idade é {idade}, seu salário é de {salario} e o seu aumento é de {resultado}")