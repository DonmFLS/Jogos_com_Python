import advinhacao
import forca

print('Escolha seu jogo:  ')

jogo = int(input(print(' 1 - Forca \n 2 - Adivinhação')))

if jogo == 1:
    print('Jogo da Forca')
    forca.jogar_forca()
elif jogo ==2:
    print('Jogo da Advinhação')
    advinhacao.jogar_advinhacao()