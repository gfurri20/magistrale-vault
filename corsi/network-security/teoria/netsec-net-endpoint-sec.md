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






---

# Malware