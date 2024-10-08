> [!info] Software process
>Sviluppo e validazione del software

Esistono svariate best practice per la gestione del software process, ognuna delle quali con le proprie caratteristiche.
Bisogna saper scegliere in base alle proprie necessità.

Lo sviluppo del software deve essere una disciplina **controllata**, **ordinabile** e **ripetibile**. L'attività di sviluppo deve essere sempre sotto controllo.

Obiettivo:
- migliorare la produttività degli sviluppatori
- controllare la qualità del software finale

$$\texttt{Process quality} = \texttt{Product quality}$$

>[!info] Processo
>Una serie di attività strutturate che permettono di sviluppare un sistema software

Tratti del processo di sviluppo:
1. **specifiche**, definite e comprese
2. **design ed implementazione**, scrittura vera e propria
3. **validazione**, verifica dell'implementazione nei confronti delle necessità utente
4. **evoluzione**, entità viva soggetta ad evoluzione (e.g. bug)

I processi si differenziano in due macro categorie:
- processi **plan-drive** -> attività di pianificazione *dettagliata*, l'obiettivo è quello di poter mappare in ogni momento lo sviluppo effettivo con il piano d'azione
- processi **agile** -> il piano cresce con lo sviluppo, a mano a mano 🎶. La pianificazione ==si adatta alle problematiche che si incontrano durante il percorso==.

Spesso si adotta un'approccio ibrido.

# Processi di sviluppo
Esistono diversi approcci pratici ai processi di sviluppo:
- **code and fix** -> implementa e correggi, il codice è sviluppato "per tentativi" e non c'è una grande parte di design e progettazione
	- vantaggioso per progetti di piccole dimensioni
	- in realtà in questo modo non si adotta un processo -> *fallimento*
- **waterfall** -> processo guidati da piani, prevede attività separate per le varie task
- **incrementale** -> prevede di consegnare molteplici versioni aventi funzionalità incrementali
- **integrazione e configurazione** -> cerca di scrivere meno codice possibile integrando blocchi già esistenti tra loro

Anche in questo caso l'azienda potrebbe mixare i processi.

## Waterfall model 🌧
Nasce con le prime, importanti e complesse commesse industriali (🪖). Deriva dal processo manifatturiero con il quale ha una mappatura 1:1.

==Ogni fase dello sviluppo ha come input l'output della fase precedente.==

Attività condotte:
1. *definizione dei requisiti* e delle funzionalità, con annesse problematiche, assieme agli stakeholders
2. *progettazione del software* e definizione ad alto livello del software; quindi comunicazione tra i vari componenti
3. *implementazione*, scrittura del codice e realizzazione assieme ad eventuali test
4. *integrazione delle componenti* e fase di test per verificare la connettività e la funzionalità lato utente finale
5. *produzione* e *manutenzione*, quindi pubblicazione del sistema e adattamento del sistema in base a problemi/cambiamenti

> possibile domanda d'esame

Ci sono contesti in cui è meno appropriato applicare waterfall perché *non si può tornare indietro*, si necessità, quindi, di una **completa** comprensione dei requisiti.

Sistemi appropriati ai quali applicare waterfall:
- sistema software/hardware
- sistema critico, ovvero un ==sistema vitale== per individui o gruppi 🏥
- sistemi di grandi dimensioni, in cui i componenti potrebbero non appartenere allo stesso dominio aziendale

I requisiti per questo tipo di sistemi devono essere validati per normativa legale, in quanto essi sono ritenuti critici e delicati.

Vantaggi:
- molto effort nella comprensione dei requisiti, lo sviluppo non parte senza completezza dei requisiti
- introduce una pianificazione dettagliata -> sviluppo ordinato e chiaro
- checkpoint intermedi molto chiari utili alla coordinazione

Svantaggi:
- le fasi devono essere complete per passare a quella successiva
- difficile far trovare spazio ai cambiamenti all'interno dello sviluppo -> *non si torna più indietro*

## Incrementale
Le varie fasi avanzano in parallelo e concorrono alla definizione delle versioni successive al processo.

Spesso si utilizza nel caso in cui i requisiti potrebbero cambiare in fase di sviluppo, perché la specifica degli stessi segue il ciclo di vita, intero, del processo.

Vantaggi:
- riduzione dei costi nel caso di cambiamenti
- meno documentazione
- più facile ottenere un feedback dall'utente finale e rifletterlo nel prodotto finale; questo grazie alla consegna di versioni preliminari

Svantaggi:
- l'adattamento di ulteriori funzionalità concorre a ridurre la qualità del SW stesso, a causa di aggiunta di pezzi ai quali non si aveva pensato inizialmente
- è difficile da capire se si sta accumulando ritardo
- sarà sempre più difficile aggiungere pezzi

## Integrazione e configurazione
Basato sul riuso del software per agire sul mercato in **maniera rapida**.

...

Di solito si cercano componenti da configurare tra di loro, non sempre danno il risultato che si cerca.
I ==requisiti devono piegarsi ai componenti che sono disponibili==, potrebbe innescarsi una fase di negoziazione.

I componenti possono essere open-source, commerciali o proprietari.

Vantaggi:
- consegna di un sistema anche a fronte di poco budget
- basso rischio grazie all'uso di componenti testate
- poco sviluppo da zero
- consegna rapida di un sistema valido -> aggressione rapida del mercato (spesso è un requisito fondamentale)

Svantaggi:
- bassa qualità -> uso componenti non pensati per quel contesto
- necessità di accettare un trade-off sulle funzionalità
- perdita del controllo sull'evoluzione del SW, sono pezzi sviluppati da altri e sui quali non si ha giurisdizione

