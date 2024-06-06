Analisi **dinamica** di un malware.

Prima dell'analisi dinamica è sempre conveniente eseguire l'analisi statica [[27_03_2024-analisi-statica]].
Questo ci permette di individuare diverse informazioni che possono essere utili in fase di analisi dinamica.

L'analisi dinamica dovrebbe concentrarsi su:
- modifiche del file system
- modifiche ai registri
- traffico di rete generato
- auto-start del malware

Quali tools useremo?
- Regshot - permette di tracciare tutte le modifiche che vengono fatte dal malware alle risorse e ai registri
- Process Monitor - per tracciare le chiamate alle WinAPI

Esistono due tipologie di analisi:

**System integrity monitoring** (RegShot)
Per individuare le modifiche che vengono effettuate dal malware su file system e registri.
Per fare ciò si fa uno screenshot della macchina si esegue il malware per tot. tempo ed estraiamo un altro screenshot, infine si comparano le differenze.
Ovviamente presenta delle limitazioni
- non è possibile capire come sono stati fatti i cambiamenti
- non è possibile trovare tutti i file tmp creati dal malware per raggiungere i propri scopi
- non individua eventuali modifiche eseguite da un rootkit

**Behavioral Monitoring** (Process Monitor)
Questa analisi permette di analizzare le chiamate alle API:
- individua come sono stati eseguiti i cambiamenti
- individua eventuali file tmp

Ci concentreremo su determinati API, registri di sistema e processi.

Regole di esecuzione dei tools:
1. farli partire entrambi as admin
2. pausa process monitor e prendo lo screen
3. faccio ripartire process monitor
4. avvio malware e lo faccio *sbrodolare*
5. pausa process monitor e prendo screen
6. comparazione delle differenze

Meglio analizzare i log dal fondo per poi salire.

## Primo Malware - budget-report
Utilizzando i passaggi sopra riportati è possibile individuare i comportamenti del malware.

Per esempio:
- ha cancellato chiavi
- ha creato directories

Grazie a ProcessMonitor possiamo filtrare per (simbolo del diamante) le informazioni che ci interessano:
- `Process Name` - filtriamo cercando il nome del processo "budget-report.exe"
- `Operation` - settiamo `WriteFile`, `RegSetValue`, `SetDispositionInformationFile`, `ProcessCreate`, eccetera.

Troviamo che:
- Si nota la modifica del registro `Hidden` che viene usato per cambiare la visibilità dei files.
- Il malware si accorge di essere eseguito in VM.
- Tramite `cmd.exe` cancella un file `.bat`.
- Raggiunge persistenza modificando il registro `RunOnce`.


