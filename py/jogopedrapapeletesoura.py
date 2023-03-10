# Jogo do Pedra, Papel e Tesoura

import random
continuidade = 'SIM'
print(('__'*35))
print('''Você está jogando jokenpô''')
print(('__'*35))
print('''Para o caso de você não lembrar as regras:

1 - você terá de escolher entre PEDRA, PAPEL e TESOURA
2 - O computador também selecionará, os dois irão expor a escolha ao mesmo tempo
3 - Se as escolhar forem iguais, então temos um empate
4 - PEDRA ganha de TESOURA, TESOURA ganha de PAPEL, PAPEL ganha de PEDRA

O jogo começou:''')
print(('__'*35))
while continuidade != 'N':
    computador = ['PEDRA', 'PAPEL', 'TESOURA']
    random.shuffle(computador)
    jc = random.choice(computador)
    print('Digite: 1 - Pedra ; 2 - Tesoura ; 3 - Papel')
    print('')
    jogada = int(input('Qual a sua jogada?: '))
    print(('__'*35))
    if jogada == 1 and jc == 'PEDRA' or jogada == 2 and jc == 'TESOURA' or jogada == 3 and jc == 'PAPEL':
        if jogada == 1:
            print('Você escolheu Pedra e a jogada do computador foi: {}'.format(jc))
        elif jogada == 2:
            print('Você escolheu Tesoura e a jogada do computador foi: {}'.format(jc))
        elif jogada == 3:
            print('Você escolheu Papel e a jogada do computador foi: {}'.format(jc))
        print('')
        print('Empate!')
        print(('__'*35))
    elif jogada == 1 and jc == 'TESOURA':
        print('Você escolheu Pedra e a jogada do computador foi: {}'.format(jc))
        print('')
        print('Você ganhou!')
        print(('__' * 35))
    elif jogada == 2 and jc == 'PAPEL':
        print('Você escolheu Tesoura e a jogada do computador foi: {}'.format(jc))
        print('')
        print('Você ganhou!')
        print(('__' * 35))
    elif jogada == 3 and jc == 'PEDRA':
        print('Você escolheu Papel e a jogada do computador foi: {}'.format(jc))
        print('')
        print('Você ganhou!')
        print(('__' * 35))
    elif jogada == 1 and jc == 'PAPEL':
        print('Você escolheu Pedra e a jogada do computador foi: {}'.format(jc))
        print('')
        print('Você perdeu!')
        print(('__' * 35))
    elif jogada == 3 and jc == 'TESOURA':
        print('Você escolheu Papel e a jogada do computador foi: {}'.format(jc))
        print('')
        print('Você perdeu!')
        print(('__' * 35))
    elif jogada == 2 and jc == 'PEDRA':
        print('Você escolheu Tesoura e a jogada do computador foi: {}'.format(jc))
        print('')
        print('Você perdeu!')
        print(('__' * 35))
    else:
        print('{} não é uma jogada permitida!'.format(jogada))
        print(('__' * 35))
        n = str(input('Deseja continuar jogando? (S/N): ')).strip().upper()
        print(('__' * 35))
        if n == 'S':
            continue
        else:
            break
print(('__'*35))
print('O jogo foi encerrado ')
print(('__'*35))