class Carta:
    def __init__(self, cima, baixo):
        self.ini = 0 # quantas vezes começaram a virar as cartas a partir dessa
        self.fim = 0 # quantas vezes terminaram de virar as cartas nessa carta
        self.cima = cima # valor de cima
        self. baixo = baixo # valor de baixo

N, T = list(map(int, input().split(' '))) # N numero de cartas, T numero de intervalos
cima = input().split(' ') # valores na parte debaixo da carta
baixo = input().split(' ') # valores na parte de cima

cartas = []
for i in range(N):
    cartas.append(Carta(int(cima[i]), int(baixo[i])))

for i in range(T):
    intervalo = input().split(' ') # vetor com o inicio e fim do intervalo
    cartas[int(intervalo[0]) - 1].ini += 1 
    cartas[int(intervalo[1]) - 1].fim += 1

intervalos = 0 # indica a combinação de incio e fim atual (quantos intervalos foram iniciados - quantos foram encerrados)
for i in range(N):
    intervalos += cartas[i].ini
    # intervalos impar indica que esta carta deve virar, por isso deve-se pegar o valor de baixo
    if intervalos % 2:
        print(cartas[i].baixo, end=' ')
    else:
        print(cartas[i].cima, end=' ')
    intervalos -= cartas[i].fim
