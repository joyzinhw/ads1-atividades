import random
print('''        Vamos jogar 21

Regras:
1 - serão distribuídas 3 catas para cada um dos jogadores 
2 - Aquele que tiver a pontuação mais próxima ou igual a 21 ganha
3 - cada carta tem como pontuação seu próprio número ou valor
4 - Se passar de 21 (estourar) o jogador perde
''')
Cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
VCartas = {'A': 1, 'J': 1, 'Q': 1, 'K': 1}
nipes = ['paus', 'copas', 'ouro', 'espadas']
jogador1 = []
jogador2 = []
cartas1 = []
cartas2 = []
p1 = 0
p2 = 0
nome1 = str(input('Nome do primeiro jogador: ')).strip().title()
nome2 = str(input('Nome do segundo jogador: ')).strip().title()
while len(cartas1) < 3:
    vc = random.choice(Cartas)
    On = random.choice(nipes)
    enipe = str('{} de {}'.format(vc, On))
    if enipe in cartas1:
        n = 0
    else:
        cartas1.append(enipe)
        if vc in VCartas:
            x = VCartas[vc]
            p1 = p1 + x
        else:
            p1 = p1 + vc
while len(cartas2) < 3:
    vc = random.choice(Cartas)
    On = random.choice(nipes)
    enipe = str('{} de {}'.format(vc, On))
    if enipe in cartas1:
        n = 0
    else:
        cartas2.append(enipe)
        if vc in VCartas:
            x = VCartas[vc]
            p2 = p2 + x
        else:
            p2 = p2 + vc
print('As cartas do  primeiro jogador ({}) foram: {}'.format(nome1, cartas1))
print('As cartas do segundo jogador ({}) foram: {}'.format(nome2, cartas2))
print('A pontuação do primeiro jogador ({}) foi: {}'.format(nome1, p1))
print('A pontuação do segundo jogador ({}) foi: {}'.format(nome2, p2))
if p1 > 21 and p2 > 21:
    print('Os dois estouraram!')
elif p1 == p2:
    print('Empataram!')
elif p1 == 21 and p2 > 21:
    print('O primeiro jogador ({}) ganhou! O segundo ({})... estourou.'.format(nome1, nome2))
elif p2 == 21 and p1 > 21:
    print('O Segundo jogador ({}) ganhou! O primeiro ({})... estourou.'.format(nome2, nome1))
elif p1 == 21 and p2 < 21:
    print('O primeiro jogador ({}) ganhou! O segundo ({})... perdeu.'.format(nome1, nome2))
elif p2 == 21 and p1 < 21:
    print('O Segundo jogador ({}) ganhou! O primeiro ({})... perdeu.'.format(nome2, nome1))
elif p1 < 21 and p2 < 21:
    a1 = 21 - p1
    a2 = 21 - p2
    if a1 < a2:
        print('O primeiro jogador ({}) ganhou! O segundo jogadror ({})... perdeu.'.format(nome1, nome2))
    else:
        print('O segundo jogador ({}) ganhou! O primeiro jogador ({})... perdeu.'.format(nome2, nome1))