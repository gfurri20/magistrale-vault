Viene dato un eseguibile strippato, quindi senza simboli di debug.

L'analisi con ghidra del codice risulta, inizialmente, inutile.
Se si prova ad eseguire l'eseguibile si ottiene sempre un `segfault`.

Un informazione che sembra essere utile è una variabile globale che punta ad una lista di byte, analizzando il codice assembly ad ogni chiamata ricorsiva tale lista viene iterata.

Attraverso un'analisi dell'esecuzione posso estrarre la lista di byte:
```python
bytes = [ 0x54, 0xc3, 0x122, 0x18b, 0x1df, 0x244, 0x2b6, 0x2ea, 
	0x35e, 0x3c3, 0x422, 0x48b, 0x4c0, 0x51f, 0x587, 0x5dc,
	0x649, 0x6aa, 0x6f8, 0x757, 0x7cb, 0x7fb, 0x85a, 0x8cc, 0x8ff,
	0x942, 0x9b7, 0xa09, 0xa7c, 0xae1, 0xb40, 0xba4, 0xbd5, 0xc4b,
	0xcb4, 0xd22, 0xd87 ]
```

Si nota subito che è una lista di numeri crescenti.

Sempre analizzando l'esecuzione del codice assembly attraverso gdb si nota che ad un certo punto viene fatta la **somma** tra il valore presente in `eax` e un valore contenuto nello `stack`.

Successivamente viene fatta la `cmp` tra il valore precedentemente calcolato e il rispettivo byte nella lista sopra-riportata.

Quindi tale deduzione ci permette di capire che il carattere i-esimo della flag non è altro che la differenza tra il byte (i+1)-esimo e il byte i-esimo della lista di bytes:
$$\texttt{flag[i] = chr(bytes[i] - bytes[i - 1])}$$
Quindi partendo da 0:
$$\texttt{flag[0] = chr(0x54 - 0x00) = "T"}$$
$$\texttt{flag[1] = chr(bytes[1] - bytes[0]) = chr(0xc3 - 0x54) = chr(0x6f) = "o"}$$
Iterando tale processo e aggiungendo il prefisso classico si ottiene la flag:
$$\texttt{ CCIT\{To\_iTer4te\_i5\_hUmaN\_t0\_r3CuRse\_d1vine\} }$$

Codice python3 per la risoluzione:

```python
bytes = [ 0x54, 0xc3, 0x122, 0x18b, 0x1df, 0x244, 0x2b6, 0x2ea, 
			 0x35e, 0x3c3, 0x422, 0x48b, 0x4c0, 0x51f, 0x587,
			 0x5dc, 0x649, 0x6aa, 0x6f8, 0x757, 0x7cb, 0x7fb,
			 0x85a, 0x8cc, 0x8ff, 0x942, 0x9b7, 0xa09, 0xa7c,
			 0xae1, 0xb40, 0xba4, 0xbd5, 0xc4b, 0xcb4, 0xd22,
			 0xd87 ]

flag = "CCIT{" + chr(bytes[0])

for i in range(0, len(bytes) - 1):
    current = chr(bytes[i + 1] - bytes[i])
    flag += current

flag += "}"

print(flag)
```

