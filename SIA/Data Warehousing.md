<small>Venerdì 26 gennaio 2024</small>

L'informatica, al giorno d'oggi, caratterizza praticamente ogni aspetto delle aziende moderne.
Rispetto agli inizi degli anni '70, in cui si introducevano in azienda i primi sistemi informatici, il ruolo degli stessi è radicalmente cambiato: da semplici strumenti implementati per migliorare l'efficienza dei processi si è a strumenti centrali dell'organizzazione aziendale.

L'informatica ha un duplice scopo:
 - supportare la gestione del SI
 - influenzare i processi aziendali

Ci sono diverse motivazioni che inducono l'introduzione di sistemi informatici:
- l'economia moderna è basata su conoscenze ed informazione
- permettono di rendere più competitiva l'azienda
- necessità di gestire mercati su scala globale

Ogni aspetto aziendale è supportato da applicativi informatici, l'insieme degli stessi si definisce **portafoglio aziendale**, esso fornisce sistemi informatici ai manager di ogni area funzionale aziendale. 

Sistema di **Business intelligence**: infrastruttura HW e SW che permette la trasformazione di dati aziendali in informazioni raffinate in modo che possano essere usate per prendere le migliori decisioni possibili per l'azienda.

$$dati \space + \space significato \space = \space informazione$$
Veloce richiamo alla piramide delle informazioni:
- fonti primitive --> dati
- lavorazione dei dati --> informazione
- rapporti --> conoscenza
- indicazione strategiche --> previsione del futuro

Ricordando la mappatura tra strumenti informativi e piramide di Anthony, i DSS (Decision Support System) sono quei sistemi che permettono di elaborare informazioni in modo da poter eseguire decisione nel quotidiano.

Il Data warehouse non è altro che un DSS, esso permette di sostituire i database operazionali per le operazioni di analisi delle informazioni a scopi decisionali.

I sistemi DSS trovano la loro utilità in quelle situazioni in cui l'analisi potrebbe portare benefici.

# Data WarehousING vs Data Warehouse
==Il Data Warehousing è, per definizione, una collezione di sistemi, tecnologie e strumenti di ausilio al *knowledge worker* per condurre analisi dei dati finalizzare all'attuazione di processi decisionali e al miglioramento del patrimonio informativo.==

Possiamo affermare che il Data Warehousing è rappresentato da un insieme di procedimenti che trasformano e manipolano i dati in modo da metterli a disposizione del *knowledge worker*.

Il Data Warehouse **fa parte** del sistema di Data Warehousing e non è altro che un contenitore di dati (di solito numerici) con delle specifiche caratteristiche che lo differenziano da un classico sistema operazionale.

Il DW è **nato** solo per questo scopo quindi ogni metro di paragone con un database operazionale è per mero scopo di confronto, ovviamente il DW svolge meglio il compito di un DSS.

## Caratteristiche di un sistema di Data Warehousing
Il processo di Data Warehousing **deve** garantire:
- **accessibilità** - ogni tipo di knowledge worker deve essere in grado di usufruire dei dati
- **integrazione** - i dati gestiti possono provenire da fonti eterogenee
- **flessibilità di interrogazione** - le interrogazioni devono essere efficaci ed efficienti
- **sintesi** - per analisi mirate
- **multidimensionalità** - visione intuitiva delle info
- **correttezza** e **completezza**

## Definizione di Data Warehouse
Un DW è un contenitore di dati di supporto per il processo decisionale che presenta le seguenti caratteristiche:
- **orientata ai soggetti interessati** - si concentra sui dati utili ai soggetti che ne usufruiscono
- **integrata** e **consistente** - contiene dati estratti da fonti eterogenee rendendoli unificati
- **rappresentativa dell'evoluzione temporale** - permette la periodizzazione dei dati
- **non volatile** - contiene grandi moli di dati e non usa le transazioni, infatti viene usato solo in fase di lettura

Le interrogazioni avvengono tramite un sistema OLAP (On-Line Analytical Processing), che permette di rendere il sistema di Data Warehousing multidimensionale, interattivo e dinamico. I dati estratti non sono "congelati" ma variano costantemente nel tempo.

# Architettura di un sistema di Data Warehousing
Un sistema di Data Warehousing può essere implementato in maniere differenti ma deve garantire che si rispetti diversi requisiti:
- **separazione** - tra parte transanzionale e analitica
- **scalabilità** - facilità di ri-dimensione in base al carico
- **estensibilità** - facilità di estensione con ulteriori funzioni (e.g. data-mining)
- **sicurezza** - access control
- **amministrabilità** - facilità di gestione

## 1 livello
L'obiettivo è quello di andare a minimizzare i dati memorizzati, eliminando le ridondanze.
Il Data Warehouse viene **simulato** da un middle-ware (detto DW virtuale) a diretto contatto con le sorgenti e le analisi:
1. sorgenti
2. middleware
3. strumenti di analisi

Pro:
- costo
- perfetto per analisi limitate
Contro:
- non c'è separazione 
- basso livello di storicizzazione

