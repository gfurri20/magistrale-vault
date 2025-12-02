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

Dataset di analisi: `plc_data_log_20251128_212142_compressed_751_rows.csv`
Ovvero il dataset `plc_data_log_20251128_212142.csv` elaborato a 751 righe.

Sono stati eseguite quattro test, che si differenziano per domanda posta e tipologia di header (**Original Header** oppure **Anon. Header**):
- $T_{\texttt{Q1.1}}$ - test su domanda [[magistrale-vault/tesi/Domande#Q1.1|Q1.1]] e dataset **non** anonimizzato
- $T_{\texttt{Q1.1}}^{\texttt{A}}$ - test su domanda [[magistrale-vault/tesi/Domande#Q1.1|Q1.1]] e dataset anonimizzato
- $T_{\texttt{Q1.2}}$ - test su domanda [[magistrale-vault/tesi/Domande#Q1.2|Q1.2]] e dataset **non** anonimizzato
- $T_{\texttt{Q1.2}}^{\texttt{A}}$ - test su domanda [[magistrale-vault/tesi/Domande#Q1.2|Q1.2]] e dataset anonimizzato

Di seguito per ogni test verranno riportati i risultati ottenuti.

### Test su Q1.1
Test sulla domanda con Dominio di risposta semplificato: 5 risposte possibili di natura diversa tra loro + la risposta nulla.

Dall'analisi dei risultati si evince che DeepSeek sembra essere un modello migliore rispetto a Grok in questo contesto, con dei risultati ben migliori e precisi.
#### Distribuzione dei test
DeepSeek si dimostra essere più affidabile ottenendo una percentuale di risposte corrette di gran lunga maggiore rispetto a Grok.

| Modello  | Accuracy (Original Header) | Accuracy (Anon. Header) |
| :------: | :------------------------: | :---------------------: |
| DeepSeek |            95%             |          ~79%           |
|   Grok   |            25%             |           15%           |
**Accuracy** calcola il successo del modello sulle risposte che non vanno in errore (errore tecnico nella risposta).

![[2025_12_02_q1_responses_img1.png]]
#### Distribuzione delle risposte
Grok ha una dispersione maggiore nelle risposte, soprattutto con Anon. Header, sottolinea la poca precisione ed un alto tasso di indecisione.

DeepSeek, nonostante l'Anon. Header, non peggiora drasticamente il tasso delle risposte corrette, mantenendo una certa soglia di sicurezza.

![[2025_12_02_q1_responses_img2.png]]
#### Confidenza dei modelli

DeepSeek si conferma un modello robusto, la box delle risposte corrette è molto compatta con dei baffi ridotti.
Questo sottolinea un'ottima coerenza e fiducia nelle proprie risposte corrette.
Con Anon. Header la confidenza crea una box più ampia e posta leggermente sotto la box delle risposte corrette, ciò significa che quando sbaglia lo fa con una confidenza di risposta minore.

Grok presenta delle box rosse molto compatte, ad un livello pari di quelle verdi. Vuol dire che individua con un alta confidenza risposte sbagliate.
Risulta essere un modello confuso ed impreciso.
![[2025_12_02_q1_responses_img3.png]]

### Test su [[magistrale-vault/tesi/Domande#Q1.2|Q1.2]]
Q1.2 non cambia il testo della domanda, ma bensì amplia il dominio delle risposte, includendo possibilità molto più simili, di natura, al sistema di riferimento.

Il tasso di successo dei modelli in esame cala drasticamente, sottolineando come un aumento di complessità del dominio (ancora limitato) di risposte possa essere "fatale".
Se l'obiettivo è quello di rispondere su un dominio illimitato, allora i segnali non son positivi.

#### Distribuzione dei test
L'**Accuracy** di entrambi i modelli cala drasticamente, arrivando, nel caso di Grok a 0%.

| Modello  | Accuracy (Original Header) | Accuracy (Anon. Header) |
| :------: | :------------------------: | :---------------------: |
| DeepSeek |            25%             |           10%           |
|   Grok   |             0%             |           0%            |
![[2025_12_02_q1_responses_img4.png]]
#### Distribuzione delle risposte
DeepSeek - Original Header si confonde spesso con "Wastewater Treatment Facility", un sistema di natura molto simile all'ICS in analisi.
Con l'anonimizzazione dell'header la risposta più comune diventa "Chemical Batch Reactor".
DeepSeek confonde la risposta corretta con i due sistemi di natura più simile tra le possibile risposte, dimostrando, comunque, la capacità di dedurre a grandi linee la (macro)-natura del sistema in esame.

Grok, con un'alta confidenza, risponde la maggior parte delle volte "HVAC & Building Automation", sistema per natura diverso.
Con Anon. Header Grok si fissa su tale risposta.

![[2025_12_02_q1_responses_img5.png]]
#### Confidenza dei modelli
Entrambi i modelli mostrano una confidenza nello sbagliare.
![[2025_12_02_q1_responses_img6.png]]