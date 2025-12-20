In questa fase di test, ai modelli è stato chiesto di identificare il numero di serbatoi coinvolti nelle operazioni dell'ICS basandosi esclusivamente sui log dei dati.

* **Domanda:** *Identify how many tanks are involved...*
* **Opzioni:** Da '1' a '10'.
* **Risposta Corretta (Ground Truth):** 3 (dedotta dalle performance perfette nello scenario chiaro).

---

## 1. Analisi su Dataset `plc_data_log`
Questo dataset contiene dati ottenuti con un sample ad intervallo maggiore. Un altra caratteristica interessante è che i valori booleani sono rappresentati in linguaggio naturale `True`/`False`. 

| Modello         | Accuracy (Original Header) | Accuracy (Anon. Header) | Comportamento Principale                                       |
| :-------------- | :------------------------: | :---------------------: | :------------------------------------------------------------- |
| **Kat-Coder**   |            79%             |           35%           | Buono con header, entra in confusione senza (risposte sparse). |
| **DeepSeek-R1** |          **65%**           |         **50%**         | Performance mediocre ma "stabile", degrada meno degli altri.   |
| **Mistral-Dev** |            100%            |           0%            | Binario. Perfetto con le etichette, fallimento totale senza.   |

![[Code_Generated_Image(13).png]]

![[Code_Generated_Image(12).png]]

**Osservazioni:**
- **Kat-Coder** prova a ragionare sui dati ma perde affidabilità senza le etichette, disperdendo le risposte tra vari valori errati.
- **DeepSeek** sembra ottenere, in media, i risultati migliori. Con le etichette ottiene un accuracy pari al 65%, essa peggiora del 15% rimuovendo le etichette. 
* **Mistral-Dev** dimostra di dipendere interamente dalla semantica delle colonne. Quando le colonne sono anonimizzate, risponde sistematicamente "2" con altissima confidenza (*Overconfidence*), sbagliando ogni singolo test.

---

## 2. Analisi su Dataset `baseline`
Questo dataset contiene maggiori informazioni, evidenziando anche i valori all'istante `t-1`. Inoltre tutte le informazioni sono rappresentante attraverso indicatori numerici, compresi i valori booleani `0` o `1`.

| Modello         | Accuracy (Original Header) | Accuracy (Anon. Header) | Comportamento Principale                                                            |
| :-------------- | :------------------------: | :---------------------: | :---------------------------------------------------------------------------------- |
| **Kat-Coder**   |            60%             |           10%           | Crollo significativo delle performance rispetto al dataset con header anonimizzato. |
| **DeepSeek-R1** |            15%             |           0%            | Fallimento quasi totale su questo dataset.                                          |
| **Mistral-Dev** |            100%            |           0%            | Conferma il comportamento binario.                                                  |

![[Code_Generated_Image(14).png]]

![[Code_Generated_Image(15).png]]

**Osservazioni:**
- **Kat-Coder** mantiene un'accuracy simile con le etichette presenti: al contrario fa registrare un crollo significativo delle performance senza etichette.
* **DeepSeek-R1**, che eccelleva in Q1 (classificazione tipo impianto), qui crolla. Nel dataset *baseline*, sembra non riuscire a isolare i segnali corretti per contare i serbatoi, confondendosi spesso con risposte come "2" o "9" nello scenario anonimo.
* **Mistral-Dev** si conferma un modello "lazy": se l'informazione è esplicita nell'header la trova subito (100%), altrimenti "tira a indovinare" con estrema sicurezza (ancora fisso su "2").

---

## 3. Conclusioni Comparative

1.  **Fragilità Semantica:** Tutti i modelli subiscono un impatto devastante dall'anonimizzazione degli header per questo task numerico. Nessun modello è riuscito a inferire correttamente il numero di serbatoi guardando solo i pattern dei dati grezzi nel dataset *baseline*.
2.  **Il paradosso di Mistral:** È il modello più accurato (100%) quando aiutato dagli header, ma il più pericoloso quando non lo è, a causa della sua totale mancanza di calibrazione (sicurezza >0.90 su risposte errate).
3.  **Difficoltà del Task Q2.1:** Rispetto al task Q1 (identificare il tipo di impianto), contare le entità (serbatoi) dai log grezzi si è rivelato molto più difficile per i modelli, che ==sembrano affidarsi quasi esclusivamente ai metadati (nomi colonne) piuttosto che alla dinamica dei valori.==

