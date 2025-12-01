In questo documento verranno definite le domande testate, in modo da tenere traccia delle modifiche.

Ogni domanda sarà nominata secondo il seguente formato: `Q[CATEGORIA].[VERSIONE]`. Dove `CATEOGORIA` e `VERSIONE` sono interi.

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
