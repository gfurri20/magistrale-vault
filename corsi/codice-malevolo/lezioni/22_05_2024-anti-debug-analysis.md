Ovviamente ci sono diverse tecniche per evitare (o rendere più complessa) l'analisi del malware:
- **anti-debugging**
- **anti-disass**
- **anti-VM**
- **anti-sandbox**

# Anti-Debugging tecniques
L'obiettivo è quello di rendere inutile il debug del malware.

Si possono usare svariate tecniche:
- Per rilevare la presenza del debugger si utilizzano apposite API. Ovviamente è facilmente rilevabile guardando gli *imports*.
- Inoltre esiste una struttura usata dal loader del SO per caricare il programma, quando si usa il debugger è quest'ultimo che funge da loader.
- Altra tecnica è quella di capire chi è il parent che ha lanciato il malware, se il loader è il debugger allora il malware
- è possibile cercare tra le finestre aperte per capire se è aperto in quel momento un debugger noto.
- altra tecnica è quella di capire quanto tempo passa tra l'esecuzione di un'istruzione e un'altra, per valutare l'intervallo di esecuzione. In questo modo si capisce se è in corso debugging.
- altra tecnica ancora è la ricerca di breakpoints, l'istruzione breakkata viene sostituita da `int 3`; quindi basterebbe controllare la presenza di tale istruzione per capire di essere debuggati (alcuni compilatori la inseriscono in compilazione -> falsi positivi).
- se il malware lancia un debug su se stesso permette di evitare il debugging esterno.

## PEB (Process Block Environment)
Esso contiene informazioni sul processo che viene eseguito correntemente.

Quando viene eseguito il Thread di un programma viene creato il PEB.

Il 30-esimo byte punta alla struttura TEB, quest'ultimo contiene tre flag:
- **BeingDebugged** - offset 0x2 (se 0 NON c'è il debugger se no c'è)
- **ProcessHeap** - 0x18
- **NtGlobalFlag** - 0x68

API utili per capire la presenza di debug:
- `IsDebuggerPresent` - controlla la flag BeingDebugged
- `CheckRemoteDebuggerPresent` - come quella sopra ma controlla anche altri processi

Per controllare la flag BeingDebugged si può anche NON usare le API, ma semplicemente esaminando la struttura "manualmente".

La **NtGlobalFlag** contiene la somma tra altre tre flag, se il valore raggiunge `0x70` allora vuol dire che il software sta venendo debuggato.

Ci sono altre due flag settate insieme alla **NtGlobalFlag**:
- Flags - offset 0x40 -> assume 0x0002 se debuggato
- ForceFlag - offset 0x44 (o 0x10) -> assume $\neq$ 0x0 se debuggato
Per trovarle bisogna accedere al PEB, calcolare l'offset 0x18 e poi si accede alle due flag sopra-riportate (??)

---
## FindWindowAPI

Un'altra API utile è la `FindWindowAPI` che restituisce l'`Handle` della finestra di primo livello il cui nome corrisponde a ciò passato come parametro.

Se il primo parametro è `NULL`, cerco tutte le finestre con nome passato come secondo argomento.

(Cercare sulla doc. ufficiale di Win)

---
## Ricerca `int 3`
Si possono cercare le istruzioni `int 3` -> `0xCC`.

---
## Registro EFLAGS
Il registro EFLAGS raggruppa le flag per ogni suo bit.
Il malware può salvare il trap flag con una `pushf` sulla cima dello stack e poi analizzarlo con una pop.

Se è 0 allora è debuggato.

---
## Controllo basato sul tempo
Controllo l'intervallo di tempo tra l'esecuzione di una istruzione e l'altra attraverso:
- `rdtsc` - istruzione macchina che restituisce il numero di cicli di clock dall'avvio della macchina
- `GetTickCounter` - API che fa la stessa roba ma è una API

Calcoliamo inizio e fine e sottraiamo tra l'esecuzione di una istruzione all'altra.

Se il risultato è elevato rispetto ad una tresh-hold allora si può dedurre la presenza di un debugger. 

---
## Eccezioni
Altra tecnica, analisi delle eccezioni.

Quando viene generata una eccezione, essa deve essere gestita da una specifica funzione.
Quest'ultima si trova all'inizio del TEB.

La lista in TEB viene scandita e viene eseguita la **prima funzione** preposta per la gestione dell'eccezione.

Si può modificare il puntatore alla funzione che viene usata per gestire le eccezioni con una funzione che esegue il controllo di anti-debugging.

Si può fare perché vengono specificati:
- exception_record
- context_record - copia dei registri

Gli attaccanti:
1. modificano l'indirizzo della funzione di gestione delle eccezioni
2. triggerano una eccezione
3. a questo punto verrà eseguita la funzione di anti-debugging

La funzione di callback:
- recupera il la struttura che contiene i valori di registro
- Eseguo l'OR con i registri di HW breakpoint
- se c'è almeno un 1 (quindi valore diverso da 0) allora il malware è eseguito in un debugger

---
## TLS Callback
Sono delle routine che vengono eseguite prima che il debugger raggiunga l'entrypoint (prima istruzione della sezione `.text`).

Tipicamente inizializzano dei dati prima dell'esecuzione del codice.
Possono essere usate per implementare codice di anti-debugging.

Il vantaggio è che possono essere facilmente individuabili attraverso l'analisi statica (esisterà una sezione `.tls`).

---
# Esericizi
`Chapter16 > Lab16-01.exe`

Dall'analisi statica non sono state individuate API per il reckoning del debug.

Passiamo ad IDA e cerchiamo dei controlli di anti-debugging, il main sembra eseguire una catena di 3 controlli per trovare il debugger:
1. controlla il **BeingDebugged** --> se uguale a 0 non c'è debug
2. controlla il **ProcessHeap**
	1. all'offset 0x10 controlliamo il **ForceFlag** -> se uguale a 0 non c'è debug
3. controlla la **NtGlobalFlag** -> se diverso da 0x70 non c'è debug

Se una di queste NON mostra un eventuale debugger allora si prosegue se no viene eseguita una specifica funzione: `sub_401000`.

Passiamo a x32dbg e mettiamo un breakpoint sulla prima istruzione dei controlli.

Quando questa istruzione viene eseguita andiamo sul registro `eax` e facciamo follow in dump e lo metto a 0, in modo da eludere il malware.

Facciamo così anche per **ForceFlag**.

Per **NtGlobalFlag** andiamo a modificare la memoria inserendo 0x0 al posto di 0x70.
In questo modo otteniamo una differenza diversa da 0x0.

Così bypassiamo anche questo controllo.

Se non riuscissimo a superare i controlli?
Viene eseguita la funzione: `sub_401000`.

Tale funzione estrae il proprio nome, e si cancella eseguendo il comando su cmd:
`cmd.exe /c del <malware_shortpath> >> NUL`.

- `cmd.exe /c` serve per killare cmd una volta eseguito il comando
- `>> NUL` permette di silenziare l'output a schermo





