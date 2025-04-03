
tcombustivel = input("Bom dia!"
                     "digite G para gasolina-R$5.8\n0"
                     "digite E para etanol-R$4.90\n")
qlitros = float(input("Informe a quantidade de litros que você deseja: "))
vgas = 5.80
veta = 4.90
if tcombustivel == "G" or tcombustivel == "g" :
    valor = vgas * qlitros
else:
     if tcombustivel == "e" or tcombustivel == "e":
         valor = veta * qlitros
     else:
        print("tipo de combustivel invalido")
print(f"o valor a ser pago é R${valor:.2f}")