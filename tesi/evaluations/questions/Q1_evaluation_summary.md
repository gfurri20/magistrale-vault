# Report Valutazione Modelli ICS - Q1

## 1. Introduzione e Selezione dei Modelli

L'analisi è iniziata con una valutazione preliminare su 5 modelli per rispondere al quesito **Q1**: dedurre il tipo di sistema di controllo industriale (ICS) fisico basandosi sui dati forniti.

|**Modello**|**Accuracy**|**Note**|
|---|---|---|
|**x-ai/grok-4.1-fast:free**|**100%**|Selezionato per analisi approfondita 4|
|**tngtech/deepseek-r1t2-chimera:free**|**100%**|Selezionato per analisi approfondita 5|
|openai/gpt-oss-20b:free|66,7%|Scartato|
|meta-llama/llama-3.3-70b-instruct:free|11,1%|Scartato|
|nvidia/nemotron-nano-12b-v2-vl:free|0%|Scartato|
L'analisi successiva si concentra esclusivamente su **Grok** e **DeepSeek**, introducendo la variante dell'anonimizzazione degli header (nomi delle colonne) per testare la capacità di ragionamento sui dati grezzi.

---
## 2. Metodologia di Test Approfondita
Sono stati eseguiti quattro tipologie di test incrociando due variabili: la complessità della domanda (Q1.1 vs Q1.2) e la visibilità degli header del dataset