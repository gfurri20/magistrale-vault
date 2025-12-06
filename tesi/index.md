Documentazione e appunti Markdown per la tesi magistrale in Scienze ed Ingegneria Informatiche (UNIVR).

# Indice documenti
Ho cercato di mantenere ordinati tutti i documenti e appunti creati.

Call con professore e tutor:
- [[2025_07_04_primo_colloquio]]
- [[2025_08_20_secondo_colloquio]]
- [[2025_09_10_terzo_colloquio]]

## Domande di valutazione
I modelli vengono valutati attraverso una serie di domande descritte ed organizzare in [[Questions]].

Le diverse valutazioni (insieme di test) vengono riportati nei moduli di `QX?evaluation`, con `X` l'identificativo della domanda madre.

Ogni valutazione è seguita da un riassunto generato con Gemini, in modo da snellire i risultati e mantenere quelli più interessanti.

Di seguito le valutazioni:
- [[Q1_evaluation]] (riassunto [[Q1_evaluation_summary]])
- [[Q2_evaluation]]

## Struttura delle directories
Ogni directory nel progetto raccoglie file precisi, in modo che l'ambiente di lavoro sia organizzato e per il più possibile pulito.

**`datasets`**
Raccoglie i dataset utilizzati per le valutazioni. Ogni dataset ha delle caratteristiche uniche e rappresenta i valori dei registri ogni intervallo di tempo.

**`evaluations`**
Organizza le valutazioni dei modelli, attualmente sono presenti solo valutazioni basate su domande. Le fonti di ragionamento sono i dati di `datasets` passati in formato testuale csv.
	`evaluations/questions` vedi [[index#Domande di valutazione]]

**`images`**
Contiene tutte le immagini del progetto usate nei vati documenti. Le sottocartelle prendono il nome del documento in cui la foto è inserita, cercando di mantenere il tutto più ordinato possibile.

**`junk`**
File "spazzatura", ovvero appunti considerati non rilevanti

**`meetings`**
Contiene tutti gli appunti presi durante le call con professore e tutor

**`notebooks`**
Tutto il codice scritto per testare i modelli è racchiuso in notebooks Jupyter, ogni notebook è contenuto nella specifica cartella.

**`responses`**
Ogni valutazione crea un file report in formato JSON. Tutti i file di report sono contenuti in questa cartella, organizzati in sotto-directories, in base al giorno di creazione del file

