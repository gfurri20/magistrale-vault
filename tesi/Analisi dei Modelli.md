## Esecuzione 2025_11_29-13_51_11
Valutazione di 5 modelli e delle loro prestazioni nel rispondere a `Q1` con **dominio risposte definito e limitato**.

Analisi su **dataset NON anonimizzato**.

```
Q1: Infer, based on data provided, what type of phisical Industrial Control System (ICS) between the following options: ['Power Generation Plant', 'Manufacturing Assembly Line', 'Oil and Gas Refinery', 'Water Purification Plant', 'Nuclear Power Plant', 'Not Identifiable']
```

Dominio delle risposte:
```python
D = [
	'Power Generation Plant',
	'Manufacturing Assembly Line',
	'Oil and Gas Refinery',
	'Water Purification Plant',
	'Nuclear Power Plant',
	'Not Identifiable'
]
```

Tempo totale di valutazione: 15048 secondi **~4 ore**.

Risultati su un totale di **10 interrogazioni per modello**:

| Modello                                  | Accuracy | # Corrette | # Errori | Tempo     |
| ---------------------------------------- | -------- | ---------- | -------- | --------- |
| `x-ai/grok-4.1-fast:free`                | **100%** | 10         | 0        | **393,5** |
| `tngtech/deepseek-r1t2-chimera:free`     | **100%** | 9          | 1        | 1044,6    |
| `openai/gpt-oss-20b:free`                | 66,7%    | 4          | 4        | 1331,7    |
| `meta-llama/llama-3.3-70b-instruct:free` | 11.1%    | 1          | 1        | 2113,6    |
| `nvidia/nemotron-nano-12b-v2-vl:free`    | 0%       | 0          | 6        | 10164,7   |

Si contraddistinguono due modelli sui quali sarà interessante approfondire l'analisi anche utilizzando il dataset con header anonimizzato.

### Osservazioni
- il dominio delle risposte è molto banale e piccolo, questo comporta due osservazioni
	- i modelli che sbagliano potrebbero essere già considerati "incapaci"
	- i modelli che fanno giusto potrebbero essere stati troppo aiutati
- sul totale degli errori (12/50 interrogazioni) la divisione sottolinea come l'unico errore avvenuto riguarda la ricezione di un JSON non formattato correttamente da parte del modello:
	- `201: JSON parsing error` - 12
	- `101: Model error` - 0
	- `301: missing short answer error` - 0
- devo capire come poter dir qualcosa sulla confidenza espressa per interrogazione dai modelli: la considero tutta insieme o solo per risposte della stessa natura?

---

