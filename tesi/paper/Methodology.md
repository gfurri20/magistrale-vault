Qua va sviluppata tutta la parte di metodologia.

Intanto volevo annotarmi la differenza tra le tre metriche che ho incluso nel file di log:
- **accuracy (successo reale)** - misura la percentuale di risposte corrette su tutte le iterazioni (gli errori e le incorrette collassano in un'unica categoria)
- **reliability (affidabilità tecnica)** - misura la percentuale di risposte valide (corrette + incorrette) rispetto a tutte le iterazioni
- **precision (ragionamento corretto)** - misura la percentuale di risposte corrette ignorando gli errori, visti come non colpa del modello

---

Metodologia, domande, obiettivo dell'analisi, tramite per raggiungere l'obiettivo

---

Cosa compone una metodologia?
Ricercare e prendere spunto da paper pubblicati.

---

Quali domande proporre al modello?

**Domande generali** che possono essere poste su dataset di sistemi eterogenei.
Una domanda generale possiede un dominio di risposta costante per ogni ICS e risulta essere un primo movimento verso la ricognizione semantica.
Quali sono le caratteristiche di una domanda generale?
- dominio di risposta costante
- non fa riferimento a possibili componenti specifici del sistema
- cerca informazioni che OGNI sistema possiede (e.g. numero di PLC oppure eventuali componenti fisici aggiuntivi)
- la cross-valutazione ci permette di capire quale tipologia di dataset si adatti maggiormente per un'analisi semantica

**Domande specifiche** che mirano ad ottenere risposte su caratteristiche precise ed eventualmente uniche del sistema.
Una domanda specifica mira ad identificare le caratteristiche uniche del sistema in analisi, approfondendo la ricognizione semantica generale.
Quali sono le caratteristiche di una domanda generale?
- può esplicitare elementi fisici/software specifici del sistema in analisi
- il dominio di risposta può essere più dettagliato in riferimento al sistema
- non esiste cross-valutazione tra tipologie di ICS

Individuare le domande generale da porre a tutti i sistemi.
Individuare, per ogni dataset (sistema) in analisi, le domande specifiche per approfondire la ricognizione semantica.



