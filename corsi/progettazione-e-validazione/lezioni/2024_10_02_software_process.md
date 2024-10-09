
> [!info] Software process
>Sviluppo e validazione del software

Esistono svariate best practice per la gestione del software process, ognuna delle quali con le proprie caratteristiche.
Bisogna saper scegliere in base alle proprie necessità.

Lo sviluppo del software deve essere una disciplina **controllata**, **ordinabile** e **ripetibile**. L'attività di sviluppo deve essere sempre sotto controllo.

Obiettivo:
- migliorare la produttività degli sviluppatori
- controllare la qualità del software finale

$$\texttt{Process quality} = \texttt{Product quality}$$

>[!info] Processo
>Una serie di attività strutturate che permettono di sviluppare un sistema software

Tratti del processo di sviluppo:
1. **specifiche**, definite e comprese
2. **design ed implementazione**, scrittura vera e propria
3. **validazione**, verifica dell'implementazione nei confronti delle necessità utente
4. **evoluzione**, entità viva soggetta ad evoluzione (e.g. bug)

I processi si differenziano in due macro categorie:
- processi **plan-drive** -> attività di pianificazione *dettagliata*, l'obiettivo è quello di poter mappare in ogni momento lo sviluppo effettivo con il piano d'azione
- processi **agile** -> il piano cresce con lo sviluppo, a mano a mano 🎶. La pianificazione ==si adatta alle problematiche che si incontrano durante il percorso==.

Spesso si adotta un'approccio ibrido.

# Processi di sviluppo
Esistono diversi approcci pratici ai processi di sviluppo:
- **code and fix** -> implementa e correggi, il codice è sviluppato "per tentativi" e non c'è una grande parte di design e progettazione
	- vantaggioso per progetti di piccole dimensioni
	- in realtà in questo modo non si adotta un processo -> *fallimento*
- **waterfall** -> processo guidati da piani, prevede attività separate per le varie task
- **incrementale** -> prevede di consegnare molteplici versioni aventi funzionalità incrementali
- **integrazione e configurazione** -> cerca di scrivere meno codice possibile integrando blocchi già esistenti tra loro

Anche in questo caso l'azienda potrebbe mixare i processi.

## Waterfall model 🌧
Nasce con le prime, importanti e complesse commesse industriali (🪖). Deriva dal processo manifatturiero con il quale ha una mappatura 1:1.

==Ogni fase dello sviluppo ha come input l'output della fase precedente.==

Attività condotte:
1. *definizione dei requisiti* e delle funzionalità, con annesse problematiche, assieme agli stakeholders
2. *progettazione del software* e definizione ad alto livello del software; quindi comunicazione tra i vari componenti
3. *implementazione*, scrittura del codice e realizzazione assieme ad eventuali test
4. *integrazione delle componenti* e fase di test per verificare la connettività e la funzionalità lato utente finale
5. *produzione* e *manutenzione*, quindi pubblicazione del sistema e adattamento del sistema in base a problemi/cambiamenti

> possibile domanda d'esame

Ci sono contesti in cui è meno appropriato applicare waterfall perché *non si può tornare indietro*, si necessità, quindi, di una **completa** comprensione dei requisiti.

Sistemi appropriati ai quali applicare waterfall:
- sistema software/hardware
- sistema critico, ovvero un ==sistema vitale== per individui o gruppi 🏥
- sistemi di grandi dimensioni, in cui i componenti potrebbero non appartenere allo stesso dominio aziendale

I requisiti per questo tipo di sistemi devono essere validati per normativa legale, in quanto essi sono ritenuti critici e delicati.

Vantaggi:
- molto effort nella comprensione dei requisiti, lo sviluppo non parte senza completezza dei requisiti
- introduce una pianificazione dettagliata -> sviluppo ordinato e chiaro
- checkpoint intermedi molto chiari utili alla coordinazione

Svantaggi:
- le fasi devono essere complete per passare a quella successiva
- difficile far trovare spazio ai cambiamenti all'interno dello sviluppo -> *non si torna più indietro*

## Incrementale
Le varie fasi avanzano in parallelo e concorrono alla definizione delle versioni successive al processo.

Spesso si utilizza nel caso in cui i requisiti potrebbero cambiare in fase di sviluppo, perché la specifica degli stessi segue il ciclo di vita, intero, del processo.

Vantaggi:
- riduzione dei costi nel caso di cambiamenti
- meno documentazione
- più facile ottenere un feedback dall'utente finale e rifletterlo nel prodotto finale; questo grazie alla consegna di versioni preliminari

Svantaggi:
- l'adattamento di ulteriori funzionalità concorre a ridurre la qualità del SW stesso, a causa di aggiunta di pezzi ai quali non si aveva pensato inizialmente
- è difficile da capire se si sta accumulando ritardo
- sarà sempre più difficile aggiungere pezzi

## Integrazione e configurazione
Basato sul riuso del software per agire sul mercato in **maniera rapida**.

...

Di solito si cercano componenti da configurare tra di loro, non sempre danno il risultato che si cerca.
I ==requisiti devono piegarsi ai componenti che sono disponibili==, potrebbe innescarsi una fase di negoziazione.

I componenti possono essere open-source, commerciali o proprietari.

Vantaggi:
- consegna di un sistema anche a fronte di poco budget
- basso rischio grazie all'uso di componenti testate
- poco sviluppo da zero
- consegna rapida di un sistema valido -> aggressione rapida del mercato (spesso è un requisito fondamentale)

Svantaggi:
- bassa qualità -> uso componenti non pensati per quel contesto
- necessità di accettare un trade-off sulle funzionalità
- perdita del controllo sull'evoluzione del SW, sono pezzi sviluppati da altri e sui quali non si ha giurisdizione

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