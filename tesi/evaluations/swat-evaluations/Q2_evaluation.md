## Valutazione preliminare
La valutazione della domanda [[Questions#Q2]] si è concentrata su tre modelli:

|               Modello                |     Accuracy Preliminare      |
| :----------------------------------: | :---------------------------: |
|    `kwaipilot/kat-coder-pro:free`    |              80%              |
| `tngtech/deepseek-r1t2-chimera:free` |              80%              |
|    `mistralai/devstral-2512:free`    | 100% (su tre risposte valide) |

Il bacino di modelli a chiamate gratuite è soggetto a continui cambiamenti: uno dei modelli utilizzati per l'analisi di Q1, i.e. `grok`, è diventato a pagamento; allo stesso tempo MistralAI ha pubblicato un modello nuovo gratuitamente.

L'analisi si basa sui tre modelli sopra-elencanti, risultati i migliori ad una prima analisi preliminare (interrogazione su 5 iterazioni su dataset con header non anonimizzato).

---

## Valutazione approfondita
La valutazione è stata eseguita sulla domanda [[Questions#Q2.1]], caratterizzata da un dominio di risposta numero $D = [1, 10]$.

Il modello aveva l'obiettivo di individuare il numero di tank che agiscono nel sistema di filtraggio acque, avendo a disposizione un contesto abbastanza semplice (senza spiegazioni approfondite sugli step del sistema).

Per ogni dataset preso in considerazione (i.e. `plc_data_log` e `baseline`), vengono eseguiti due test: uno su header originale e uno su header anonimizzato.

### Dataset `plc_data_log`

|           Modello            | Accuracy (Original Header) | tmp (sec) | Accuracy (Anon. Header) | tmp (sec) |
| :--------------------------: | :------------------------: | --------- | :---------------------: | --------- |
|     `kat-coder-pro:free`     |            ~79%            | 900       |           35%           | 303       |
| `deepseek-r1t2-chimera:free` |            65%             | 1440      |           50%           | 1569      |
|     `devstral-2512:free`     |            100%            | 417       |           0%            | 542       |
Si nota un netto peggioramento al cambiare della natura dell'header.

Nello specifico Devstral peggiora totalmente in quanto sembra fissarsi sempre sulla stessa risposta.

![[Code_Generated_Image(13).png]]

![[Code_Generated_Image(12).png]]

### Dataset `baseline`
