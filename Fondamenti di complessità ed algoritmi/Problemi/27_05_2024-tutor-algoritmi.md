## Problema `lists_alignment`

### Descrizione del problema
Date due liste $U$ e $D$ di interi, per ogni indice i si prende il minimo tra $U[i]$ e $D[i]$ e si calcola la sommatoria di questi valori:
$$val(U,D) = \sum_{i}min(U[i], D[i])$$

*es:* 
```
9 1 1 1 1
1 9 1 1 1

Value: 5
```

-> Il problema sta nell'eliminare da ogni lista zero o più elementi, ottenendo due nuove liste $U'$ e $D'$, in modo da *massimizzare* $val(U',D')$

*l'esempio quindi diventa:*
```
9 1 1 1
9 1 1 1

Value: 12
```

---

>[!info] Attenzione
>Verificare sempre quali sono i limiti delle Subtask.
>Può essere che una soluzione quadratica sia già sufficiente a risolvere il problema.

> [!info] ATTENZIONE
> Leggere sempre i Subtask: ci sono dei subtask `easy` in fondo alla lista di questo esercizio. Sono punti regalati!

---
### Problema propedeutico `edit_distance`
Date due stringhe `S1` e `S2`:
```
S1 = ACGTAA
S2 = ATAACC
```
Si vuole trovare il numero minimo di operazioni da eseguire per rendere le stringhe uguali.

In certi problemi, tali operazioni possono avere dei costi:
esempio:
- insert: 2
- delete: 2
- replace: 3
- equals: 0
(In questo esempio fare replace è più conveniente di fare insert e poi delete)

L'algoritmo più efficiente al momento ha complessità $n^2$.

La **soluzione** richiede l'uso di programmazione dinamica.
Si costruisce una tabella con
- colonne: corrispondono ai caratteri di `S1`
- righe: corrispondono ai caratteri di `S2`

Nella cella di colonna i e riga j si inserisce il costo per far diventare la stringa `S1[:i]` in `S2[:j]`

|             | `empty` | **A** | **C** | **G** | **T** | **A** | **A**  |
| ----------- | ------- | ----- | ----- | ----- | ----- | ----- | ------ |
| **`empty`** | 0       | 2     | 4     | 6     | 8     | 10    | 12     |
| **A**       | 2       | 0     | 2     | 4     | 4+2=6 | 6+2=8 | 8+2=10 |
| **T**       | 4       | 2     | 3     | 5     | 4     | 6     | 8      |
| **A**       | 6       | ...   | ...   | ...   | ...   | ...   | ...    |
| **A**       | 8       | ...   |       |       |       |       |        |
| **C**       | 10      | ...   |       |       |       |       |        |
| **C**       | 12      | ...   |       |       |       |       |        |
Si riesce a riempire la tabella abbastanza agevolmente guardando per ogni cella:
- la cella a sinistra per una eventuale *delete* (costo +2)
- la cella superiore per una eventuale *insert* (costo +2)
- la cella in diagonale (alto-sx) per una eventuale *replace* (costo +3)
cercando così ogni volta l'operazione con costo minimo.

*pseudo-codice di quella che sarebbe la ricorsione*
``` python

def f(S1, S2):
	if len(S1) == 0:
		return len(S2) * cost_insert
	if len(S2) == 0:
		return len(S1) * cost_delete
	return min(
		f(S1[1:], S2) + cost_delete,
		f(S1, S2[1:]) + cost_insert,
		f(S1[1:], S2[1:]) 
			+ cost_replace if S1[0]!=S2[0] else 0,
	)
```

---
### Soluzione del problema
Per risolvere il problema `lists_alignment` si segue lo schema risolutivo del problema `edit_distance`, costruendo una tabella simile e salvando per ogni cella, oltre al valore, anche la direzione (ovvero la cella) da cui siamo arrivati per ottenere quel valore (tecnica **backtracking**).

```
U =  1  7  4  9  2
D =  5  2 11  0  4

```

Costruiamo la tabella

|        | 1   | 7            | 4            | 9                           | 2                           |
| ------ | --- | ------------ | ------------ | --------------------------- | --------------------------- |
| **5**  | 1   | 5            | 5            | 5                           | 5                           |
| **2**  | 1   | 5 $\uparrow$ | 7 $\nwarrow$ | 7 $\leftarrow$ o $\nwarrow$ | 7 $\leftarrow$ o $\nwarrow$ |
| **11** | 1   | 8 $\nwarrow$ | 9 $\nwarrow$ | 16 $\nwarrow$               | 16 $\leftarrow$             |
| **0**  | 1   | 8            | 9            | 16                          | 16                          |
| **4**  | 1   | 8            | 12           | 16                          | 18                          |
*NB: non ho messo tutte le frecce*

Il valore ottimo in questo esempio è `18` e facendo backtracking con le direzioni salvate è possibile ricostruire la soluzione:
```
U' =  7  4  9  2
D' =  5  2 11  4

5 + 2 + 9 + 2 = 18
```

