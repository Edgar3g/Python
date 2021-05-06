import random
frutas = ['Banana', 'Maçã', 'Uva', 'Limão', 'Laranja', 'Pera', 'Mamão'];
tentativas_validas = 6;

minha_escolha = random(frutas)

jogador = None

print('*********************+++++++++++++********')     
print('*    Adivinhe a minha Fruta Favorita     *')     
print('******************************************')
print(f'\n\n{frutas}')
while jogador != minha_escolha:
    jogador = input('\n\nQual a minha fruta?: ')
