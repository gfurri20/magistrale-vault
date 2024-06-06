Approfondiremo l'architettura x86.

Il codice ad alto livello è tradotto in linguaggio macchina attraverso il compilatore.

Ques'ultimo produrrà una sequenza di byte che verrà interpretata come codice.
Un disassembler è un tool che permette di passare dalla sequenza di bytes al codice in linguaggio macchina.

Due possibili annotazioni dei valori:
- **little endian** - LSB sarà contenuto nell'indirizzo di memoria più basso ("al contrario")
- **big endian** - MSB nell'indirizzo di memoria più basso ("as is")

Flags:
- **ZF** - settato quando otteniamo 0 da qualsiasi operazione
- **CF** - settato quando si ottiene un riporto da un'operazione
- **SF** - settato quando si ottiene un risultato negativo (< 0)
- **TF** - a true quando il binario viene eseguito in un debugger

La sintassi `[eax]` permette di recuperare il valore contenuto nell'indirizzo di memoria specificato in `eax`.

Non si può copiare un valore tra aree di memoria: ~~`mov [...], [...]`~~

L'istruzione `lea` - Load Effective Address, copia l'indirizzo non il valore puntato dall'indirizzo.

Esercizio:
```asm
mov dword ptr [ebp-4], 1
mov eax, dword ptr [ebp-4]
mov dword ptr [ebp-8], eax
```
$$\downarrow$$
```c
int a = 1;
int b = a;
```

`dword` fa riferimento a valori a 32 bit, mentre `qword` a 64 bit.

Altro esercizio:
```c
int a = 22
int b = 5
int c = a + b
int d = a - b
```

In realtà il codice assembly non contiene le dichiarazioni, quindi non sarebbero propriamente da mettere.