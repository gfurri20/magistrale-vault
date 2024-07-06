Esistono diverse tecniche per aggiungere sicurezza direttamente sugli end-host.
# Firewalls
**Un firewall permette di proteggere i flussi di traffico in entrata e in uscita** rispetto ad una rete, attraverso delle regole dette policies:
- definisce un collo di bottiglia che filtra il traffico con l'obiettivo di proteggere la rete da ogni possibile minaccia
- permette di monitorare eventi di sicurezza
- aggiunge sicurezza a quei servizi che non la implementano per natura (e.g. NAT)

Limiti di un firewall:
- inutile in caso di attacchi che lo bypassano
- inutile in caso di attacchi originati all'interno della rete

Esistono diverse tecniche attraverso le quali un firewall controlla il traffico:
- **Service Control** -> controllo sul tipo di servizio interrogato
- **Direction Control** -> controllo sulla direzione del flusso rispetto al servizio richiesto
- **User Control** -> controllo sul flusso generato da un determinato utente
- **Behavior Control** -> controllo su determinati comportamenti dei flussi (e.g. spam control)

Esistono quattro principali tipologie di firewall:
1. **Packet Filtering**
2. **Stateful Inspection**
3. **Application Proxy**
4. **Circuit-level Proxy**

![[fw-sceheme.png]]

## 1. Packet Filtering Firewall
Un firewall di tipo Packet Filtering applica un insieme di regole ad ogni pacchetto IP in entrata e in uscita, in base al risultato della regola decide se inoltrare il pacchetto oppure se scartarlo.
Le regole controllano determinati parametri degli header IP o TCP, come l'indirizzo IP, il protocollo di livello trasporto, il numero della porta, eccetera.

Ogni insieme di regole è caratterizzato da una **regola di default**:
- `Discard` -> whitelist (ciò che non è espresso è scartato)
- `Forward` -> blacklist (ciò che è espresso è scartato)

| Action    | in-host | in-port | out-host | out-port | comment                        |
| --------- | ------- | ------- | -------- | -------- | ------------------------------ |
| `allow`   | `*`     | `*`     | `*`      | `25`     | Permette ogni connessione SMTP |
| `discard` | `*`     | `*`     | `*`      | `*`      | Default `discard`              |
e.g. questa policy permette solo connessioni (in/out) SMTP, tutto il resto è scartato.

Vantaggi:
- è una tecnica molto *semplice da implementare*
- rimane trasparente all'utente
- *molto efficiente*

Svantaggi:
- **non protegge da attacchi a livello applicazione**
- i log sono limitati
- **non supporta tecniche di autenticazione avanzate**
- sensibili a **configurazioni sbagliate**
- necessità di **mantenere aperte tutte le porte alte** per connessioni in entrata (se viene esposto un determinato servizio)

Alcuni attacchi e contromisure:
- **IP address spoofing** -> sostituzione dell'IP esterno con un IP interno nel tentativo di ingannare i filtri
	- scartare i pacchetti con IP interno derivanti da un'interfaccia esterna
- **Source routing attacks** -> viene specificato il percorso che il pacchetto deve seguire nel tentativo di eludere la sicurezza
	- scartare tutti i pacchetti aventi tale opzione
- **Tiny fragment attacks** -> separazione dell'header TCP in diversi pacchetti IP nel tentativo di eludere la sicurezza
	- impostare un limite alla grandezza dei frammenti

## 2. Stateful Inspection Firewall
Estende il FW packet filtering restringendo le regole per il traffico TCP, difatti ==viene creata una directory che mantiene i riferimenti alle connessioni TCP aperte==.

Per ogni connessione TCP viene creata una entry che mantiene le informazioni relative.
In questo modo vengono permesse le porte alte solamente per le connessioni attive.

Alcuni Stateful Inspection FW mantengono ulteriori informazioni TCP:
- sequence numbers -> prevenzioni di attacchi session hijacking
- alcune porzioni di dati -> per identificare e tracciare tali connessioni

## 3. Application-Level Gateway Firewall
Un FW Application-Level non permette connessioni TCP end-to-end perché il suo compito è quello di inoltrare internamente il traffico di livello applicazione esterno.
Se il FW non implementa un determinato servizio allora l'inoltro non avviene ed il traffico viene scartato.

==L'utente si autentica al FW, il quale si interpone tra servizio ed utente.==

Un Application-Level FW tende ad essere *più sicuro rispetto ad un FW packet filtering* perché non necessita di analizzare ogni possibile combinazione di parametri IP e TCP, basta *impostare il controllo sul servizio specifico*.

Lo svantaggio principale è che **aumenta l'overhead** e le prestazioni ne risentono.

## 4. Circuit-Level Gateway
Un Circuit-Level FW non permette connessioni TCP end-to-end perché instaura due connessioni TCP: un tra utente e FW ed un altra tra FW e servizio.

==E' un Application-Level FW, però a livello TCP==.

