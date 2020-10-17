# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 07:48:51 2020

@author: Gabriel Paiva de Almeida
@author: Rodrigo de Liima Azeredo

"""

import random

# fichas= int(input('Quantidade de fichas: '))
# aposta= int(input('Quanto deseja apostar? '))
A= 1
J= 0
Q= 0
K= 0
baralho= [A,2,3,4,5,6,7,8,9,10,J,Q,K]
baralho[9]= 0
banco=[]
jogador=[]

embaralhar=baralho[:] #Criou uma copia da lista baralho
random.shuffle(embaralhar) #Embaralhou aleatoriamente a lista
c= 0
while c < 2:
    carta1= random.choice(embaralhar) #Escolheu aleatoriamente uma carta da lista
    carta2= random.choice(embaralhar) #Escolheu aleatoriamente uma carta da lista
    embaralhar.remove(carta1) #Removeu a carta do baralho
    embaralhar.remove(carta2) #Removeu a carta do baralho
    banco.append(carta1)
    jogador.append(carta2)
    c+=1

print(banco)
print(jogador)
print(embaralhar)

somab= 0
for soma in banco:
    somab+= soma
if somab > 9:
    somab= somab-10
print(somab)

somaj= 0
for som in jogador:
    somaj+= som
if somaj > 9:
    somaj= somaj-10
print(somaj)
