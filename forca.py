import random as rd

def jogar_forca():
    imprime_ola()
    palavra_secreta = gera_palavra()
    captura_chute()
    acertos = inicializa_acertos(palavra_secreta)


    print(acertos)
    enforcou = False
    acertou = False
    erro = 0

    while not enforcou and not acertou:

        chute = captura_chute()
        letras_restantes = str((acertos.count('_') - 1))

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute,acertos, letras_restantes)
        else:
            print('Você errou!!!!')
            erro += 1
        print(erro)
        print(erro)

        enforcou = erro == len(palavra_secreta)  # Retorna um bool ->True
        acertou = '_' not in acertos  # Retorna um bool ->True

        if acertou:
            print('Parabêns, você ganhou!!!')
        elif enforcou:
            print('Você perdeu! FIM DE JOGO')
            print(f'A palavra era {palavra_secreta}')



def imprime_ola():
    print('*****************')
    print('Jogo da Forca')
    print('*****************')


def gera_palavra():
    frutas = open('frutas.txt', 'r')
    palavra_sortida = []

    for fruta in frutas:
        fruta = fruta.strip()
        palavra_sortida.append(fruta)

    frutas.close()

    gera_numero = rd.randrange(0, len(palavra_sortida))
    palavra_secreta = palavra_sortida[gera_numero].upper()
    print(palavra_secreta)
    return palavra_secreta


def inicializa_acertos(palavra):
    return ['_' for le in palavra]


def captura_chute():
    chute = str(input('Digite a letra:  ')).upper()
    chute = chute.strip()
    return chute


def marca_chute_correto(palavra_secreta, chute,acertos, letras_restantes):
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            print(f"Essa letra: \'{letra.upper()}'\nEstá na posição: {index}")
            acertos[index] = letra
            print(f'Ainda restam: {letras_restantes} tentativas')
        index = index + 1

    print(acertos)


