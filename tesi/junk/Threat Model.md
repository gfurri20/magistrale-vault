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

## Attaccante
Consideriamo un attaccante il cui obiettivo è la ricognizione semantica dell'ICS target, con il fine ultimo di organizzare attacchi "stealth" allo stesso.

L'attaccante non possiede una conoscenza a priori della topologia del sistema, del processo industriale specifico o della mappatura dei registri.

L'attaccante è in grado di ottenere il dump dei valori dei registri del sistema di tutte le PLCs in due modalità:
1. scansione di rete e registrazione dei valori dei registri in un determinato intervallo di tempo;
2. ottenimento dei dump tramite supporto fisico a causa di smarrimento o esfiltrazione.
Nel primo caso assumiamo che l'attaccante possieda un dataset di serie temporali senza nomi dei registri del sistema; al contrario, nel secondo, assumiamo che l'attaccante possieda un dataset di serie temporali con annessi i nomi dei registri del sistema a cui la serie temporale fa riferimento.

## LLM Interrogation
Assumiamo che l'attaccante abbia accesso a LLM allo stato dell'arte, sia commerciali che open-source già addestrate e pronte all'uso per interrogazioni "one-shot".

## Security Goal


