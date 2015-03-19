# -*- coding: utf-8 -*-
import time

Pedra = 0
Papel = 1
Tesoura = 2
Lagarto = 3
Spock = 4

lista = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]

computer = 0
player = 0

from random import randint
print("Pedra-Papel-Tesoura-Lagarto-Spock.")
time.sleep(1)
print("Preparado para jogar?")
time.sleep(1)
print("Vence o jogo quem conseguir 3 vitórias na sequência.")
time.sleep(1)
print("Estou pronto pode fazer a sua escolha.")
time.sleep(2)
 
while computer < 3 and player < 3: #discutir
    p = -1
    p = int(input("Pedra: 0, Papel: 1, Tesoura: 2, Lagarto: 3, Spock: 4?"))
    c = randint(0,4)
        
    print("Sua escolha: ", lista[p])  
    time.sleep(1)
    
    print("Computador: ", lista[c])
    time.sleep(1)
    
    if c == 0 and p == 1:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 0 and p == 2:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == 0 and p == 3:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 0 and p == 4:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == 1 and p == 0:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == 1 and p == 2:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 1 and p == 3:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == 1 and p == 4:
        time.sleep(1)
        print("Acertei!")
        computer += 1 ; player = 0
    elif c == 2 and p == 0:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 2 and p == 1:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == 2 and p == 3:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == 2 and p == 4:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 3 and p == 0:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == 3 and p == 1:
        time.sleep(1)
        print("Acertei!")
        computer += 1 ; player = 0
    elif c == 3 and p == 2:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == 3 and p == 4:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 4 and p == 0:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 4 and p == 1:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 4 and p == 2:
        time.sleep(1)
        print("Boa escolha!")
        player += 1 ; computer = 0
    elif c == 4 and p == 3:
        time.sleep(1)
        print("Acertei")
        computer += 1 ; player = 0
    elif c == p:
        time.sleep(1)
        print("Empatamos, jogue de novo.")
    elif p >= 5 or p < 0:
        time.sleep(1)
        print("Essa opção não existe. Jogue de novo.")
        
    print("PLACAR: VOCÊ: " , player , "COMPUTADOR: " , computer )
        
    if computer == 3:
        
        print("Você perdeu o jogo!")
    
    if player == 3:
        
        print("Parabéns! Você venceu o jogo.")
    