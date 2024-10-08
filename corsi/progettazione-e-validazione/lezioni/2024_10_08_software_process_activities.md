
Attività comuni ai vari processi software (vedere [[2024_10_02_software_process]]):
- specifica
- design ed implementazione
- validazione
- evoluzione

---

# Specifica
-> Obiettivo: capire cosa il sistema deve farlo con annessa documentazione, servizi e funzionalità a disposizione dell'utente finale.

**Punto critico**, perché se si sbaglia a capire le specifiche si sbaglia il progetto!

L'analisi dei requisiti può essere preceduta dallo *studio di fattibilità*, esso permette di simulare il processo di sviluppo in breve tempo. Permette di capire quanto un progetto è fattibile assieme ai limiti presenti.

-> Output: documento dei requisiti, specifica le funzionalità del sistema. Deve soddisfare le necessità dello stakeholder.

Fasi della Specifica:
1. **analisi dei requisiti** - comunicazione con l'utente finale per ottenere i requisiti
	- frutto del dialogo con il cliente
	- produzione di schemi ed appunti
2. **raffinazione dei requisiti** - correzione degli errori e delle inconsistenze
	- si produce un documento non ambiguo utile per lo sviluppo
	- due tipi di requisiti
		- *utente* -> requisiti legati alle procedure aziendali/legali
		- *sistema* -> implementazione funzionale
3. **validazione dei requisiti** - analisi dell'effettiva implementazione reale dei requisiti entro i limiti esistenti
	- gestione degli errori o delle eccezioni, spesso mancante o lacunosa
	- risoluzione definitiva degli errori e delle ambiguità


# Design ed Implementazione
-> Obiettivo: trasformazione della Specifica in un sistema software effettivo

==Le fasi possono essere sequenziali oppure parallele.==
## Design
Impostazione della struttura del software insieme alla scelta degli strumenti da usare per lo sviluppo

1. *architectural design* - scelta dell'architettura, è una progettazione di alto livello (astratti)
2. *database design* - progettazione della struttura dati (e.g. db relazione, eccetera)
3. *interface design* - integrazione tra i vari componenti, formato di scambio dati e con quali regole (potrebbero esserci team diversi)
4. *component design* - selezione delle tecnologia da utilizzare

## Implementazione
Sviluppo effettivo in base alle scelte fatte precedentemente


# Validazione
-> Obiettivo: confermare o meno che l'implementazione segua i requisiti utente

1. *checking* - ispezione manuale del codice alla ricerca di inconsistenze
2. *program testing* - esecuzione del prodotto in modo da verificare il funzionamento rispetto ai requisiti
	1. component testing - test indipendente dei singoli componenti
	2. system testing - test dei componenti assemblati per la riproduzione di scenari che ricercano la realtà
	3. acceptance test - test del software intero da parte dell'utente, attuando una totale verifica del sistema nella realtà, ==è possibile scoprire errori nella raccolta dei requisiti==

I test vengono definiti in ordine diverso rispetto alla definizione, questo perché ci si sposta dallo specifico allo generico.



# Evoluzione
-> Obiettivo: mantenimento del SW rispetto ad errori, adeguamenti o altre necessità.

Quindi il sistema deve comunque cercare di introdurre una gestione del cambiamento facilitata:
- anticipazione del cambiamento -> introdurre nei requisiti la gestione del cambiamento

Il cambiamento deve essere analizzato, incrocio tra funzionalità nuove e vecchie, pur garantendo l'usabilità.

Per gestire il cambiamento in maniera corretta risulta utile creare un **prototipo**, per anticipare le nuove funzionalità in modo da ottenere del feedback, in maniera veloce e più economica. Inoltre permette di aumentare la chiarezza durante la comunicazione tra utente e sviluppatore.

Un altro modo per gestire il cambiamento è quello di prevedere **consegne incrementali** e periodiche nel tempo. Possiede funzionalità limitate ma scenari ben maggiori, il contrario del prototipo.
Godevoli vantaggi ➕
- trasferimento della funzionalità veloce
- permette di migliorare la fase di testing
- abbassa il rischio del progetto
Svantaggi 🚫
- si necessita di tanto lavoro per la prima release -> primo feedback tardi
- difficile pensare incrementi sensati nelle successive iterazioni
- la specifica è portata avanti in parallelo e questo non è possibile per alcune commesse (e.g. commesse governative o critiche)

