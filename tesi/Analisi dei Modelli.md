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