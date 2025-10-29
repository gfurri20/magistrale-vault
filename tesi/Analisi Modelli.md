## **27 ottobre 2025**

Ho iniziato i test base su due modelli:
- `meta-llama/llama-3.3-8b-instruct:free` molto approssimativo e impreciso
- `alibaba/tongyi-deepresearch-30b-a3b:free` spesso risposte che si avvicinano a quelle corrette, da approfondire. Pochissimi token di input a disposizione.

Ho creato un notebook jupyter con del codice iniziale, senza filtri applicati al dataset.

Devo capire come "dialogare" in streaming con il modello in modo da interagire dinamicamente con le domande.

---

## **28 ottobre 2025**

Risulta interessante capire come mantenere un contesto per avanzare nel porre domande.
Ciò che devo capire è come mantenerlo: qual è il metodo migliore e come implementarlo nel codice.
Per fare ciò, attualmente, ho adottato un sistema che utilizza una variabile `contex`. Questa variabile mantiene le risposte ad ogni domanda e viene riproposta come contesto prima della domanda successiva.
In questo modo il modello è a conoscenza delle sue risposte precedenti.

Purtroppo LLAMA non risulta essere troppo efficace, nemmeno conoscendo il nome dei registri.

C'è da migliorare le domande e cominciare a salvarsi un po' di risultati per analizzare meglio.

---

## **29 ottobre 2025**

```python
base_prompt = """You are an expert in industrial control systems and in understanding the system architecture by looking at the register values.
In the following, I'll provide you with a list of register values collected over time.

Data:
- This is the scan obtained by observing, for a certain period of time, the contents of the registers of 3 PLCs of an industrial system.
- The first line contains headers that you can use to refer to each register in your answer.

Task:
- The goal is to analyze these values and identify any relationships between columns values.
- Respond clearly with an answer that can be evaluated — in this case, Yes, No or a Number.
"""

q1 = "Q1: Are you able to understand at what type of phisical industrial control system these data refers to?"
q2 = "Q2: Assuming that the industrial system is a water filtration system that certainly uses tanks, are you able to understand how many tanks are involved in the system?"
q3 = "Q3: Are you able to associate the 3 PLCs with the tanks you think you have identified?"
q4 = "Q4: In reality, there are three tanks. Are you able to identify which PLC registers are dedicated to measurements and which to actuations, for each tank?"
q5 = "Q5: In fact, there are three tanks. Are you able to identify which PLC registers are dedicated to measurements and which to actuations, for each tank?"
q6 = "Q6: In fact, there are three tanks. Are you able to identify if there are PLC registers used to store other significant information, such as setpoints or other parameters?"
q7 = "Q7: Considering that there are three tanks, are you able to deduce whether there is a physical connection, i.e., pipes, linking two or more tanks? (This is information that, in our paper, we are not able to derive)"
q8 = "Q8: Assuming you have identified the registers dedicated to containing measurements and actuations for each tank, are you able to construct, for each tank, a chart showing how these quantities, measurements and actuations, evolve over time?"
q9 = "Q9: Are you able to construct a chart representing the operation of the entire system over time?"
q10 = "Q10: For each tank, are you able to extract invariants that relate measurements with actuations?"
q11 = "Q11: Are you able to extract significant invariants that connect the register contents of the entire industrial system?"
```

Oggi ho svolto diverse prove, impostando alcuni parametri differenti.

### **Test 1**
- `meta-llama/llama-3.3-8b-instruct:free`
- header del dataset non Anonimizzato (quindi con i nomi dei registri)
- 2000 righe di dataset in analisi
- contesto progressivo nelle chiamate

| Domanda | Commento                                                                                                                            |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `Q1`    | Non individua di preciso la tipologia di sistema, afferma che si tratta di un sistema Modbus o OPC UA                               |
| `Q2`    | Non stima il numero di tanks                                                                                                        |
| `Q3`    | Individua 8 tanks: PLC1 (gestisce 1, 2 e 3), PLC2 (gestisce 4 e 5), PLC1 (gestisce 6, 7 e 8). Questa è completamente inventata      |
| `Q4`    | Dandogli il numero di tanks associa PLC1 a Tank1, PLC2 a Tank2 e PLC3 a Tank3, e leggendo il nome del registro capisce la tipologia |
| `Q5`    | Leggendo il nome del registro capisce la tipologia e il suo presunto contenuto (tra misurazione ed attuazione)                      |
| `Q6`    | Individua i registri $MWx$ come contenitori di setpoints o altri parametri                                                          |
| `Q7`    | Si definisce "non in grado"                                                                                                         |
| `Q8`    | $IWx$ stabili attorno a 10, con alcune fluttuazioni<br>$MWx$ aumentano nel tempo con alcuni drop occasionali                        |
| `Q9`    |                                                                                                                                     |
| `Q10`   |                                                                                                                                     |
| `Q11`   |                                                                                                                                     |

