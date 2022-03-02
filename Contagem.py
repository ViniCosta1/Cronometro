from sqlite3 import TimestampFromTicks
import time

# Cronômetro

tempo = int(input("Quanto tempo você quer que eu conte? \n"))

time.sleep(1)
print("Começando a contagem...")
time.sleep(2)

for sec in range(0, tempo):
    print(sec)
    time.sleep(1)
    continue
print(tempo)
print("Acabou a contagem!")

# Contagem regressiva

regressao = int(input("Digite sua contagem regressiva: \n"))

time.sleep(1)
print("Começando a contagem...")
time.sleep(2)

for falt in range(regressao, 0, -1):
    print(falt)
    time.sleep(1)
    continue
print('0')
print(f"Terminou a contagem de {regressao} segundos!")