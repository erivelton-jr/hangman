from random import choice
from palavras import palavra
from art import fases
jogo = choice(palavra)
forca = []
vidas = 0

for f in range(len(jogo)):
    forca += '_'

while True:
    print(forca)
    letra = input('Diga uma letra: ').lower()
    for pos in range(len(jogo)):
        if jogo[pos] == letra:
            forca[pos] = letra
    if letra not in jogo:
        print(fases[vidas])
        vidas += 1
    if vidas == 6:
        print('Você foi enforcado')
        break
    if '_' not in forca:
        print(f'PARABÉNS! Você ganhou\n'
              f'A palavra era {jogo.title()}')
        break


