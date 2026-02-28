# My-Galgos-Task

Neste projeto estaremos explorando uma possivel solucao para o problema do caixeiro viajante, um problema NP-Dificil, ou seja, nao possui uma solucao eficiente conhecida.

Minha primeira ideia de como abordar o problema seria tentar utilizar um algoritmo eficiente que eu ja estou familiarizado, o A*. A ideia era selecionar um ponto inicial e um final para executar o algoritmo e depois explorar as possiveis combinacoes que proporcionam um caminho "aceitavel", depois rodar o algoritmo novamente utilizando o caminho reverso e as impondo restricoes necessarias. Mas depois percebi que em modelos muito grandes seria inviavel.

Entao comecei a procurar por outras solucoes, como o algoritmo guloso do Vizinho mais proximo, dado que eu li que uma abordagem Heuristica ou Meta-heuristica no meu caso seria a mais eficaz. Mas eu gostaria de usar uma solucao mais sofisticada, o que me deu a ideia de combinar algoritmos como Held-Karp e Colonia de Formigas.


