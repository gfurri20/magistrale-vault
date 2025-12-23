In questa fase di test, ai modelli è stato chiesto di identificare il numero di PLC (Programmable Logic Controllers) coinvolti nelle operazioni dell'ICS basandosi esclusivamente sui dataset forniti.

* **Domanda:** *Identify how many PLCs are involved...*
* **Opzioni:** Da '1' a '10'.
* **Risposta Corretta (Ground Truth):** 3 (dedotta dalle performance perfette nello scenario chiaro).
### Report Utilizzati
I report utilizzati in analisi sono compresi nel folder:
- `2025_12_18/*`
### Dataset Utilizzati
1.  **`plc_data_log`**: Dataset compresso a 1501 righe. Versione snella con timestamp e booleani (`true`/`false`).
2.  **`baseline`**: Dataset compresso a 1285 righe. Base di conoscenza standard, più ricca di informazioni storiche.

---

## 1. Analisi su Dataset `plc_data_log`
I risultati evidenziano una forte dipendenza dagli header.
![[Code_Generated_Image(16).png]]

| Modello         | Accuracy (Original Header) | Accuracy (Anon. Header) | Comportamento Principale                                                                    |
| :-------------- | :------------------------: | :---------------------: | :------------------------------------------------------------------------------------------ |
| **Mistral-Dev** |          **100%**          |         **0%**          | Binario. Perfetto con le etichette, fallimento totale senza.                                |
| **Kat-Coder**   |            100%            |          52.6%          | Ottimo con header, perde stabilità senza (mix di risposte).                                 |
| **DeepSeek-R1** |            100%            |           55%           | Simile a Kat-Coder, degrada significativamente ma mantiene una parziale capacità deduttiva. |


**Distribuzione delle Risposte e Confidenza:**
* **Mistral-Dev** si conferma estremamente fragile semanticamente: senza leggere "PLC" negli header, si fissa sulla risposta errata "1", con una confidenza molto alta.
* **DeepSeek e Kat-Coder** mostrano una resilienza parziale, indovinando circa la metà delle volte anche senza header, ma disperdendo le altre risposte tra "1" e "4".

---

## 2. Analisi su Dataset `baseline`
Il dataset in analisi sembra creare maggiore confusione ai modelli, l'accuratezza dui dati con header anon. cala drasticamente!

| Modello | Accuracy (Original Header) | Accuracy (Anon. Header) | Comportamento Principale |
| :--- | :---: | :---: | :--- |
| **Mistral-Dev** | **100%** | **0%** | Conferma il comportamento binario (fisso su "1" senza header). |
| **Kat-Coder** | 100% | 22.2% | Crollo verticale delle performance rispetto al dataset più piccolo. |
| **DeepSeek-R1** | 95% | 0% | Fallimento totale nello scenario anonimo (risponde "9" o "10"). |

![[Code_Generated_Image(17).png]]

**Distribuzione delle Risposte e Confidenza:**
* **DeepSeek-R1** subisce un tracollo inaspettato nel dataset *baseline* anonimizzato: invece di contare i PLC, sembra confondersi con il numero massimo di opzioni o altre entità, rispondendo sistematicamente "9" o "10".
* **Kat-Coder** è l'unico che tenta di mantenere una minima coerenza (22%), ma è chiaramente in difficoltà nel districare i segnali in un dataset più denso senza etichette.

---

## 3. Conclusioni Comparative
Com'era abbastanza prevedibile, i modelli capiscono molto bene il numero di PLCs del sistema avendo a disposizione le etichette dei registri.
Questo perché le etichette comprendono la numerazione della PLC alla quale il registro fa riferimento:
1.  **Header Dependency:** Anche per il conteggio dei PLC (Q3.1), l'anonimizzazione degli header è fatale per l'affidabilità.
2.  **Degrado con Dataset Complesso:** Passando da `plc_data_log` a `baseline`, le capacità di ragionamento sui dati grezzi (Anon. Header) peggiorano per DeepSeek e Kat-Coder. Questo suggerisce che più dati (senza etichette) creano più difficoltà nell'isolare le singole entità (PLC).
3.  **Confronto con Q2.1 (Serbatoi):** I modelli hanno performato meglio nel contare i PLC (Q3.1) rispetto ai serbatoi (Q2.1) nello scenario *Original Header* (tutti al 100% o quasi), ma mostrano le stesse debolezze strutturali quando i nomi delle colonne vengono rimossi.Mistral-Dev￼￼ è l'esempio più lampante di modello "lazy" che funziona solo con metadati espliciti.

==Questo dimostra come i modelli in analisi siano incapaci di inferire, da dati numerici temporali grezzi, alcune caratteristiche fondamentali dell'ICS.==