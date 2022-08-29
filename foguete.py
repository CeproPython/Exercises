# Alexsey
# importando método sleep que suspende a execução por alguns segundos
from time import sleep
# imprimindo cabeçalho
print('VAMOS PARA MARTE')
# pausa de 1 segundo
sleep(1)
print('CONTAGEM REGRESSIVA PARA MARTE')
# laço que começa em 10 até 0 com passo -1
for cont in range(10, -1, -1):
    # imprimindo o contador
    print(cont)
    # pausa de 1 segundo
    sleep(1)
# imprimindo as mensagens 
print('SEU FOGUETE PARTIU PARA MARTE!')

###############################

# Vanessa
print("contagem regressiva")
x = 10
while x >=0:
    print(x)
    if x == 0:
     print("fogo")
    x = x-1