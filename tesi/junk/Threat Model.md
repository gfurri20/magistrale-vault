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

## Obiettivo
L'obiettivo dell'attaccante è quello di inferire le caratteristiche dell'ICS target, tramite interrogazioni a LLM, sfruttando i dump ottenuti.
Un attacco viene considerato di successo se (qua da capire se possiamo effettivamente parlare di successo, solo se accuracy è 100%, introduco degli intervalli? da valutare).

---

In questa sezione definiamo formalmente le capacità dell'avversario, i vettori di acquisizione dati e il ruolo delle Large Language Models (LLM) come oracolo per l'inferenza semantica.

Consideriamo un attaccante ($A$) motivato dalla ricognizione semantica dell'infrastruttura ICS target. L'obiettivo ultimo di $A$ è acquisire una comprensione profonda del processo fisico per pianificare futuri attacchi "stealth".

L'avversario non possiede alcuna conoscenza a priori della topologia di rete, delle specifiche del processo industriale o della mappatura di memoria delle PLC.

Assumiamo che $A$ abbia successo nell'ottenere dati storici grezzi dal sistema. Definiamo due scenari distinti basati sulla natura dell'esfiltrazione e sulla qualità dei meta-dati disponibili:

- **Scenario A: Network Scanning (Unlabeled Dataset).** L'attaccante ha accesso alla rete e interroga le PLC in un intervallo di tempo $T$.
    - $A$ ottiene serie temporali di valori grezzi associati solo a indirizzi di memoria fisici la cui label non fornisce informazioni semantiche sul sistema.

- **Scenario B: Physical/Engineering Dump (Labeled Dataset).** L'attaccante ottiene il dump tramite supporti fisici (es. USB smarrita, furto di hardware, insider threat).
    - Oltre alle serie temporali, $A$ recupera le etichette dei registri, con la possibilità di ottenere informazioni semantiche dai soli nomi.        

Si assume che $A$ abbia accesso a Large Language Models (LLM). L'attaccante utilizza il modello in modalità **"One-Shot Inference"**. La LLM viene utilizzata come un motore di ragionamento generalista per correlare i pattern numerici con la conoscenza ingegneristica presente nel suo training set.

L'attaccante sottoporrà alcune domande sequenziali al modello, con l'obiettivo di **individuare le caratteristiche del sistema**.
La sequenzialità delle domande, impone l'arricchimento del prompt con il contesto delle domande precedenti. (da valutare la frase)

