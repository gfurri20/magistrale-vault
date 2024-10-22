# Ingegneria dei requisiti

> [!info] Requisito
> Descrizione del servizio che il SW dovrà fornire all'utente

Esistono due tipi di requisiti:
- **User** -> cosa deve fare il sistema per supportare l'utente (esprimono una necessità intrinseca del business), tipicamente espressi in linguaggio naturale + qualche schemino
- **System** -> per gli addetti ai lavori, sono descritti in un doc. più strutturato e sono, a livello di dettaglio, più concreti

Spesso ad un user requirement corrispondono molteplici system requirements.

> [!info] Stakeholder
> Coloro che sono affetti, qualsiasi modo, dal sistema software. Dal medico che usa il SW fino al paziente che è semplicemente inserito.

***Requisito funzionale*** -> descrivono le funzionalità dei servizi che il sistema mette a disposizione
- reazione a diversi input
- funzionamento rispetto a svariate eventualità
- possiedono ==diversi livelli di astrazione==
- alcuni potrebbero essere ==ambigui== e quindi interpretati in maniera diversa
- Obiettivi:
	- devono essere *completi* -> ogni punto di appartenenza deve essere definito completamente
	- devono essere *consistenti* -> lo stesso concetto non deve essere sviluppato in maniera diversa
- In pratica:
	- i diversi stakeholders potrebbero avere necessità diverse
	- le inconsistenze non sono facili da trovare e serve un'analisi mirata

***Requisito non-funzionale*** -> esprimono caratteristiche del sistema rispetto a dei limiti/vincoli impostati da standard, contesto o necessità
- sono requisiti ma non sono funzionalità
- sono molto importanti perché ==vincolano il tipo di architettura== che dovremmo utilizzare
- un requisito non-funzionale ==può generare svariati requisiti funzionali==
- spesso si utilizzano delle tassonomie gerarchiche per individuare tutti i req. non funzionali (vedi slides)

## Processo di lavoro
Il processo si divide in varie fasi ed ha il compito di raccogliere e specificare i requisiti adeguati.

L'obiettivo è la composizione del documenti dei requisiti, fondamentale per passare alla fase di sviluppo.

La divisione è logica, nella realtà, le tre fasi sotto-riportate non sempre eseguite in un ordine preciso. 

### 1. Elicitazione
In questa fase ingegneri del SW e stakeholders lavorano insieme per capire:
- il dominio di applicazione del sistema
- requisiti funzionali
- requisiti non-funzionali
- vincoli

Spesso gli stakeholders non sanno cosa vogliono concretamente, oppure esprimono i requisiti nel loro gergo, avendo una conoscenza esplicita che non esprimono.

Differenti stakeholders possono avere requisiti diversi, rispetto ai loro POV.

I requisiti sono in continua evoluzione, quindi vanno "inseguiti" costantemente nel tempo.

Per raccogliere tutte le informazioni necessari ci sono diverse modalità:
- **Interviste** -> domande esplicite allo stakeholder
	- crocette o domande aperte
	- lo stakeholder va guidato nell'indagine
	- esistono dei problemi legati alla distanza culturale (inserimento di termini tecnici), va usata la prospettiva dello stakeholder
- **Studi etnografici** -> l'ingegnere dei requisiti si "immerge" nella realtà aziendale per comprendere come gli stakeholder lavorano, con lo scopo di capire a pieno i requisiti
	- ovviamente costano molto economicamente e temporalmente
- **Storie e scenari** -> analisi delle storie e degli scenari di lavoro esemplificativi
	- *Storie* -> narrative e ad alto livello
	- *Scenari* -> strutturati per sottolineare informazioni specifiche
	- una parte di una storia può trasformarsi in diversi scenari

### 2. Specifica


### 3. Validazione