## 2 livelli
In realtà si sviluppa su quattro livelli ed introduce un DW effettivo e i sistemi di ETL:
1. sorgenti - anche eterogenee
2. alimentazione - sistemi ETL, puliscono i dati
3. warehouse - DW effettivo a contatto con i data mart
4. analisi - con OLAP quindi multidim, dinamico ed interattivo

I **data mart** sono dei sottoinsiemi di dati specifici per una determinata categoria di knowledge worker prelevati dal DW. Grazie all'aggregazione di dati permettono di raggruppare info in base ad aree di business, riducendo il volume e migliorando le prestazioni.
I data mart dipendenti sono creati a partire dal DW (prestazioni migliori del DW); mentre quelli indipendenti sono creati direttamente dalle sorgenti (snellimento fasi progettuali ma possibile inconsistenza).

Pro:
- info di buona qualità (grazie a ETL)
- OLAP che separa la parte transazionale
- multidim, dinamicità ed interattività
- migliore reportistica grazie ai data mart
Contro:
- costo
- mancanza di un bacino di dati comuni e di riferimento

## 3 livelli
Presenta gli stessi livelli dell'architettura a 2 livelli ma aggiunge il bacino dei **dati riconciliati** che permette al DW di non pescare direttamente dalle sorgenti (ripulite con ETL) ma, bensì, di estrarre i dati da un modello comune e di riferimento per l'intera azienda.

==Dati riconciliati: ulteriore processo di ripulitura e omogenizzazione.==

Pro:
- più alta separazione
- modello di dati comuni ed omogenei
Contro:
- costo
- ridondanza

# Sistemi ETL
I sistemi ETL (Extraction, Trasformation and Loading) attingono i dati dalle sorgenti (spesso eterogenee) per eseguire un processo di pulitura in modo alimentare il DW.

I dati vengono:
- estratti
- puliti
- trasformati
- caricati

## Estrazione
Estrazione da sorgenti eterogenee. La scelta dei dati avviene in base alla qualità e alla necessità.

C'è l'estrazione statica per popolare la prima volta un DW, vengono fotografati i dati operazionali.
C'è l'estrazione incrementale per aggiornare periodicamente il DW e catturare i cambiamenti.

## Pulitura
L'obiettivo è quello di migliorare i dati, quindi identifica duplicati, inconsistenze, mancanze, errori, eccetera

## Trasformazione
Conversione da operazionale a DW suitable con fase di integrazione.
Qua i processi ETL distinguono architettura a 2 o 3 livelli:
- 2 livelli, quindi immediata alimentazione DW: viene fatta denormalizzazione e aggregazione per sintetizzare i dati
- 3 livelli, quindi alimentazione dei dati riconciliati: normalizzazione, matching per cercare ricorrenze e selezione per ridurre i record

## Caricamento
Due tipi di caricamento:
- refresh per sostituire i dati integralmente
- update per aggiungere i cambiamenti

# Multi dimensionalità
Metodo di rappresentazione dei dati per renderli intuitivamente fruibili a qualsiasi knowledge worker.

Ogni fatto di interesse corrisponde ad un cubo:
- ogni cella (bidimensionale) contiene misure numeriche
- ogni asse rappresenta una dimensione

Una dimensione è organizzata gerarchicamente, e.g.:
$$\text{giorno} \rightarrow \text{mese} \rightarrow \text{anno}$$
L'analisi dei dati permette diverse attività:
- reportistica - per visualizzare le prestazioni aziendali con grafici ed altro
- OLAP - per interagire multidim, dinamicamente ed interattivmanete con i fatti
- data mining - per scoprire info nascoste all'interno di innumerevoli dati

Una sessione OLAP consiste in un percorso di navigazione in cui ogni operazione eseguita è influenzata dalla storia delle interrogazione precedenti, sono formulate per differenza.
Tutto ciò permette di modellare un cubo composto da fatti.

Gli operatori OLAP sono:
- roll-up: aggrega per dimensione in base alla gerarchia
$$\text{giorno} \rightarrow \text{mese}$$
- drill-down: disaggrega per dimensione in base alla gerarchia
$$\text{mese} \rightarrow \text{giorno}$$
- slice-and-dice: permette di ottenere dei muri di fatti o di rimpicciolire il cubo di partenza
- pivoting: permette di cambiare la modalità di presentazione
- drill-across: permette di collegare uno o più cubi per eseguire comparazioni

# Qualità dei dati
La qualità dei dati in un sistema DW è caratterizzato da:
- **accuratezza** - valore memorizzato vs reale
- **attualità** - no obsolescenza
- **completezza**
- **consistenza** - uniformità di rappresentazione
- **disponibilità** - facilità di prelievo
- **tracciabilità** - risalire alla fonte
- **chiarezza** - interpretabili da tutti

# ROLAP e MOLAP

Il modello **ROLAP** (Relational Online Analytical Processing) è un tipo di elaborazione analitica online (OLAP) che utilizza modelli di dati multidimensionali per analizzare informazioni. ROLAP accede alle informazioni memorizzate in un database relazionale.

Il problema è il grandissimo uso di operatori di join che appesantiscono le transazioni.

Il modello **MOLAP** (Multidimensional OLAP) fa in modo che i dati siano memorizzati in vettori e l'accesso è di tipo posizionale. Il vantaggio è che non vengono usate operazioni di join, migliorando le prestazioni.