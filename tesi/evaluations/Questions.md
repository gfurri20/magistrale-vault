In questo documento verranno definite le domande testate, in modo da tenere traccia delle modifiche.

Ogni domanda sarà nominata secondo il seguente formato: `Q[CATEGORIA]-[VERSIONE]`. Dove `CATEOGORIA` e `VERSIONE` sono interi.

# Contesto
Le domande successive a Q1, necessitano di informazioni aggiuntive per fare in modo che il modello formuli una risposta.
Tale mole di informazioni è definita come **CONTESTO**.

Il contesto sarà incluso nel prompt della domanda e corrisponde alle *semplici risposte alle domande precedenti*.

Di seguito il contesto specifico per [[Questions#Q3-1]]:
```
...
# Context
The ICS is catagorized as a Water & Wastewater System. The operations involve three water tanks.
...
```

Le informazioni contestuali vengono incluse nella domanda manualmente, alla creazione.
Per questo motivo lo definirei **CONTESTO INDOTTO**.
# Q1
Identificazione della categoria di appartenenza del sistema sotto valutazione.

## Q1-1
Il dominio di risposta consiste in un insieme di macro-categorie di sistemi ICS.

```
Q1-1: Classify the physical Industrial Control System (ICS) into one of the following categories: ['Energy & Power System', 'Oil, Gas & Chemicals System', 'Manufacturing System', 'Water & Wastewater System', 'Building Automation System', 'Not Identifiable']
```

---
# Q2
Identificazione del numero di serbatoi d'acqua utilizzati nel sistema.
## Q2-1
Dominio a 10 numeri: $D = [0, 10]$
```
Q2-1: Identify how many water tanks are involved during the operations of the ICS under consideration between the following options: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'].
```

Contesto:
```
The ICS is categorized as a Water & Wastewater System.
```

---

# Q3
Identificazione del numero di PLCs coinvolte nel sistema.
## Q3-1
Dominio a 10 numeri: $D = [0, 10]$.
```
Q3-1: Identify how many PLCs are involved during the operations of the ICS under consideration between the following options: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'].
```

Contesto:
```
The ICS is categorized as a Water & Wastewater System.
The operations involve three water tanks.
```

## Q3-2
Si può creare un dominio che permetta al modello di rispondere associando PLC a serbatoio?

```
{T1:PLC1, T2:PLC2, T3:PLC3}
```

E' anche vero che sono solo nomi, sarebbe la stessa cosa se si producesse:

```
{T1:PLC10, T2:PLC3, T3:PLC2}
```

Bisognerebbe attribuire delle caratteristiche alle PLC in modo tale che l'assegnazione abbia un senso. Come? #TODO



