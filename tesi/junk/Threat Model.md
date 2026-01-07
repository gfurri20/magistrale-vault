L'Attaccante ha bucato un ICS e vuole identificare delle info (process comprehension) in modo da lanciare attacchi "stealthy".

Obiettivo: identificare le caratteristiche del sistema

Usenix Security

Assumiamo
L'attaccante possieda alcune conoscenze che si vogliono migliorare con l'ausilio di LLM:
1. scansione dei registri di sistema, sia con etichetta che senza

Deve rispondere a delle domande rispetto al sistema target.

Qual è il modo migliore per passare informazioni?
- formato del dataset (strutturato o no) \[Invertire gli assi del CSV\]
- contesto o no? Risposta secca alle domande precedenti (a cascata)

TODO
1. Aumentare il numero di dataset, anche di sistemi diversi -> (semplificazione del dominio di risposta) modificare il dominio includendo solo "macro-domini". Proseguo con le domande originali
2. Inserire nell'output i dati di ragionamento della risposta
3. Bozza threat model ed eventuale related work

## Threat Model Description
Un thread model deve specificare:
- le abilità dell'attaccante
- le conoscenze a priori dell'attaccante
- l'obiettivo dell'attaccante
- 

