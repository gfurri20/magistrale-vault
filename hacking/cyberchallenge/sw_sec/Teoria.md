<small>Martedì 5 marzo 2024</small>

Il linking può essere statico o dinamico:
- statico -> le librerie vengono incluse (maggiore spazio occupato)
- dinamico -> le librerie NON vengono incluse

Per eseguire più programmi "simultaneamente" si usa la memoria virtuale in modo da andare a dividere la memoria in pagine, ovvero unità di dimensione specifica.

Il linux si usa il formato ELF, è diviso in sezioni.
La sezione è una porzione di programma decisa a tempo di compilazione:
- data
- rodata -> read-only data
- bss
- text -> codice del programma
- ...
La memoria è divisa in segmenti, ovvero pagine di memoria nelle quali gli eseguibili vengono caricati.

La memoria di un processo si divide in parti (in realtà la RAM contiene tutti i processo ma grazie alla memoria virtuale sembra che ogni processo la possieda tutta):
- OS Kernel *$\downarrow$, allocata per il sistema operativo
- stack $\downarrow$, variabili automatiche delle funzioni
- heap $\uparrow$, variabili allocate run-time
- ...

Lo stack cresce verso il basso $\downarrow$ mentre l'heap cresce verso l'alto $\uparrow$.

Lo stack, oltre a mantenere le variabili automatiche, svolge un ruolo fondamentale per quanto riguarda le chiamate a funzione.

Se si riesce a modificare l'indirizzo di return è possibile che il programma si comporti in maniera diversa.

La chiamata funzione avviene attraverso un operatore `call`, l'invocazione di tale comando permette di salvare lo stack il return address (ovvero l'indirizzo attuale di esecuzione).
La calling convention di x86 (32 bit) prevede che gli argomenti vengano messi sullo stack in ordine, dal primo all'ultimo, infine viene messo il return address. Il valore di ritorno viene salvato nel registro `eax`, di solito.

In gergo la calling convention si chiama ABI (Application Binary Interface), essa dipende dal SO, architettura e versioni di librerie condivise (per questo si preferiscono quelle statiche, a volte).

> **glibc** - libreria che contiene le funzioni canoniche di C

E' fondamentale implementare una politica di **separazione dei privilegi**. In linux si utilizza una gerarchia ad anelli (e.g. ring 0 è il livelli del Kernel).
Per passare da un lv. di privilegio all'altro si utilizzano le *system call*.

La system call è un'istruzione particolare che permette di eseguire un'operazione "privilegiata" switchando il livello di privilegio in modo da poterla eseguirla effettivamente.
E.g.: per eseguire una scrittura su file è necessario chiamare una syscall `fwrite(...)`.

## Reverse Engineering

Su i file eseguibili possiamo svolgere due tipi di analisi:
- statica, analisi senza esecuzione
- dinamica, analisi eseguendo il file

> `pie`, (positional independent executable) - ovvero un eseguibile che può essere caricato in memoria a qualsiasi indirizzo (gli indirizzi cambiano da un'esecuzione all'altra)

Se un file è *dynamically linked* allora è necessario un interprete, questo perché il Kernel prima andrà ad eseguire il codice dell'interprete che permette di caricare tutti gli oggetti dinamici.

Per velocizzare alcune chiamate di sistema, in Linux, si usano le VDSO (rif. [VDSO](https://en.wikipedia.org/wiki/VDSO)), ovvero librerie integrate direttamente nel Kernel.

Tecnicamente il nome delle funzioni è inutile, basta sapere l'indirizzo.

Quando un file è *strippato* allora vuol dire che sono stati rimossi i simboli di debug.

La sezione `.init` è una porzione di codice invocata ancora prima del main e serve per eseguire istruzioni "introduttive".

De-compilare un eseguibile permette di ricavare il codice sorgente (non proprio tutto tutto e sicuramente non sempre).

## Analisi Dinamica
Analisi del programma durante la sua esecuzione.

Prima di partire con l'uso del debugger è possibile andare a rintracciare le chiamate di sistema che sono state invocate, si usa il comando `strace`.
Possiamo anche visualizzare le chiamate di libreria eseguite attraverso `ltrace` (ovviamente funziona solo per file linkati dinamicamente).
Entrambi i comandi si appoggiano alla syscall `ptrace`.

Le librerie dinamiche sono utilizzate in base alla priorità, quindi si possono caricare delle librerie alterate che poi verranno utilizzate dall'eseguibile (e.g.: `LD_PRELOAD`).
Questa tecnica è molto interessante perché permette di funzionare anche dopo che il file è stato modificato.

---

<small>Martedì 2 aprile 2024</small>

## Buffer Overflow
Attacco sfruttando la sovrascrittura dello stack a causa della mancanza di controlli.

Risulta facile andare a sovrascrivere il `return address`, ciò permette di andare ad eseguire codice alternativo.

Per proteggersi da un buffer overflow si può:
- controllare la dimensione del buffer direttamente nel codice
- stack canary - ciò permette di inserire valori sentinella prima del `return address`, sono valori casuali che vengono controllati per capire se l'input è stato alterato.

`pwntools` ha un comando che permette di mostrare le misure di sicurezza impiegate sull'eseguibile.

Il **canary** non protegge del tutto dal buffer overflow obv.

**Programma PIE vs. NoPIE**
PIE = Position Independent Executable, un programma è PIE se gli indirizzi non sono statici ma vengono assegnati dinamicamente ad ogni esecuzione. Nello specifico il programma viene caricato in un indirizzo scelto casualmente.

Una funzione può essere chiamata attraverso:
- indirizzo relativo, relativo all'indirizzo di caricamento
- indirizzo assoluto

Si dice `gadget` una funzione già scritta nel codice che permette di essere sfruttata in modo malevolo.

## Shell Code
Uno shell code permette di eseguire una vera e propria shell sul sistema attaccato.

Se riusciamo a controllare il buffer con un buffer overflow è possibile iniettare codice che dopo verrà puntato sostituendo il `return address`.

`pwntools` permette di creare shell code per le diverse piattaforme.

Ovviamente sta roba è praticamente impossibile da mettere in pratica su sistemi moderni, ciò a causa del cosiddetto `NX` (https://it.wikipedia.org/wiki/NX-bit).

## Format String
`printf` parsa la stringa in input per capire quanti placeholder (e quindi variabili) prendere in input. Ciò viene fatto a tempo di compilazione.

L'attaccante potrebbe essere in grado di aggiungere placeholder non effettivamente voluti per cercare di iniettare codice.

E' possibile sfruttare il placeholder `%n` per sovrascrivere indirizzi arbitrari di memoria.



