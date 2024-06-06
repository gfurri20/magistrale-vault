# Ottimizzazione di `prev_and_next`
L'algoritmo scritto la volta scorsa in realtà è quadratico perché python scorre la lista durante la concatenazione.

Risolviamo, modificando in questo modo la soluzione:

```python
def next_piastrelle(inst, config) -> bool:
	if len(inst) == 0:
		return False
	if inst[0] == 1:
		valid_length = len(config)
		config.append(inst[0])
		exists = next_piastrelle(inst[1:], config)
		if exists:
			return True
		else:
			del config[valid_length:]
			len_bagno = sum(inst)
			if len_bagno < 2:
				return False
			config.append(2)
			for i in range(len_bagno - 2):
				config.append(2)
			return True
	elif inst[0] == 2:
		exists = next_piastrelle(inst[1:], confing)
		return exists
	# configurazione non è valida (MAI)
	return False

def prev_piastrelle(inst, config):
	...
```

---

# Soluzione di `poldo_mania`

 > ss = sotto-sequenza (sintassi che piace al bianco)

Dobbiamo trovare la sotto-sequenza maggiore più lunga.
`3 7 2 9 4 5 8`

Provare tutte le possibili combinazioni

Parte dal fondo e si chiede qual'è la ss più lunga che inizia con il numero puntato
	- 8 -> solo 1, sè stesso
	- 5 -> 2, prende lui e 8
	- 4 -> 3
	- 9 -> 1
	- 2 -> 4 elementi
	- 7 -> 2, prende 2 e 9
	- 3 -> 4

Inoltre bisogna salvare le ss a cui fanno riferimento ogni numero:
3 --> 4 perché prende il numero 4 --> 3 (3 + 1 = 4)

Il terzo approccio (in $nlog(n)$).
Si parte da un array vuoto che risponde ad una domanda:

Si parte dalla fine e ci si chiede qual'è il minimo numero che se preso può dare una ss di dimensione i (con i che indica la posizione):
- il primo è 8 --> `[1:8, 2:None, ...]`
- passiamo a 5, può aggiungersi o sostituire --> `[1:8, ]`
		Per farlo facciamo ricerca binaria sul nostro array e vediamo dove metterlo
		`[1:8, 2:5]` lo mettiamo in 2 perché è minore di 8 e ci può creare una ss
- passiamo al 4 --> stesso ragionamento `[1:8, 2:5, 3:4, ...]`
- passiamo al 9 --> con la ricerca binaria scopriamo che va sulla pos 1
		`[1:9, 2:5, 3:4, ...]`