## Esecuzione su [[magistrale-vault/tesi/Domande#Q1|Q1]]
L'obiettivo è quello di concentrare l'analisi sui modelli migliori risultanti dal capitolo precedente [[Analisi dei Modelli#Esecuzione 2025_11_29-13_51_11]].

Modelli presi in considerazione:
- `x-ai/grok-4.1-fast:free`
- `tngtech/deepseek-r1t2-chimera:free`

Sono stati eseguite quattro test, che si differenziano per domanda posta e tipologia di header (**Original Header** oppure **Anon. Header**):
- $T_{\texttt{Q1.1}}$ - test su domanda [[magistrale-vault/tesi/Domande#Q1.1|Q1.1]] e dataset **non** anonimizzato
- $T_{\texttt{Q1.1}}^{\texttt{A}}$ - test su domanda [[magistrale-vault/tesi/Domande#Q1.1|Q1.1]] e dataset anonimizzato
- $T_{\texttt{Q1.2}}$ - test su domanda [[magistrale-vault/tesi/Domande#Q1.2|Q1.2]] e dataset **non** anonimizzato
- $T_{\texttt{Q1.2}}^{\texttt{A}}$ - test su domanda [[magistrale-vault/tesi/Domande#Q1.2|Q1.2]] e dataset anonimizzato

Di seguito per ogni test verranno riportati i risultati ottenuti.

### Dataset plc_data_log
Dataset di analisi: `plc_data_log_20251128_212142_compressed_751_rows.csv`
Ovvero il dataset `plc_data_log_20251128_212142.csv` elaborato a 751 righe.

Il dataset `plc_data_log_20251128_212142.csv` risulta essere una versione più snella e compatta di `baseline.csv`, arricchita però dal timestamp delle letture del registro.
I valori Booleani sono rappresentanti come `true` o `false` e non `1` o `0`.
Inoltre sono stati rimossi i valori dei registri `prev_*`.
#### Test su Q1.1
Test sulla domanda con Dominio di risposta semplificato: 5 risposte possibili di natura diversa tra loro + la risposta nulla.

Dall'analisi dei risultati si evince che DeepSeek sembra essere un modello migliore rispetto a Grok in questo contesto, con dei risultati ben migliori e precisi.
##### Distribuzione dei test
DeepSeek si dimostra essere più affidabile ottenendo una percentuale di risposte corrette di gran lunga maggiore rispetto a Grok.

| Modello  | Accuracy (Original Header) | Accuracy (Anon. Header) |
| :------: | :------------------------: | :---------------------: |
| DeepSeek |            95%             |          ~79%           |
|   Grok   |            25%             |           15%           |
**Accuracy** calcola il successo del modello sulle risposte che non vanno in errore (errore tecnico nella risposta).

![[2025_12_02_q1_responses_img1.png]]
##### Distribuzione delle risposte
Grok ha una dispersione maggiore nelle risposte, soprattutto con Anon. Header, sottolinea la poca precisione ed un alto tasso di indecisione.

DeepSeek, nonostante l'Anon. Header, non peggiora drasticamente il tasso delle risposte corrette, mantenendo una certa soglia di sicurezza.

![[2025_12_02_q1_responses_img2.png]]
##### Confidenza dei modelli
DeepSeek si conferma un modello robusto, la box delle risposte corrette è molto compatta con dei baffi ridotti.
Questo sottolinea un'ottima coerenza e fiducia nelle proprie risposte corrette.
Con Anon. Header la confidenza crea una box più ampia e posta leggermente sotto la box delle risposte corrette, ciò significa che quando sbaglia lo fa con una confidenza di risposta minore.

Grok presenta delle box rosse molto compatte, ad un livello pari di quelle verdi. Vuol dire che individua con un alta confidenza risposte sbagliate.
Risulta essere un modello confuso ed impreciso.
![[2025_12_02_q1_responses_img3.png]]

#### Test su [[magistrale-vault/tesi/Domande#Q1.2|Q1.2]]
Q1.2 non cambia il testo della domanda, ma bensì amplia il dominio delle risposte, includendo possibilità molto più simili, di natura, al sistema di riferimento.

Il tasso di successo dei modelli in esame cala drasticamente, sottolineando come un aumento di complessità del dominio (ancora limitato) di risposte possa essere "fatale".
Se l'obiettivo è quello di rispondere su un dominio illimitato, allora i segnali non son positivi.

##### Distribuzione dei test
L'**Accuracy** di entrambi i modelli cala drasticamente, arrivando, nel caso di Grok a 0%.

| Modello  | Accuracy (Original Header) | Accuracy (Anon. Header) |
| :------: | :------------------------: | :---------------------: |
| DeepSeek |            25%             |           10%           |
|   Grok   |             0%             |           0%            |
![[2025_12_02_q1_responses_img4.png]]
##### Distribuzione delle risposte
DeepSeek - Original Header si confonde spesso con "Wastewater Treatment Facility", un sistema di natura molto simile all'ICS in analisi.
Con l'anonimizzazione dell'header la risposta più comune diventa "Chemical Batch Reactor".
DeepSeek confonde la risposta corretta con i due sistemi di natura più simile tra le possibile risposte, dimostrando, comunque, la capacità di dedurre a grandi linee la (macro)-natura del sistema in esame.

Grok, con un'alta confidenza, risponde la maggior parte delle volte "HVAC & Building Automation", sistema per natura diverso.
Con Anon. Header Grok si fissa su tale risposta.

![[2025_12_02_q1_responses_img5.png]]
##### Confidenza dei modelli
Entrambi i modelli mostrano una confidenza nello sbagliare.
![[2025_12_02_q1_responses_img6.png]]

### Dataset baseline
Dataset di analisi: `baseline_compressed_1285_rows.csv` Ovvero il dataset `baseline.csv` elaborato e compresso a 1285 righe.

Questo dataset rappresenta la base di conoscenza standard, contenente una quantità maggiore di informazioni storiche rispetto alla versione `plc_data_log`. Mantiene la struttura originale dei dati ma in forma compressa per ottimizzare l'analisi.

#### Test su Q1.1
Test sulla domanda con Dominio di risposta semplificato: 5 risposte possibili di natura diversa tra loro + la risposta nulla.

Dall'analisi dei risultati si evince che l'utilizzo del dataset `baseline` ha migliorato significativamente le prestazioni generali rispetto al dataset `plc_data_log`, specialmente per Grok nello scenario con header. DeepSeek raggiunge la perfezione in entrambi gli scenari.

##### Distribuzione dei test
DeepSeek si conferma infallibile, ottenendo il 100% di risposte corrette indipendentemente dall'anonimizzazione. Grok mostra un netto miglioramento quando i nomi delle colonne sono presenti (95%), ma crolla significativamente quando vengono rimossi.

| Modello     | Accuracy (Original Header)     | Accuracy (Anon. Header)     |
| ----------- | ------------------------------ | --------------------------- |
| DeepSeek    | 100%                           | 100%                        |
| Grok        | 95%                            | 40%                         |
**Accuracy** calcola il successo del modello sulle risposte che non vanno in errore (errore tecnico nella risposta).

![[2025_12_02_q1_responses_img7.png]]

##### Distribuzione delle risposte
Nello scenario **Original Header**, entrambi i modelli convergono quasi perfettamente sulla risposta corretta ("Water Purification Plant"), con Grok che commette un solo errore ("Manufacturing Assembly Line").

Nello scenario **Anon. Header**, la differenza diventa abissale. Mentre DeepSeek rimane ancorato alla risposta corretta senza esitazioni, Grok entra in confusione: le sue risposte si disperdono tra "Power Generation Plant" e "Manufacturing Assembly Line", con un aumento dei casi "Not Identifiable". Questo indica che Grok dipende fortemente dalle etichette semantiche delle colonne per orientarsi nel dataset `baseline`.

![[2025_12_02_q1_responses_img8.png]]

##### Confidenza dei modelli
DeepSeek mostra una confidenza eccezionalmente alta e stabile (scatole verdi compatte verso l'alto) in entrambi gli scenari. La sua sicurezza è pienamente giustificata dalla sua accuratezza del 100%.

Grok, nello scenario Anonimo (grafico in basso), evidenzia il suo problema di calibrazione: le scatole rosse (risposte errate) si sovrappongono in termini di confidenza a quelle verdi. Ciò significa che spesso fornisce risposte errate (come "Power Generation") con una confidenza medio-alta (attorno a 0.8), dimostrando di non essere "consapevole" di quando sta analizzando male i dati numerici con header anonimizzato.

![[2025_12_02_q1_responses_img9.png]]
#### Test su Q1.2
Non ho ancora eseguito il codice...
