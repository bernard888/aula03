mes = int(input("digite aqui um número de 1 a 12: "))

"""if mes<1 or mes>12:
    print("valor invalido")
else:
    if mes==1:
        print("janeiro")
    elif mes==2:
        print("fevereiro")
    elif mes==3:
        print("março")
    elif mes==4:
        print("abril")
    elif mes==5:
        print("maio")
    elif mes==6:
        print("junho")
    elif mes==7:
        print("julho")
    elif mes==8:
        print("agosto")
    elif mes==9:
        print("setembro")
    elif mes==10:
        print("outubro")
    elif mes==11:
        print("novembro")
    else:
        print("dezembro")"""

match mes:
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("março")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8:
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("outubro")
    case 11:
        print("novembro")
    case 12:
        print("dezembro")
    case _:
        print("numero invalido")