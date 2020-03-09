# Troca
Resolução da questão 'troca' da fase 3 do ano de 2018.

## Resolução 
Esse problema consiste em receber vários intervalos que indicam os índices das cartas que devem ser viradas, e, a partir deles, descobrir para cada carta se no final ela estará virada para cima ou para baixo. Para isso, basta percorrer por todas as cartas e guardar para cada uma quantos intervalos estão ocorrendo no momento. Se o número de intervalos for par, a carta terminará virada para cima, terminando do mesmo jeito que começou. Caso o número de intervalos seja ímpar, ela terminará virada para baixo. A classe Carta guarda seus dois valores, quantos intervalos iniciaram nela e quantos terminaram na mesma. Após criar todas as cartas a partir dessa classe, atribue-se 0 a variável intervalo e o programa percorre cada carta, somando 1 sempre que um intervalo é iniciado, e subtraindo-se 1 quando um intervalo se encerra.
