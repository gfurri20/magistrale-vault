Qua va sviluppata tutta la parte di metodologia.

Intanto volevo annotarmi la differenza tra le tre metriche che ho incluso nel file di log:
- **accuracy (successo reale)** - misura la percentuale di risposte corrette su tutte le iterazioni (gli errori e le incorrette collassano in un'unica categoria)
- **reliability (affidabilità tecnica)** - misura la percentuale di risposte valide (corrette + incorrette) rispetto a tutte le iterazioni
- **precision (ragionamento corretto)** - misura la percentuale di risposte corrette ignorando gli errori, visti come non colpa del modello