
## 1. Introduzione e Selezione dei Modelli
L'obiettivo dell'analisi è valutare le prestazioni di modelli LLM nell'inferire la tipologia di un sistema di controllo industriale (ICS) fisico basandosi sui log dei dati.
Dopo una fase preliminare su 5 modelli (durata circa 4 ore), sono stati selezionati i due modelli più performanti per un'analisi approfondita:

1.  **`x-ai/grok-4.1-fast:free`** (Accuracy preliminare: 100%)
2.  **`tngtech/deepseek-r1t2-chimera:free`** (Accuracy preliminare: 100%)

L'analisi successiva si concentra su due variabili principali: la complessità del dominio di risposta ([[Questions#Q1.1]] vs [[Questions#Q1.2]]) e l'anonimizzazione degli header del dataset.

---

## 2. Metodologia di Test
Sono stati eseguiti quattro tipologie di test incrociando le seguenti condizioni:
* **Domande:**
    * **[[Questions#Q1.1]] (Dominio Semplificato):** 5 opzioni di risposta + risposta nulla.
    * **[[Questions#Q1.2]] (Dominio Complesso):** 11 opzioni di risposta, incluse categorie semanticamente simili (es. *Water Purification* vs *Wastewater Treatment*).
* **Condizioni Dataset:**
    * **Original Header:** Nomi delle colonne visibili (es. nomi dei sensori).
    * **Anon. Header:** Nomi delle colonne rimossi, lasciando solo i dati grezzi.

### Report Utilizzati
I report utilizzati in analisi sono compresi nelle seguenti folder:
- `2025_12_02/*`
- `2025_12_03/*`
### Dataset Utilizzati
1.  **`plc_data_log`**: Dataset compresso a 751 righe. Versione snella con timestamp e booleani (`true`/`false`).
2.  **`baseline`**: Dataset compresso a 1285 righe. Base di conoscenza standard, più ricca di informazioni storiche.

---

## 3. Risultati: Dataset `plc_data_log`

### 3.1 Test Q1.1 (Dominio Semplificato)
In questo contesto, DeepSeek si dimostra nettamente più affidabile di Grok, mantenendo una soglia di sicurezza anche senza header.

| Modello | Accuracy (Original Header) | Accuracy (Anon. Header) |
| :--- | :---: | :---: |
| **DeepSeek** | **95%** | **~79%** |
| **Grok** | 25% | 15% |

![[2025_12_02_q1_responses_img1.png]]

![[2025_12_02_q1_responses_img2.png]]

**Analisi:**
* **Grok:** Mostra un alto tasso di indecisione e imprecisione. La dispersione delle risposte è elevata.
* **DeepSeek:** Conferma la sua robustezza. Anche con header anonimi, il calo non è drastico.

### 3.2 Test Q1.2 (Dominio Complesso)
L'aumento della complessità del dominio delle risposte (11 opzioni) causa un crollo drastico delle prestazioni per entrambi i modelli.

| Modello  | Accuracy (Original Header) | Accuracy (Anon. Header) |
| :------: | :------------------------: | :---------------------: |
| DeepSeek |           ~26.3%           |          ~5.3%          |
|   Grok   |             0%             |           0%            |

![[2025_12_02_q1_responses_img4.png]]

![[2025_12_02_q1_responses_img5.png]]

**Analisi Errori:**
* **DeepSeek:** Si confonde spesso con *Wastewater Treatment Facility*, un sistema molto simile all'ICS corretto (*Water Purification*). Con header anonimi vira su *Chemical Batch Reactor*. Tuttavia, dimostra di dedurre la "macro-natura" del sistema.
* **Grok:** Fallisce completamente. Risponde con alta confidenza *HVAC & Building Automation*, un sistema di natura totalmente diversa.

---

## 4. Risultati: Dataset `baseline` (Migliorativo)

L'utilizzo del dataset `baseline` migliora significativamente le prestazioni generali, specialmente per Grok nello scenario con header.

### 4.1 Test Q1.1 (Dominio Semplificato)
DeepSeek raggiunge la perfezione. Grok mostra una dipendenza critica dalla presenza degli header semantici.

| Modello | Accuracy (Original Header) | Accuracy (Anon. Header) |
| :--- | :---: | :---: |
| **DeepSeek** | **100%** | **100%** |
| **Grok** | 95% | 40% |

![[2025_12_02_q1_responses_img7.png]]

**Analisi:**
* **DeepSeek:** Infallibile in entrambi gli scenari.
* **Grok:** Crolla dal 95% al 40% rimuovendo gli header. Questo indica che Grok dipende fortemente dalle etichette delle colonne per orientarsi.

### 4.2 Test Q1.2 (Dominio Complesso)
Nonostante il dataset migliore, la complessità del dominio Q1.2 rimane un ostacolo insormontabile per un'alta affidabilità.

| Modello | Accuracy (Original Header) | Accuracy (Anon. Header) |
| :--- | :---: | :---: |
| **DeepSeek** | **40%** | **20%** |
| **Grok** | 20% | 0% |

![[2025_12_02_q1_responses_img10.png]]

**Analisi:**
* **DeepSeek:** Riesce a identificare correttamente l'impianto nel 40% dei casi con header. Senza header, scende al 20%, confondendosi nuovamente con *Chemical Batch Reactor* e *Wastewater Treatment*.
* **Grok:** Nello scenario anonimo collassa completamente (0% accuracy), fissandosi erroneamente su *HVAC & Building Management* (17 volte su 20).

---

## 5. Analisi della Confidenza e Conclusioni

### Overconfidence (Eccesso di Sicurezza)
Un dato critico emerso nei test complessi (Q1.2) è l'eccessiva sicurezza dei modelli anche in caso di errore.
* **DeepSeek:** Mantiene una confidenza molto alta (>0.8) sia quando indovina sia quando sbaglia.
* **Grok:** Mostra confidenza altissima (spesso >0.9) per risposte palesemente errate, specialmente nello scenario anonimo.
* **Implicazione:** Questo comportamento è pericoloso in ambito industriale, poiché l'operatore non riceve segnali di incertezza dal modello.

### Sintesi Finale
1.  **DeepSeek vs Grok:** DeepSeek è strutturalmente superiore nell'analisi di pattern numerici grezzi. Grok si comporta come un "lazy learner" che necessita di etichette esplicite.
2.  **Impatto della Complessità:** Il passaggio da un dominio semplice a uno complesso (Q1.2) è stato "fatale" per l'accuratezza, evidenziando i limiti attuali nell'analisi fine-grained senza contesto esplicito.
3.  **Qualità del Dataset:** Il dataset `baseline` permette performance migliori rispetto al `plc_data_log`, ma non risolve i problemi strutturali di allucinazione di Grok sui dati anonimi.