I documenti PDF malevoli sono principalmente usati per attaccare le vittime:
- phishing
- estrazione dell'eseguibile malevolo
- scarica il malware da un server C2

Quindi come vettori per inoltrare il malware.

# Struttura di un PDF

Ci sono diversi tipi di elementi che compongono un pdf malevolo:
- oggetti
- parole chiave

## Oggetti
Sono composti da:
- header - identifica la specifica del file, si trova nei primi 1024 byte di un documento pdf
- catalog - indice di un documento, ne definisce la struttura
- stream - contengono i dati veri e propri

Gli oggetti sono identificati da dei delimitatori e possono essere richiamati all'interno di altri oggetti.

## Parole chiave
Danno informazioni relative al pdf:
- `/OpenAction` - azione che viene svolta all'apertura
- `/JavaScript`, `/JS` - precedono codice js
- `/Names` - per identificare altri oggetti
- `/EmbeddedFiles` - specifica che il pdf contiene altri files
- `/URI`, `/SubmitForm` - apre URL utili per scaricare files
- `/Launch` - simile a OpenAction, esegue dei comandi

Le keyword sono specificate all'interno delle virgolette: `<< ... >>`.

## Data
Possono essere diversi tipi:
- testo
- codice

Gli attaccanti possono adottare tecniche per rendere difficile l'analisi delle stringhe di un pdf.

> [!info] e.g.
> Per oscurare il nome di un oggetto è possibile sostituire alcuni caratteri in hex, usando il carattere `#`; si può anche usare codifica ottale o aggiungere degli spazi

Inoltre possono usare delle parole chiave che indicano che il contenuto di un oggetto è stato codificato:
- `/ASCIIHexDecode` - oggetto codificato in Hex
- `/ASCII85Decode` - oggetto codificato in una base diversa
- `/Crypt` - oggetto cifrato con un determinato algo

Tali tecniche possono essere utilizzate insieme, ma sono facili da scardinare applicando i medesimi algoritmi in ordine inverso.

---

# Analisi vera e propria
Dopo una prima analisi iniziale sulle stringhe si possono applicare le `yara rules` per cercare informazioni maggiori; inoltre si possono analizzare i metadata per ricavare informazioni ulteriori.

Una volta fatto ciò si possono analizzare le keywords per cercare oggetti codificati o altre informazioni utili.

## Tools
- `strings` - analisi delle stringhe
- `exiftool` - analisi dei metadati
- `pdfid.py` - restituisce info sulla struttura del pdf, tipologia di oggetti, parole chiave eccetera
- `pdf-parser.py` - permette di estrarre il contenuto di un oggetto e di codificarlo di conseguenza
- `peepdf` - mostra gli oggetti che possono contenere codice JS, marca gli oggetti che contengono parole chiave ed inoltre salva il contenuto di un oggetto (è il tool più completo)

## Analisi del codice JS
Tipicamente il codice JS viene usato per scaricare il malware sulla macchina oppure per sfruttare eventuali vulns (british bitch 🇬🇧 🫖 💂).

Spesso il codice JS è offuscato per rendere complicata l'analisi.
Per capire il codice bisogna dare il reverse del codice. :tea

Esistono varie tecniche di offuscamento:
- **Formatting** - illeggibilità del codice attraverso rimozione di spazi e newlines
- **Data Obfuscation** - offuscamento del valore delle variabili
	- sostituzione dei caratteri con l'equivalente esadecimale
	- uso di base64 o codifica esadecimale
	- encrypt di stringhe utili con diverse metodologie
	- separazioni di frammenti di stringhe
	- si può applicare anche per i numeri complicando le operazioni algebriche
- **Extraneous Code** - aggiunta di codice inutile come variabili o funzioni inutilizzate
- **Substitution** - sostituzione dei nomi delle variabili con sequenze di caratteri random, questo per creare confusione. Per eliminare tale livello di offuscamento bisogna andare ad analizzare il contenuto della variabile che ci potrebbe aiutare ad associare un nome comprensibile.

Sarebbe opportuno eseguire il codice JS in una sandbox per avere il completo controllo dell'esecuzione

`peepdf` rimane un tool utile per fare ciò perché permette di:
- riorganizzare il codice
- eseguirlo in una sandbox
- permette di eseguire comandi inline

`spidermokey` è una sandbox nella quale si può eseguire il codice JS ed intercetta:
- `eval` - valuta le espressioni
- `document.write` - scrive su documenti
- `window.navigate` - 
Per usarlo `js_file <FILE>`.

--- 

La pratica la lascio a **Lucianone Nazionale** perché devo andare a lavoro.

...