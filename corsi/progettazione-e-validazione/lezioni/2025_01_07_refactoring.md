# Refactoring

L'obiettivo è il **miglioramento** del design del codice esistente, con vari scopi:
- limitare il degrado del codice
- migliorare la leggibilità
- semplificare il codice e i test

Non vanno aggiunte funzionalità ma vanno semplicemente modificate le funzioni già presenti.

Il design cambia per diversi motivi:
- scelte tecnico-pratiche
- mode del momento
- necessità del cliente

Ovviamente il refactoring ha un costo:
- temporale
- economico

## Refactoring vs Re-engineering
Il Re-engineering consiste nel **modificare** pesantemente la struttura cambiandone addirittura **l'architettura di base**.

Il refactoring procede in parallelo durante tutto lo sviluppo del SW e non va ad intaccare l'archiettura.

## Debito tecnico
Il debito tecnico è l'accettazione di compromessi durante lo sviluppo del codice, a discapito della qualità.
Tale debito deve essere registrato perché è necessario sapere il rapporto tra qualità e funzionalità.

==Il debito tecnico è direttamente proporzionale al costo di di fare modifiche.==

Quindi diventa necessario mantenere, entro una soglia, il debito tecnico attraverso azioni di refactoring.

## Quando fare Refactoring?
Non c'è una specifica sulle tempistiche, tipicamente è utile farlo:
- prima dell'introduzione di nuove funzionalità
- dopo aver sistemato errori nel codice
- all'identificazione di un _code smell_
==La good practice dice di farlo appena è possibile.==

### Code smells
Problemi nel codice non facilmente identificabili che però restituiscono una sensazione di disagio nell'insieme. Non sono bug o errori ma semplicemente del codice cattivo.
- **Codice duplicato** - linee di codice duplicate inutilmente che possono essere raggruppate in una funzione; anche troppi commenti sono degli smell
- **Metodi lunghi** - i metodi dovrebbero essere contenuti e limitati, in caso è possibile dividere il metodo per aumentare la leggibilità
- **Switch-case** - spesso è possibile sostituire gli switch case, che introducono duplicazione, con la logica del polimorfismo
- **Data clumping** - ripetizione degli stessi campi o funzioni delle classi in più punti del codice, in questo caso si potrebbe introdurre una classe in più e sfruttare l'ereditarietà
- **Speculative generality** - eventuali specifiche o implementazioni con uso futuro possono essere semplicemente rimosse; oppure codice zombie; oppure clausole catch vuote

### Cloni
Con **clone** si intendono pezzi di codice duplicati all'interno dello stesso SW.

Possiamo dividere i cloni in diverse tipologie:
- Tipo 1 - copia incolla
- Tipo 2 - copia incolla con ridenominazioni delle variabili
- Tipo 3 - modifica della stessa funzione nei tipi delle variabili

## Procedura di refactoring
Si segue una propria routine per il refactoring che parte dal far girare i casi di test, segue l'identificazione e correzione dei code smell, fino a far girare di nuovo i test, ==ciclicamente==.

Inoltre la good practice dice di eseguire modifiche in piccole parti, senza mai esagerare.

Esistono liste già compilate contenenti diversi tipi di refactoring: refactoring.com.

---

Tipica domanda d'esame