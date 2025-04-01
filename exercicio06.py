time1 = input("digite o nome do time: ")
gols1 = int(input(f"digite o número de gols feitos pelo {time1}: "))
time2 = input("digite o nome do time: ")
gols2 = int(input(f"digite o número de gols feitos pelo {time2}: "))

if gols1>gols2:
    print(f"o time {time1} venceu a partida!")
else:
    if gols2>gols1:
        print(f"time {time2} ganhou a partida!")
    else:
        print(f"os times {time1} e {time2} empataram!")
