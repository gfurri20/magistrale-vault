Le **infrastrutture critiche** sono tutte quelle aziende/strutture che permettono ad uno stato o nazione di mantenere attive le funzioni vitali del paese (e.g. centrali elettriche, servizi militari e pubblici, aziende di cibo, eccetera).

Tutte queste infrastrutture, ormai, dipendono dalla connessione in rete.
Con la sempre maggiore popolarità delle tecnologie IoT all'interno delle catene di produzione delle aziende e dei sistemi di controllo aziendali in generale, i target degli attacchi informatici stanno sempre di più virando nei confronti degli ICS collegati alla rete.

Un ICS (Industrial Control System) è un sistema elettronico di controllo utilizzato per gestire i processi industriali (e.g. fabbrica di cibo ma anche peggio come centrali elettriche o centrali nucleari).

Giusto per la cronaca un attacco molto noto, chiamato Stuxnet, ha targettato una centrale di arricchimento dell'uranio in Iran.
Ora, Stuxnet è un virus che sarà costato un sacco di soldi, ha sfruttato **4** zerodays, probabilmente è stato finanziato da un governo (hanno molti soldi); però questo tipo di attacco è la nuova frontiera della cybersecurity.

Gli ICS sono sistemi **non** nativamente creati per essere gettati sulla rete, per questo motivo sono facili prede.

## ICS Cyber Kill Chain
Gli ICS controllano 3 tipi di dispositivi collegati alla rete:
- IoT, general purpose devices
- OT (Operational Technology), tutti quei dispositivi aziendali che controllano i dati prelevati dai sensori e dalle macchina nella catena di produzione
- IOMT (Internet Of Medical Things), tutti quei dispositivi medicali collegati alla rete (e.g. elettrocardiogramma)

La cyber kill chain che descrive un attacco ad ICS non si differenzia troppo dalla [[2023_10_04_cyber_kill_chain_MITRE]] generale.

Essa si divide in due "stage":
1. Preparazione ed esecuzione dell'**intrusione**
2. Sviluppo ed esecuzione dell'**attacco**

La prima fase è suddivisa in sotto-fasi:
- Planning and preparation, quindi fase di raccolta informazioni e sviluppo degli strumenti malevoli
- Intrusion, quindi fase di initial access, delivery, exploit ed esecuzione
- Installazione di persistenza con server C2

Quando i sistemi sono stati infettati inizia lo stage dell'attacco, questo è caratterizzato da una fase di analisi e test che permette all'attaccante di capire come compiere effettivamente l'attacco.


