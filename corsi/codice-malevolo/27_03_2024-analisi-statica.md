Analisi **statica** di malware Windows.

## Primo Malware - financial-xls
Bisognerà aprirlo con il tool: *pestudio* (tools > pestudio)

Subito si può capire che il file è stato impacchettato con UPX, leggendo il campo *signature*.

Analizzando gli *imports* si possono vedere le API importate, troviamo subito due librerie interessanti:
- LoadLibrary - si occupa di caricare la libreria
- GetProcAddress - restituisce l'indirizzo per eseguirla

Nelle *sections* osserviamo tre sezioni:
- UPX0
- UPX1
- .rsrc
Mancano .text, .data, .bss e altro. C'è qualcosa di strano.

Per UPX0 la *raw-size* è 0, quindi può indicare che verrà caricato in mem. per poi essere eseguito spacchettato.

Osserviamo le *strings* per cercare di capire il comportamento ma non si capisce molto di più.

Le *resources* evidenziano una risorsa dialog (finestra di dialogo con l'utente) che presenta lingua Russa (inhales in communism).

Spacchettiamolo sto malwerozzo diddio:
- `upx -d <percorso_file.exe> -o <file_output.exe>`

Sempre con *pestudio* apriamo il file spacchettato per analizzarlo.

Nelle *sections* i nomi normali si sono ripristinati anche se i permessi sono rimasti gli stessi.

Le *imports* sono molte di più, le funzioni segnalate sono:
- `GetDesktopWindow` e `FindWindow` - per interagire con l'utente attraverso UI
- `RegSetValue`, `RegCreateKey`, `RegDeleteValue`,... - per interagire con i registri
- API per creazione di connessione internet attraverso le socket, sono caratterizzate da un numero, ciò vuol dire che sono state chiamate attraverso il numero identificativo nel codice sorgente
- `VirtualAlloc` - per allocare memoria all'interno dello spazio del malware
- `WriteFile`, `DeleteFile` - per gestire i file sulla macchina
- `GetEnvironmentStrings` - per recuperare il valore delle variabili d'ambiente
- `TerminateProcess` - per terminare l'esecuzione di processi
- `Sleep` - tecniche di anti-debugging utili per evitare il riconoscimento
- `WinExec` - usata per eseguire codice
- `LoadLibrary` - già trovata prima per importare librerie

Le *strings* ora ci danno maggiori info:
- indirizzo IP, possibile un C2 server
- stringhe corrispondenti a chiavi di registro (e.g. ...Run, usata per raggiungere persistenza)
- codice HTTP
- directory probabilmente per salvare info
- nomi di file
- `C:\Windows\xpupdate.exe` - **potrebbe raggiungere i privilegi di admin?**
- messaggio per l'utente
Si può ipotizzare che il MW modifichi dei registri per raggiungere persistenza aggiungendo una chiave al registro `Run`.
Inoltre è possibili che contatti un server C2 per lo scambio di info e comandi.

Possiamo concludere che il MW tenta di
- guadagnare persistenza
- stabilire una connessione, potenzialmente con un server C2
- creare file e.g. `BraveSentry`

Sulla macchina Remnux possiamo usare `yara`:
`yara -w -s -m ~/Desktop/Samples/yara/rules/index.yar <file_upx>`

Questo ci permette di confermare che potrebbe creare connessione di rete.
L'autore specificato all'interno del file fa riferimento a colui che ha creato la regola.

La stessa analisi sul file spacchettato ci da maggiori informazioni:
- ci specifica il compilatore
- la stringa "Armadillo" potrebbe far riferimento all'omonimo MW

## Secondo Malware - Malware/other files/malware
Il file header sembra essere stato compilato nel 1992, ma credo sia una grande cazzata.
Dall'optional header si capisce che usa una GUI.

Nella parte *section* vediamo come le sezioni `BSS` e `.tls` abbiamo dimensione su disco di 0. (Il tls è codice che può essere usato come anti-debug).
In `.rsrc` sembra che vengano importati dei file scritti in Delphi.

Analizzando gli *imports* sembra che analizzi i tasti della tastiera implementando così un keylogger.
Sembra scrivere su file e caricare librerie runtime.

Analizzando le *strings* si individuano diversi tasti della tastiera, riferimenti a chiavi di registro, windows API importate, svariati dll.

Sembra essere un leylogger.

## Terzo Malware - Malware/Practical Analysis/BinaryCollection/Chapter1L
Nello specifico: Lab01-04

Il file sembra essere compilato nel 2019 (ma è fake perché il libro da cui è stato preso è del 2013 lol)

Nella sezione *resources* c'è un eseguibile che è possibile individuare anche nelle *sections*.

Nella sezione *imports* è presente una API per caricare risorse in memoria, ciò è compatibile con l'eseguibile individuato.

A runtime, il MW sembra caricare le dll in memoria per poi chiamarne le funzioni.

Il malware sembra instaurare connessioni di rete e modificare files.

Il binario malevolo interno è per windows perché inizia con `4D 5A`.

