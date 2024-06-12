I file word malevoli sono molto popolari negli allegati delle mail di phishing, usati come vettori d'attacco per deployare/scaricare il malware

Se un word contiene macro allora è nel formato `.docm` oppure `.docx`. Esiste anche un formato vecchio che contiene dati in binario.

## Formato vecchio
E' composto da:
- header - facilmente riconoscibile
- root storage - file system simile al SO
	- oggetti storage che contengono degli stream

Che tool possiamo usare?
- `olebrowse.py` - naviga nella struttura
- `oletimes.py` - estrae i timestamps
- `oleid.py` - individua caratteristiche malevole (tipo se contiene una macro)
- `oledump.py`- estrae script macro
- `olevba.py` - permette di estrarre ed analizzare le macro contenute (e.g. de-offusca pure uajò)

## Formato nuovo `XML Format`
La sotto-cartella che contiene le macro è `word\qualcosa.bin`.

- analisi metadata -> `exiftool`
- signature detection -> `yara` + `zipdump`, l'ultimo permette di analizzare ricorsivamente tutto il contenuto del file word
- VBA -> `olevba.py`

### `zipdump`

```bash
zipdump -y signature.yar <document.docx>
```

# Metodologia da applicare
Possiamo eseguire dei passaggi:
1. determinare il formato del documento da analizzare
2. analisi statica del documento
	- analisi delle stringhe
	- analisi dei metadati
	- analisi tramite yara
3. estrazione della macro dal documento + analisi
## Analisi della macro
Di solito sono scritte in VisualBasic e potrebbero richiamare comandi (e.g. powershell), inoltre è necessario analizzare per nome di files.

Alcune funzioni utili:
- con `AutoOpen()` verrà eseguita una funzione/i all'avvio
- con `AutoClose()` verrà eseguita una funzione/i alla fine
- `Shell()` permette di eseguire direttamente comandi powershell

Inoltre è possibile usare direttamente le WindowsAPI con tutte le funzioni che ne derivano.

```VBA
Private Declare Function <WindowsAPI>
```

Una volta dichiarata è possibile usarla ovunque nel codice, spesso vengono usate per tentativi di **process injection**, ovvero per eseguire codice nello spazio di memoria di un altro processo.

Anche le macroVBA vengono offuscate con tecniche viste nei file PDF, ref.: [[05_06_2024-pdf-analisys]].

Un tool utile per de-offuscare è `vipermonkey` (è *sperimentale*, quindi non è detto che vada sempre).
Tale tool esegue e cerca di comprendere il comportamento della macro.

# 1. Analisi `badoc.doc`
File: `~/Desktop/Samples/Samples/malicious-documents/badoc.doc`

1. usiamo `oletimes.py` per vedere quando è stato creato il documento
	- contiene delle macro perché sono specificate nell'output
	- creato il 10 feb 2015, tutte le date coincidono
2. usiamo `oleid.py badoc.docx`, dall'analisi:
	- il formato è quello vecchio
	- contiene dei caratteri cirillici
	- contiene una VBA
3. usiamo `olevba.py badoc.docx`, dall'analisi:
	- ci viene restituita la macro intera
	- nella tabella da un riassunto del comportamento della macro

## Analisi della macro
`olevba.py` ci restituisce una serie di funzioni che agiscono nella macro:
- `Shell()`
- `AutoOpen()`
- `UserAgent()` - scarica da Internet??
- `char` - offusca pezzi di stringhe??
- codifiche in base64 ed esadecimale

### Codice della macro
Cosa si nota:
- riferimenti a directory sulla macchina Windows
	- e.g. `local/temp` - come cartella temporanea di download
- pezzi di URL
- riferimenti a `Windows MI` (? non so se si scrive così) - serve per eseguire diverse funzionalità, in questo caso viene usata per determinare la versione del SO
- sembra che in base alla versione vengano eseguite parti di codice diverse
- riferimento al comando `ping`
- alcune stringhe sono completamente offuscate

Possiamo de-offuscare le stringhe attraverso il comando:
`olevba.py --reveal --deobf`.

A seguito della de-offuscazione (non so come si dica) individuiamo:
- funzioni di collegamento ad internet
- comandi powershell
- stringhe de-offuscate
	- ci sono 4 nomi di file eseguibili
	- riferimenti ad adobe
	- estensioni di file
	- riferimenti a cartelle sulla macchina

# 2. Analisi `payment.doc`
File: `~/Desktop/Samples/Samples/malicious-documents/payment.doc`

Il file sembra essere stato creato nel 2016 e contenere delle macro un po' sus.
Inoltre sembra usare il formato vecchio.

Con `olevba` si individua una chiamata che tenta di scaricare un file da un URL, il file sembra essere un eseguibile.
Il file viene scaricato in `%AppData%`, rinominato in `playa.exe` ed avviato.

Tale script VBA runna all'apertura del file.

1. `file payment.doc`
2. `oletimes.py payment.doc`
3. `oledump.py paymeny.doc`
4. `oledump.py -s <numero_oggetto_macro> -v payment.doc > payment.vba` - estrae la macro in base al numero dell'oggetto che contiene la macro
5. `olevba.py` - ci restituisce subito la macro che abbiamo anche estratto precedentemente
6. usiamo `vipermonkey` che esegue il codice per capire

# 3. Analisi `statement.doc`
File: `~/Desktop/Samples/Samples/malicious-documents/statement.doc`

- microsoft word 2007 -> formato nuovo
- con `exiftool` si capisce che è stato generato da un template che accetta macro
- usiamo yara ma *con zipdump perché è formato nuovo*:
	`zipdump -y ~/Desktop/Samples/yara/rules/index.yar <file>`
- `olevba.py -c <file> > file.vba` - estraiamo il codice della macro
	- quando viene aperto il documento viene eseguita `GOODSub`:
		- crea o accede ad un file temporaneo.
		- prende il contenuto della macro e lo salva
		- cerca le istanze della stringa `RELAX` all'interno della macro (quindi di sè stessa)
		- usa la funzione `Right` per prendere il contenuto della stringa eliminando la parola `RELAX`, in questo modo, "pulisce" il codice.
- Sostanzialmente la macro va a modificare il proprio codice per evadere i controlli dei vari software antivirus
