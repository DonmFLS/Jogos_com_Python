import random as rd

def jogar_advinhacao():
     print('*****************')
     print('Jogo da Advinhação')
     print('*****************')
     numero_secreto = rd.randrange(1,101)

     pergunta = int(input(print('Qual nível de dificuldade gostaria? \n 1 - Fácil \n 2 - Médio \n 3 - Dificíl')))

     if pergunta == 1:
          total_ten = 15
     elif pergunta == 2:
          total_ten = 10
     else:
          total_ten = 5

     pontuacao = 1000



     for rodada in range(1,total_ten +1):

          print(f'{rodada} de {total_ten}')

          chute = int(input('Digite seu número:   '))

          print(numero_secreto)
          print(f'Sua pontuação: {pontuacao}')

          if(chute < 1 or chute > 100):
               print('Você deve digitar um número entre 1 e 100')
               continue

          acertou = chute == numero_secreto
          menor = chute < numero_secreto
          maior = chute > numero_secreto


          if acertou:
               print(f"Parabéns, você acertou, o número secreto é:  {numero_secreto} ")
               break
          elif menor:
               print(f'Você errou, seu número digitado foi menor que o segredo')
               pontos_perdidos = abs(numero_secreto - chute)
               pontuacao -= pontos_perdidos
               print(f'pontos: {pontuacao} ')
          elif maior:
               print(f'Você errou, seu número digitado foi maior que o segredo')
               pontos_perdidos = abs(numero_secreto - chute)
               pontuacao = pontuacao - pontos_perdidos


     print('FIM DO JOGO')





