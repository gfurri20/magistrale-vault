Per trovare la soluzione sarà necessario combinare diversi algoritmi tra loro.

Dato l'array `a`:
$$\texttt{a = [1, 7, 9, 0, 11, 4]}$$
se prendo `a[1]` non potrò prendere `a[1+1]` e `a[a+2]`.

La prima task consiste nel trovare il numero massimo di queste soluzioni.

Cerchiamo la risposta aggiungendo elementi ad un array vuoto e guardiamo quante soluzioni in due modi, quando l'elemento viene preso e quando non viene preso:
- n = 0 --> l'unica soluzione è $\emptyset$
- n = 1 --> numero di soluzioni è 1 + 1
- n = 2 --> 2
- n = 3 --> 3
- n = 4 --> <span style="color:#00b050">2 + 4</span>
- n = 5 --> posso prendere 5,2 ; 5,1 e 5. Se non lo prendo ho 6. In totale abbiamo 3+<span style="color:#00b050">6</span> soluzioni (il 6 è il risultato di sopra!!!!)
- n = 6 --> prendo 6,3 ; 6,2 ; 6,1 ; 6. Inoltre quando non lo prendo ho 9. Totale 4+9.
- n = 7 --> prendo 7,1 ; 7,2 ; 7,3 ; 7,4,1 ; 7. Nel caso 7,4,1 avrò che il n° di soluzioni è la somma tra il n° di sol. prendendo 7, n° sol. prendendo solo 4 e n° sol. prendendo solo 1. Seguendo la logica per ognuno avrò: ==6 + 13==.
- n = 8 --> stessa logica, 6+3+==19==.
- n = 9 --> avremmo 28 + 13

|              | 9   | 8   | 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n° preso     | 13  | 9   | 6   | 4   | 3   | 2   | 1   | 1   | 1   | 1   |
| n° non preso | 28  | 19  | 13  | 9   | 6   | 4   | 3   | 2   | 1   | 0   |


Quindi dato array lungo n il numero n-1 viene calcolato attraverso:
$$p(n-1) + q(n-2)$$
con $p$ che calcola il numero di soluzioni prendendo il numero e $q$ che calcola il numero totale di soluzioni per il numero precedente.

**Detto meglio**: per trovare il n° di sol. per n=9, bisogna sommare:
1. gli elementi del numero -3, quindi di 6: 4 + 9 = 13
2. gli elementi del numero precedente, quindi 9 + 19 = 28

In questo modo lo si in modo lineare!

---

Seconda e terza task: trovare il valore ottimo, ovvero la massima somma possibile.

Scorriamo l'array e per ogni numero salviamo il massimo tra la somma precedente oppure la soluzione che si ottiene prendendo quel numero:

| ==8==   | 1   | 12  | ==24==   | 11  | 4   | ==30== | 7   |
| ------- | --- | --- | -------- | --- | --- | ------ | --- |
| 8+54=62 | 54  | 54  | 24+30=54 | 30  | 30  | 30     | 7   |
Quindi la somma ottimale avviene prendendo 8-24-30.

Se ci ricordiamo i valori che abbiamo preso è facile ricostruire la soluzione (basterebbe tenere traccia con un array). Si dice che si fa "backtracking".

Un algoritmo del genere è lineare perché per ogni cella guardiamo al massimo due celle, un numero costante: $O(n) = O(n + c)$.

---

Quarta task: numero di soluzioni ottime

| 6   | 12  | 11  | 6   |
| --- | --- | --- | --- |
| 12  | 12  | 11  | 6   |
In questo esempio la soluzione ottima è 12.
Quanti modi ci sono per ottenere 12? Posso prendere il 12 che già c'era, oppure prendo il 12 che si forma da 5+7.

| 12  | 12  | 11  | 6   |                                                                        |
| --- | --- | --- | --- | ---------------------------------------------------------------------- |
| 2   | 1   | 1   | 1   | soluzioni ottime che danno il numero sopra dal suo indice all'indietro |
| A   | B   | C   | D   |                                                                        |
Sostanzialmente il risultato nella colonna A corrisponde alla somma tra le celle B e D.

---

E.g.: caso particolare, perché l'insieme vuoto deve essere considerato come soluzione ottima

| 0      | 0     | 0     | 0   | 0   | 0   | $\emptyset$ |                            |
| ------ | ----- | ----- | --- | --- | --- | ----------- | -------------------------- |
| 4+9=13 | 3+6=9 | 2+4=6 | 1+3 | 3   | 2   | 1           | numero di soluzioni ottime |