- passiamo al 2 --> ricerca binaria `[1:9, 2:5, 3:4, 4:2]`
- tocca al 7 --> ricerca binaria `[1:9, 2:7, 3:4, 4:2]`, va a sostituire il 5
- 3 --> ricerca binaria `[1:9, 2:7, 3:4, 4:3]
- aggiungiamo un 5 davanti -->  `[1:9, 2:7, 3:5, 4:3]`

L'array costruito ci dice che il più grande numero che può essere usato per far partire una ss di dimensione 4 è il numero 3, eccetera.

Come recuperare la ss però? Riscriviamo l'algo con questa aggiunta (array ausiliario che collega gli elementi)
- partiamo da 8 -> è solo uno `[8->+inf]`
- siamo su 5 -> sappiamo che il 5 è preso da 8, mettiamo allora una freccia `[8->+inf, 5->8]`
- siamo su 4 -> stessa storia `[8->+inf, 5->8, 4->5]`
- siamo su 9 -> 
- siamo su 2 -> prende il valore dal 4 `[8->+inf, 5->8, 4->5, 2->4]`
- siamo su 7 -> prende il valore dal 9 `[9->+inf, 8->+inf, 7->9, 5->8, 4->5, 2=4]`
- siamo su 3 -> `[9->+inf, 8->+inf, 7->9, 5->8, 4->5, 2->4, 3->4]`
- aggiungiamo un 5 finale tanto per -> `[9->+inf, 8->+inf, 7->9, 5->7, 4->5, 2->4, 3->4]`

Il link è sull'elemento precedente dell'inserzione sul primo array.

Infine prendiamo l'ultimo elemento del primo array e seguiamo le frecce! Otteniamo così la ricostruzione.

Le frecce che non danno la ss più lunga non sono inutili perché non sappiamo effettivamente qual'è la più lunga, finché non si finisce.

---

## Analisi della complessità di un problema

Generalmente un PC fa dalle 10-100 milioni di operazioni al secondo --> $\frac{10^{7/8} \texttt{ operazioni}}{1 \texttt{ secondo}}$

Esempio con `n = 20`
- $n!$ - algoritmo che deve provare tutte le combinazioni
- $2^n$ - prova tutti i sottoinsiemi
- $n^4$ - su 20 elementi in realtà non è un problema

| Istanza     | $n!$ | $2^n$ | $n^4$ | $n^3$ | $n^2$ | $nlog(n)$ | $n$ |
| ----------- | ---- | ----- | ----- | ----- | ----- | --------- | --- |
| ~11/12      | ✅    | ✅     | ✅     | ✅     | ✅     | ✅         | ✅   |
| ~20         | ❌    | ✅     | ✅     | ✅     | ✅     | ✅         | ✅   |
| ~60         | ❌    | ❌     | ✅     | ✅     | ✅     | ✅         | ✅   |
| ~220        | ❌    | ❌     | ❌     | ✅     | ✅     | ✅         | ✅   |
| ~3000       | ❌    | ❌     | ❌     | ❌     | ✅     | ✅         | ✅   |
| ~2000000    | ❌    | ❌     | ❌     | ❌     | ❌     | ✅         | ✅   |
| ~$10^{7/8}$ | ❌    | ❌     | ❌     | ❌     | ❌     | ❌         | ✅   |

Il tempo lineare funziona è praticamente il meglio perché banalmente stiamo leggendo l'input, quello ci blocca.

---

# Somme prefisse
Molti problemi si risolvono utilizzando strutture dati che permettono di salvare dati utili ausiliari.

Supponiamo di avere due array con dei valori:
`a = [1,  4,  7, 9,  0, 2]`
`b = [9, 10, 13, 9, 11, 9]`

Il primo mantiene dei valori qualsiasi, il secondo mantiene, per ogni valore del primo array, la somma tra il valore massimo alla sua sx il valore massimo alla sua dx:
- 1 -> 0 + 9
- 4 -> 1 + 9
- eccetera

Come troviamo `b`?

L'idea è quella di farsi un array che calcola i massimi partendo dalla fine.
Successivamente scorro dall'inizio, sapendo che il massimo a sinistra sarà il numero precedente maggiore, mentre a destra pesco dall'array creato.

Questo algoritmo gira in tempo lineare.

La struttura dati si chiama **massimi suffissi**, ovvero una lista di numeri in cui ogni valore è il risultato dell'operazione associato ai precedenti.

==Le funzioni più utilizzate per creare i suffissi o prefissi sono il massimo, il minimo e la somma.==

Supponiamo di avere un array statico:
`[1, 4, 7, 9, 0, 2]`
e vogliamo sapere la somma nel range `[4, 7, 9]`.

Possiamo fare dei calcoli iniziali ma ad ogni query di range dobbiamo rispondere subito, senza ricalcolare.

Creiamo la seguente struttura dati (somma cumulativa):
`[1, 5, 12, 21, 21, 23]`

Dato un range `[1:4]` possiamo sottrarre l'ultimo numero compreso nel range con il primo numero escluso a sinistra dal range.

Se si cambia un valore nel primo array allora bisognerebbe aggiornare ad ogni update, quindi il primo algoritmo funziona solamente in caso di array di partenza statici.

Ci sono però algoritmi in tempi $nlog(n)$ per gestire anche l'update dell'array.