Il FW a questo punto avrà il compito di inoltrare i pacchetti tra una connessione e l'altra, **senza controllare il contenuto**.
Il livello di sicurezza dipende dal numero e dal tipo di connessioni che vengono autorizzate.

In questo caso l'overhead è presente sulle connessioni in entrata che devono essere esaminate, perché l'amministratore di rete assume che gli utenti interni siano fidati.

## DMZ
All'interno di una rete possono essere configurati più firewall, ognuno di tipologia diversa e con scopi differenti.

Spesso all'interno di una rete aziendale si individua una porzione che contiene i servizi che devono essere esposti sulla rete.
Tale porzione di rete è detta Demilitarized Zone (DMZ), essa viene separata dalla rete interna in modo da creare aree che necessitano di sicurezza differente.

Di solito si individua un **FW esterno**, che garantisce una protezione iniziale ma che permette il traffico verso la DMZ, ed un **FW interno**, che aumenta il grado di protezione nei confronti della rete interna.


---

# Intrusion Detection Systems (IDS)

>[!info] Intrusion
>Violazione della policy di sicurezza, con l'obiettivo di violare la confidenzialità, integrità o disponibilità di un determinato servizio, sistema o infrastruttura.
>Può essere causa di un attaccante esterno/interno oppure di un dipendente che sfrutta le proprie autorizzazioni.

>[!info] Intrusion detection
>Il processo che raccoglie ed analizza le informazioni relative agli eventi del sistema e che permette di individuare segni di intrusione.

>[!important] Intrusion Detection System
>Un insieme di processi SW e componenti HW che implementano il processo di intrusion detection e rendicontazione dei vari tentativi di intrusione non autorizzati.

Gli IDS possono essere *classificati come segue*:
- **Host-Based** IDS -> vengono associati ad un ==singolo host==, aggiungono un layer di sicurezza specializzato a dispositivi a rischio
	- analisi più tempestiva, precisa e completa attuata in diverse modalità
	- in alcuni casi può anche fermare un attacco in corso
	- permette di identificare *sia minacce esterne che interne*
	- sfrutta una *combinazione tra anomaly detection e misuse detection*
	- introducono un certo grado di overhead
- **Network-Based** IDS -> ==monitorano il traffico della rete== a cui sono associati e dei dispositivi facentene parte
	- ascolta il traffico in modalità promiscua in punti strategici
	- si concentrano sul traffico livello rete, trasporto ed applicazione
	- i pacchetti sono considerati *interessanti se matchano una firma*
		- cerca in base al testo
		- cerca in base a porte conosciute
		- cerca in base a combinazioni sospette di header

Un IDS si compone di *tre parti logiche*:
- **Sensori** -> responsabili della ==raccolta dei dati==
	- raccolgono informazioni di natura diversa (e.g. pacchetti di rete, file di log, ...)
	- inviano le informazioni agli analizzatori
- **Analizzatori** -> responsabili di ==identificare se un'intrusione è avvenuta== o meno attraverso l'analisi dei dati
	- ricevono dati dai sensori oppure da altri analizzatori
	- possono essere in grado anche di elencare eventuali contromisure
- **Interfacce utente** -> fornisce l'==interazione con l'utente==
	- visualizzazione dei risultati
	- impostazioni relative al sistema

## Obiettivi
Gli obiettivi principiali di un IDS sono:
- **prevenzione efficace** di intrusioni evitando falsi negativi o positivi
- **identificare velocemente** eventuali intrusioni in modo da prendere provvedimenti utili nell'immediato
- rilevazioni di informazioni utili per lo **studio delle tecniche di intrusione**

## Approcci alla Intrusion detection
Alla base dell'intrusion detection c'è la possibilità di ==registrare il comportamento degli utenti per individuare in modo efficace ed efficiente eventuali comportamenti anomali==. Distinguiamo due approcci complementari:
- **Misuse detection** -> definisce regole in modo da *identificare incidenti di sicurezza o pattern ricorrenti di attacco*
	- sfrutta algoritmi di pattern-matching e database di tecniche già analizzate
	- *debole contro attacchi inediti*
	- possibili falsi positivi
- **Anomaly detection** -> *cerca comportamenti anomali* rispetto alla normalità
	- sfrutta file di audit e treshold oppure la *profilatura delle attività* degli utenti
	- potrebbe essere in grado di *scoprire nuovi attacchi*
	- trade-off tra falsi positivi e falsi negativi (i.e. certe volte le attività di un utente malevolo si possono sovrapporre a quelle di un utente legittimo)

## Network-Based IDS (NIDS)
Un NIDS può essere configurato in diverse posizioni della rete per garantire il controllo di traffichi differenti:
1. all'imbocco della rete esterna
2. nella DMZ per l'analisi del traffico relativo ai servizi
3. all'interno della rete interna dedicata ai servizi locali
4. all'interno della rete interna dedicata ai dipendenti

---

# Malware
