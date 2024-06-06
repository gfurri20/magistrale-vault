<small>Martedì 19 marzo 2024</small>

Problema "accensione" su rtal.

Procedo per casi sul numero di computer:
- tot. 1, allora l'unico computer è spento o è acceso e abbiamo un pulsante
	- `0` -> `1` premendo pulsante 1
	- `1` -> `1` non facendo nulla
- tot. 2, allora abbiamo due computer e 4 configurazioni iniziali possibili
	- `00` - \[2] -> `11` 
	- `01` - \[1] -> `11`
	- `10` - \[1] -> `00` - \[2] -> `11`
	- `11` - non faccio nulla
- tot. 3, allora abbiamo 8 configurazioni iniziali possibili
	- `000` - \[1,2,3\] -> `100 010 111`
	- `001` - \[2] -> `111`
	- `010` - \[3] -> `111`
	- `011` - \[1] -> `111`
	- `100` - \[2] -> `010` - \[3] -> `111`
	- `101` - \[1] -> `001` - \[2] -> `111`
	- `110` - \[1] -> `010` - \[3] -> `111`
	- `111` - non faccio nulla

Esempio del testo, totale 6 computer allora ci sarebbero $2^6 = 64$ configurazioni possibili, il testo ci da:
- `010100` - \[2] -> `100100` - \[5] -> `000110` - \[6] -> `111111`
	- \[1] => `x-----` divisori (1)
	- \[2] => `xx----` divisori (1,2)
	- \[3] => `x-x---` divisori (1,3)
	- \[4] => `xx-x--` divisori (1,2,4)
	- \[5] => `x---x-` divisori (1,5)
	- \[6] => `xxx--x` divisori (1,2,3,6)


---
<small>Martedì 26 Marzo 2024</small>

La chiave del problema sta nell'iniziare dall'interruttore `n`, grazie al fatto che i tasti vanno premuti in ordine l'ultimo pulsante dovrà essere premuto al massimo una volta.

Domanda: qual'è la complessità asintotica dell'algoritmo?

Prima soluzione possibile in classe:
```python
def class_solution(n, acceso):
    for i in range(len(n) - 1, -1, -1):
        if not acceso[i]:
            acceso[i] = True
            for j in range(i):
	            PRINT_DI_DEBUG(i, j) # per capire ciò che si ripete
		        if i % j == 0:
	                acceso[j] = not acceso[j]
```

Questa soluzione è la stessa che ho scritto nel file `accensione.py`.

Qual'è allora la complessità asintotica? Chiaramente $O(n^2)$ perché è presente un ciclo innestato.

**Come migliorare?**
Con una semplice analisi dei risultati ripetuti è possibile ricondurre le ripetizioni alla sommatoria di Gauss:
$$\sum_{i=1}^{n+1} i = \sum_{i=1}^{n} i + (n + 1) = \frac{n*(n+1)}{2} + (n+1) = \frac{n^2 + n + 2n + 2}{2} = ...$$
$$... = \frac{n^2 + 3n + 2}{2} = \frac{(n+1)(n+2)}{2} = O(n^2)$$
Otteniamo così una formula quadratica.

Bisogna trovare un modo ricorsivo per risolvere il problema e grazie al Master Theorem sarà possibile capirne la complessità asintotica.