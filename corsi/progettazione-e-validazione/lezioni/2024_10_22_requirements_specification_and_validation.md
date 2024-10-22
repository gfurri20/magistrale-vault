# Requirements Specification
I requisiti devono dire **cosa** il prodotto dovrà fare, non in **come**. In pratica la divisione non è così netta perché ci sono alcuni aspetti in cui il come diventa intrinsecamente requisito. Certe volte l'architettura dipende dalla funzionalità richiesta.

Ci sono ==diversi modi per esprimere i requisiti==:
- **linguaggio naturale**
	- intuitivo ed universale
	- vago ed ambiguo -> stesse parole in domini diversi possono avere semantiche diverse
	- bisogna utilizzare delle parole ed espressioni precise per le diverse situazioni, oltre che uniformare il contesto di utilizzo di una parola
- **modalità strutturate**
	- grado di libertà molto inferiore, perché è guidato e standardizzato
	- funziona bene in sistemi embedded
	- spesso i requisiti sono strutturati in una *tabella gerarchica vincolata*
	- la struttura è decisa all'inizio ed utilizzata per tutti i requisiti
	- nel caso di condizione spesso è meglio rappresentarle in una tabella e con una sintassi che include caratteri matematici
- **use case**
	- è una rappresentazione grafica ad alto livello che rappresento uno specifico scenario
	- ogni use case può essere esploso in un sequence diagram per evidenziare le azioni in sequenza o parallelo

Il ***documento dei requisiti*** rappresenta e raccoglie tutti i requisiti raccolti e specificati. Può avere forme e realizzazioni diverse, in base al tipo di processo di produzione utilizzato.

Utenti che utilizzano tale documento:
- clienti -> possono controllare tutti i vari requisiti specificati
- manager -> possono usarlo per stimare un preventivo generale
- ingegneri del SW -> progettazione e realizzazione del sistema
- testers -> impostazione dell'attività di test del sistema
- mantenitori

## Standard IEEE
IEEE ha redatto uno standard per la creazione del documento dei requisiti, attraverso un semplice schema.

- Prefazione
- Introduzione
- Glossario -> definisce delle *keyword*, ovvero termini specifici associati ad un significato preciso
- Definizione dei requisiti utente
- Vincoli architetturali
- Definizione dei requisiti di sistema
- Modelli, evoluzioni
- Appendici ed indice (non all'inizio chissa perché)

---

# Requirements Validation
L'obiettivo è quello di capire se i requisiti sono ciò che l'utente davvero vuole.

Checklist di validazione:
- *verifica della validità* -> dà risposta alle necessità degli stakeholder?
- *verifica della consistenza* -> siamo coerenti nei requisiti?
- *verifica di completezza* -> tutte le funzionalità sono catturate dal documento dei requisiti?
- *verifica di realizzazione* -> è possibile realizzare uno specifico requisito, per budget/tempo o personale?
- *verifica di verificabilità* -> può il componente essere controllato?

---

# Cambiamento dei requisiti
Maggiore è la grandezza del sistema da realizzare, maggiore sarà la possibile necessità di cambiamenti.

Potrebbe anche cambiare la priorità tra gli stakeholders, in questo caso va data maggiore importanza in base alle nuove assegnazioni.

Diventa necessario:
- dotarsi di policies
- dotarsi di tool automatizzati che aiutano il processo di cambiamento
- costruire un processo di cambiamento dei requisiti

## Processo di cambiamento
Passi da seguire:
1. analisi del problema in modo da recepirla
2. cambiamento dell'analisi iniziale e dei costi
3. cambiamento dell'implementazione
