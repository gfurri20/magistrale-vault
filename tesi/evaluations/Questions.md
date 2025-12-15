In questo documento verranno definite le domande testate, in modo da tenere traccia delle modifiche.

Ogni domanda sarà nominata secondo il seguente formato: `Q[CATEGORIA].[VERSIONE]`. Dove `CATEOGORIA` e `VERSIONE` sono interi.

# Contesto
Le domande successive a Q1, necessitano di informazioni aggiuntive per fare in modo che il modello formuli una risposta.
Posso definire queste informazioni: **Contesto**

Ora ==devo capire come dare questo contesto==.

Potrebbe essere dato correttamente: Contesto **indotto**
Oppure potrei chiedere al modello stesso di fornirmi il contesto, a partire dalla domanda precedente: Contesto **ricavato**.

Per ora mi concentrerò su valutazioni a partire da contesto indotto, esso sarà inserito direttamente nel prompt di richiesta valutazione per ogni modello.

# Q1
Identificazione della tipologia di ICS fisico.

## Q1.1
Dominio ristretto 5 possibilità + quella nulla.

```python
Q1.1: Infer, based on data provided, what type of phisical Industrial Control System (ICS) between the following options: ['Power Generation Plant', 'Manufacturing Assembly Line', 'Oil and Gas Refinery', 'Water Purification Plant', 'Nuclear Power Plant', 'Not Identifiable']
```

## Q1.2
Dominio ristretto 10 possibilità + quella nulla. Alcune possibilità sono molto simili, come dinamiche (e.g. Wastewater Treatment Facility), a quella corretta.

```python
Q1.2: Infer, based on data provided, what type of phisical Industrial Control System (ICS) between the following options: ['Power Generation Plant', 'Manufacturing Assembly Line', 'Oil and Gas Refinery', 'Water Purification Plant', 'Nuclear Power Plant', 'Chemical Batch Reactor', 'HVAC & Building Management', 'Automated Bottling Plant', 'Smart Grid Substation', 'Wastewater Treatment Facility', 'Not Identifiable']
```

---
# Q2
Identificazione del numero di tanks utilizzate nel sistema.

**Contesto indotto**: Assumere che l'ICS di riferimento sia un sistema di filtraggio dell'acqua: Water Purification Plant.

## Q2.1
Dominio a 10 numeri: $D = [1, 10]$
```python
Q2.1: Only based on data provided, identify how many tanks are involved during the operations of the ICS under consideration between the following options: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Contesto:
```
The ICS is a simplified version of a Water Purification Plant.
It produces filtered water through filtration and reverse osmosis processes.
```

---

# Q3
Identificazione del numero di PLCs coinvolte nel sistema.

**Contesto indotto**: Assumere che l'ICS di riferimento sia un sistema di filtraggio dell'acqua che sfrutta tre tank di dimensioni diverse.

Si potrebbe aumentare il contesto spiegando le funzionalità dei tank per ognuna delle tre fasi di filtraggio (1. filtraggio, 2. reverse osmosis, 3. backtank).

## Q3.1
Dominio a 10 numeri: $D = [1, 10]$.
```
Q3.1: Based on provided data and context, identify how many PLCs are involved during the operations of the ICS under consideration between the following options: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Contesto:
```
The ICS is a simplified version of a Water Purification Plant.
It produces filtered water through filtration and reverse osmosis processes.
The operations involve three water tanks having varying capacities.
```

## Q3.2
Si può creare un dominio che permetta al modello di rispondere associando PLC a serbatoio?

```
{T1:PLC1, T2:PLC2, T3:PLC3}
```

E' anche vero che sono solo nomi, sarebbe la stessa cosa se si producesse:

```
{T1:PLC10, T2:PLC3, T3:PLC2}
```

Bisognerebbe attribuire delle caratteristiche alle PLC in modo tale che l'assegnazione abbia un senso. Come? #TODO



