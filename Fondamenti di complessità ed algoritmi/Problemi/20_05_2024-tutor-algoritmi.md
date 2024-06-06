La scorsa volta abbiamo visto le somme (o differenze) prefisse, strutture dati utili per la risoluzione di determinati problemi.

Noi vogliamo che la cella il posizione i-esima contenga la somma dei primi i elementi. (somme o differenze cumulative).
Questo era stato fatto su liste statiche, sarebbe utile capire come farlo su liste dinamiche.

Ciò si fa una struttura dati chiamata **fenwick-tree**.

# Fenwick Tree
Supponiamo di avere un array iniziale (indice iniziale 1):
$$\texttt{[3, 4, 2, 8, 0, 7, 9, 0, 2, 1, 2]}$$
Costruiamo un'altro array tale che:
1. guardiamo la posizione dell'elemento corrente
2. contiamo il numero di fattori due che possiede la posizione $x$
3. troviamo $2^x$, ovvero il numero di caselle precedenti da comprendere nel calcolo della somma cumulativa (compresa la casella corrente)
4. si passa al prossimo numero

Si possono velocizzare le query lavorando con numerazione binaria.
Man mano, cancellando i bit, si possono ottenere i valori che compongono il numero di partenza.

Quando arriviamo a 0 sappiamo che è finito (per questo partiamo da 1).

Come fare ad aggiornare?
Supponiamo di voler aggiornare il terzo elemento: `00000011`:
- prendo l'ultimo bit significativo e sommo al numero stesso -> `00000100`
- stessa cosa -> `00000100 + 00000100 = 0001000`
Ci fermiamo quando il numero ottenuto è maggiore di quello della lunghezza dell'array iniziale.

---

Supponiamo di voler trovare il numero rappresentato da una sequenza binaria, in questo caso: `0001001101000`.

1. facciamo il not bit a bit -> `1110110010111`
2. se sommiamo 1 a questo numero: tutti i numeri diventano 0 finché non si arriva al primo 0 -> `1110110011000`
3. ora facciamo l'and bit a bit tra i due numeri sopra -> `0000000001000`

Il numero trovato viene fatto:
- la sottrazione nella query
- la somma nell'update

pd sto coglione parla velocissimo

---

Codice per lavorare sul numero in C:
```c
// Per numeri signed
x -= x & -x // query
x += x & -x // update
```

```c
// Per numeri unsigned
x -= x & (!x + 1) // query
x += x & (!x + 1) // update
```

```python
def update(f:list, i:int, amount:int) -> None:
	while i < len(f):
		f[i] += amount
		i += i & -i

def query(f:list, i:int) -> int:
	# init a 0
	r = 0
	while i > 0:
		r += f[i]
		i -= i & -i
	return r
```

> [!info] min/max
> Se volessimo trovare il min o max, allora bisogna impostare r, rispettivamente, a +inf o -inf.

Nel caso del massimo gli elementi possono solo aumentare e viceversa con il minimo.

## Applicazione a LIS
"Vogliamo sapere in tempo log il valore più grande tale per cui i valori davanti sono minori".

Abbiamo l'array di partenza:
1. ordinare tutti gli elementi e tenersi traccia delle posizioni (per ogni numero anche se si ripetono)
$$\texttt{a = [3, 4, 2, 8, 0, 7, 9, 0, 2, 1, 2]}$$
$$\texttt{ord = [0, 0, 1, 2, 2, 3, 4, 7, 8, 9]}$$
$$\texttt{pos = [4, 7, 9, 2, 8, 0, 1, ...]}$$
2. per ogni cella dell'array dobbiamo capire dove è andata a finire, usiamo un array di reverse index (dove prima abbiamo indice valore otteniamo valore indice, usiamo l'array $\texttt{pos}$ per fare ciò)
$$\texttt{pos\_reverse\_index = [3, 4, 2, 0, , , 0, 2, 1]}$$
Poi ha rushato e ho perso tutto diobosco.

... roba ...

Nel reverse index abbiamo dei valori che indicano la massima sottosequenza che possiamo ottenere utilizzando il numero indicato dalla posizione.

---

Poldo con fenwick:
```python
N = 8
A = [1, 5, 3, 4, 5, 6, 9, 2]

fenwick = [0] * (N + 1)

def query(F:list, i:int) -> int:
	val = 0
	while i > 0:
		val = max(val, F[i])
		i -= 1 & -i # cala
	return val

def update(F:list, i:int, x:int) -> None:
	while i < len(F):
		F[i] = max(F[i], x)
		i += i & -i # cresce

# array che implementa il reverse index
I = [(A[i], i) for i in range(N)]
I.sort()

# ora calcoliamo il valore trasposto
T = [0] * N

for i in range(len(T)):
	T[I[i][1]] = i + 1

print(T)
# -> [1, 5, 3, 4, 6, 7, 8, 2]
# l'array da un punteggio a questi numeri, dal più piccolo al più
# grande, crescente.
# stiamo rimappando i valori da un range più grande ad un range più
# piccolo e gestibile

S = [0] * N

# quadratico
for i in reversed(range(N)):
	max_seq = 0
	for j in range(i + 1, N):
		if A[i] < A[j]:
			max_seq = max(max_seq, S[j])
	S[i] = max_seq + 1

print(S)
print(max(S)) # soluzione di poldo vanilla

# lineare

# array che implementa il reverse index
I = [(-A[i], i) for i in range(N)]
I.sort()

for i in reversed(range(N)):
	max_seq = 0
	S[i] = query(F, T[i]) + 1

	# stampo gli elementi del fenwick
	print("FEN IDX: ", [k for k in range(1, N + 1)])
	# print("   ORIG: ", [S[k] for k in range(N)])
	# array originario su cui si fanno i massimi prefissi
	print(" ORIG T: ", [S[I[k][1]] for k in range(N)])
	# array di fenwick
	print("FENWICK: ", [query(F, k) for k in range(1, N + 1)])
	print(f"Update position {T[i]} to value {S[i]}")

	update(F, T[i], S[i])
	
print(S)
print(max(S)) # soluzione di poldo vanilla
```

DAJE