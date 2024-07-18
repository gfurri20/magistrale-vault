# Cyber-Physical Systems

>[!info] CPS
>Un sistema si dice cyber-fisico se un sistema fisico ed ingegneristico è monitorato, controllato ed integrato attraverso processi informatici.

Un CPS si compone di tre componenti:
- **Sensor Network** -> monitorano i fenomeni fisici derivanti dai processi fisici
- **Communication Network** -> utilizza i dati ricavati dai Sensor Network per prendere decisioni attraverso il sistema informatico
- **Actuator Network** -> implementa le decisioni prese dal sistema informatico sui processi fisici

![[cps.png]]

Un CPS deve possedere determinati standard:
- **Interoperabilità** -> abilità di un sistema di scambiare informazioni tra diversi componenti
- **Prevedibilità** -> garantisce un determinato grado di qualità
- **Affidabilità** -> garantisce un certo grado di correttezza
- **Sostenibilità** -> durabilità nel tempo
- **Dipendenza** -> grado di fiducia relativo a tutto il sistema
- ***Sicurezza*** -> integrità e confidenzialità

Possibili attaccanti di un CPS, ognuno con intenzioni diverse:
- cyber criminali
- dipendenti incazzati
- attivisti e terroristi
- governi (e.g. stuxnet)

---
# Industrial Control Systems (ICS)
Un ICS è un sistema di automazione che provvede al controllo e al monitoraggio delle funzioni all'interno di un'azienda. Una rete di ICS compone un CPS.

Un ICS si compone di diversi elementi:
- **HMI** -> interfaccia utente di visualizzazione e controllo
- **Stazioni dei dipendenti** -> supervisione e controllo dei processi
- **ICS servers** -> per diverse utilità
- **Controller** -> interfaccia tra il sistema informatico e i sensori che raccolgono i dati (e.g. PLC)

Gli ICS sono contenuti nella *rete industriale*, quest'ultima comunica quotidianamente con la *business network*, formando così una rete unica.

Questa rete può essere divisa in porzioni, ognuna delle quali possiede determinati standard di sicurezza.
==Diventa necessario segregare la rete attraverso dispositivi di sicurezza, come firewall e IDS.==
La porzione di rete che contiene i vari ICS è detta **Control Zone** ed è la rete che deve essere maggiormente protetta.

![[cps-zones.png]]

## Protocolli Industriali
I protocolli di comunicazione utilizzati a livello industriale sono stati creati senza introdurre nessun tipo di sicurezza. Al giorno d'oggi è fondamentale e quindi è stato necessario intervenire su tali protocolli per garantirla.

Esistono due tipi di reti:
- **routable** -> utilizzano i protocolli di rete definiti da TCP/IP o ISO/OSI
	- includono anche protocolli non routable trasformati (e.g. DNP3 over TCP)
- **non routable** -> si basano su comunicazioni seriali, su bus o point-to-point e sono tipiche dei sistemi industriali

Una PLC potrebbe essere collegata simultaneamente ai sensori attraverso una rete non routable e ad uno switch attraverso una rete routable.

Possiamo dividere i protocolli industriali in due categorie:
- **Fieldbus protocols** -> amministrano la comunicazione tra sensori, dispositivi di controllo ed HMI
	- Modbus
	- DNP3
- **Backend protocols** -> permettono system-to-system comunication
	- OPC
	- ICCP

### Modbus
Creato nel 1979 e permette la comunicazione tra dispositivi industriali e PLCs. 
Modbus è un protocollo di livello applicazione basato su architettura request/response. Il protocollo distingue tre PDU:
- `request` -> per l'invio di richieste
- `response` -> per l'invio di risposte
- `exception response` -> per l'invio di notifiche d'errore

Modbus include delle varianti:
- *Modbus RTU* -> utilizza una rappresentazione binaria per la comunicazione con gli RTU
- *Modbus ASCII* -> utilizza una rappresentazione ASCII

Modbus manca di sicurezza:
- non c'è autenticazione (niente integrità o non-ripudiabilità)
- non c'è cifratura (niente confidenzialità)
- non c'è un sistema di checksum
Diventa necessario introdurre dei principi di sicurezza:
- introduzione di IDS e firewalls
- implementazione di liste di whitelisting

## Componenti di un ICS
Un ICS si compone di diversi elementi:
- **Indicatori fisici** -> componenti che misurano o modellano il fenomeno fisico
	- sensori
	- attuatori
	- valvole
- **Sistemi di controllo**
	- *PLC* (Programmable Logic Controller) -> dispositivo informatico specializzato nell'automazione di funzioni industriali
	- *RTU* (Remote Terminal Unit) -> mette in comunicazione un dispositivo fisico remoto ed il server ICS che raccoglie i dati
	- *IED* (Intelligent Electronic Device) -> si interpone tra RTU e dispositivo fisico con il compito di tradurre i dati dal dominio analogico a quello digitale
	- *HMI* (Human Machine Interface) -> fornisce un'interfaccia grafica all'utente umano per monitorare e controllare real-time il sistema industriale fisico attraverso i dati forniti dai dispositivi ed elaborati dal Controller (e.g. PLC)

### PLC
Tipicamente una PLC controlla uno specifico processo industriale real-time ed è composta da:
- power supply
- input module
- control processor
- communication module
Le PLC sono caratterizzata da S.O. embedded specifici per la loro funzione indutriale.

Una PLC lavora seguendo una *serie di operazioni*:
1. controlla lo stato dell'input fornito dai sensori connessi
2. esegue il programma in base ai dati ricevuti
3. aggiorna lo stato dell'output in base ai risultati del programma
4. ritorna al punto (1)

## Sicurezza degli ICS
Possibili attacchi ad un ICS:
- MITM
- DDoS
- Replay Attacks
L'obiettivo dipende dall'autore dell'attacco, ogni gruppo ha intenzioni diverse.

L'obiettivo degli attaccanti è quello di penetrare i dispositivi di controllo, che per natura sono i punti più critici di un ICS.

Per proteggere un CPS è necessario introdurre diverse strategie:
- segregazione della rete in modo da ottenere un controllo più granulare
- introduzione di firewall e IDS
- utilizzo di protocolli sicuri di comunicazione
- introduzione di controlli degli accessi, sia informatici che fisici
