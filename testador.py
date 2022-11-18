import random as rd

#tentativa de criar um array

#def cria_array (palavra):
 #   nv_array =[]
  #  i = 1
   # while i <= len(palavra):

#        nv_array.append('_')
 #       print(i)
  #      print(nv_array)
   #     i += 1
#

#inteiros = [1,3,4,5,7,8,9]
#pares = [n for n in inteiros if n%2==0] # vai iniciar a lista com n PARA CADA número em inteiros QUE seja par
#for numero in inteiros:
 #   if numero % 2 == 0:
  #      pares.append(numero)

#print(pares)


#frutas = open('frutas.txt', 'r')
#palavra_secretass = []

#for fruta in frutas:
 #   fruta = fruta.strip()
  #  palavra_secretass.append(fruta)

#frutas.close()

#print(len('frutas.txt'))

#palavra_secreta = palavra_secretass[rd.randrange(1, len('frutas.txt'))].upper()

#print(palavra_secreta)

import random as rd

def jogar_forca():
    print('*****************')
    print('Jogo da Forca')
    print('*****************')

    frutas = open('frutas.txt', 'r')
    palavra_secretass = []

    for fruta in frutas:
        fruta = fruta.strip()
        palavra_secretass.append(fruta)

    frutas.close()

    palavra_secreta = palavra_secretass[rd.randrange(1, 44)].upper()

    print(palavra_secreta)
    print(len(palavra_secreta))


    enforcou = False
    acertou = False
    acertos = ['_' for letra in palavra_secreta]



    i = 0

    while not enforcou and not acertou:

        print(f'{acertos}')
        chute = str(input(f'Digite a letra:  ')).upper()
        chute = chute.strip()
        letras_restantes = str((acertos.count('_')-1))


        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    print(f"Essa letra: \'{letra.upper()}'\nEstá na posição: {index}")
                    acertos[index] = letra
                    print(f'Ainda restam: {letras_restantes} tentativas')


                index = index +1

            print(acertos)
        else:
            print('Você errou!!!!')

        i += 1
        enforcou = i ==len(palavra_secreta) #Retorna um bool ->True
        acertou = '_' not in acertos #Retorna um bool ->True

        if acertou:
            print('Parabêns, você ganhou!!!')
        elif enforcou:
            print('Você perdeu! FIM DE JOGO')





jogar_forca()