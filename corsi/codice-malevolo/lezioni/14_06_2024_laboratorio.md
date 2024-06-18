
Analisi di PDF malevoli su `REMnux`
- `example1.pdf`
- `example2.pdf`

# example1.pdf

`exiftool example1.pdf`
non vediamo molto

`yara -w -s -m <rules_path>/index.yar example1.pdf`
c'è qualcosa di sbagliato nella struttura e vediamo sempre `Big_Numbers1`

`pdfid.py example1.pdf`
vediamo che c'è del codice javascript e la parola chiave OpenAction

`peepdf -i example1.pdf`
non funziona

`pdf-parser.py --search javascript example1.pdf`
Vediamo che c'è  un oggetto con parola chiave OpenAction
Vediamo inoltre il codice js di interesse, con un URL codificato in esadecimale. Possiamo decodificarlo con `CyberChef` usando la ricetta `from hex`. 

```
http://searchglobalsite.com/in.cgi?17
```

L'URL decodificato, una volta scansionato con `VirusTotal`, vediamo che è generalmente associato allo scaricamento di spyware.

---

# example2.pdf

`exiftool example2.pdf`
vediamo che è stato modificato nel 2016 ma manca la data di creazione

`yara -w -s -m <rules_path>/index.yar example2.pdf`
abbiamo molti risultati. Vediamo che c'è un eseguibile

`peepdf -i example2.pdf`
vediamo che c'è del codice js nell'oggetto 9. C'è la parola chiave openAction e abbiamo EmbeddedFiles nell'oggetto 5.

`> object 9`
ci fa vedere che viene esportato l'oggetto `template` con opzione `nLaunch: 0` , questo salva il file senza eseguirlo.
Interattivamente arriviamo a capire che l'oggetto interessato in realtà è l'8

`pdf-parser.py -o 8 -f -w -d object8 example2.pdf`
ci permette di esportare il file

`file object8`
ci dice che il file è un eseguibile
possiamo calcolare l'hash del file per caricarlo su *VirusTotal

---

# 3. analisi di un eseguibile windows

file: `Chapter_12L/Lab12-01.exe`

## i) analisi statica

**pestudio**
vediamo gli *imports*, ci sono alcune funzioni interessanti, 
- VirtualAlloc
- WriteProcessMemory
- CreateRemoteThread
usate per avviare un thread malevolo (**process injection**)

vediamo le *stringhe*
- explorer.exe
- librerie
- dll
- Lab12-01.dll

## ii) analisi dinamica

**ProcMon**

Filtri utilizzati:
- ProcessName `Lab12-01.exe`
- Operation:
	- ThreadCreate
	- ProcessCreate
	- WriteFile
	- RegSetValue
	- SetDispositionInformationFile

Escono 3 eventi.
Vediamo che lancia un thread, un processo, e modifica il valore di un registro (mette come valore tutto il percorso all'eseguibile stesso).
Non capiamo molto da qui.

## iii) reverse engineering

**Ghidra**
Usiamo ghidra per fare reverse engineering e andare più a fondo sul comportamento del file.

>[!warning] Attenzione
>Impostare la flag *"WindowsPE x86 Propagate External Parameters"* prima di avviare l'analisi con ghidra

Dalla funzione *entry* cerchiamo il *main* (call preceduta da 3 push)
-> `FUN_4010D0`

Le prime librerie che vengono chiamate sono 
- LoadLibrary
- GetProcAddress
per avviare una libreria

**`EnumProcessMonitor`**: per tutti i processi che sono in esecuzione sulla macchina popola una struttura dati con i relativi PID

Poi fa la stessa cosa con la funzione **`GetModuleBaseName`**: restituisce un handle a un modulo particolare 

**`EnumProcesses`**: enumera i processi

Gli indirizzi di queste 3 librerie vengono salvate tre variabili.

Nella variabile 108 viene recuperato il valore della directory di esecuzione del processo, con **`GetCurrentDirectory`**.
Questa viene concatenata con altre due stringhe:
1. '//'
2. nome della libreria `Lab12-01.dll`

Poi viene invocata la funzione **`EnumProcesses`** (che ci restituisce 0 se fallisce, oppure un valore diverso)

Se la chiamata va a buon fine, inizia un ciclo for. Tale ciclo for sostanzialmente trova il processo in cui vuole iniettare il codice malevolo.

Una volta trovato, con la funzione **`VirtualAllocEx`**.
Questa funzione prende come parametri
- l'handle del processo
- indirizzo in cui allocare l'area di memoria
- dimensione
- tipo di memoria allocata
- tipo di protezione per l'area di memoria

Se la funzione alloca correttamente l'area, ne restituisce l'indirizzo.

Se ha successo, viene chiamata la funzione **`WriteProcessMemory`**.
Parametri:
- handle del processo
- base address, indirizzo a cui scrivere
- dimensione dell'area di memoria in esadecimale
- ...

In pratica viene presa la DLL e copiata in quest'area di memoria

...

Ultimo passaggio è la creazione del thread con **`CreateRemoteThread`**.

> "In pratica il malware ha creato un'area di memoria, ci ha copiato la DLL malevola e infine ha creato un thread, lanciando la DLL."


> [!info] Esame
> 1. documento malevolo
> 2. analisi di un malware: statica + dinamica
> 
> -> Far vedere di aver capito il corso (il dono della sintesi è apprezzato)



