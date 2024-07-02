# Wireless Security
Le connessioni wireless sono, dal punto di vista della sicurezza, molto critiche.
- **canale** -> il canale ad onde radio è pubblico e il traffico non è "rinchiuso" in un cavo
	- è difficile proteggere le comunicazioni in broadcast da ascoltatori malevoli
	- è più facile sfruttare vulnerabilità presenti in protocolli di rete wireless
- **mobility** -> la mobilità dei dispositivi può essere un fattore di rischio
- **risorse** -> le risorse nei dispositivi mobili sono limitate e quindi maggiormente suscettibili ad attacchi DoS
- **accessibility** -> spesso sensori, telecamere oppure dispositivi wireless sono lasciati non protetti sulla rete (guarda [shodan.io](shodan.io)), rischiano sia via Internet sia via fisica

## Wireless Network Threats
Le reti wireless possono essere soggetti ad una grande gamma di rischi:
- **Accidental association** -> accesso intenzionale ad una LAN diversa da quella voluta a causa di sovrapposizioni tra segnali
- **Malicious association** -> accesso ad un AP malevolo, apparentemente legittimo (e.g. reti pubbliche)
- **Ad-hoc networks** -> una rete *ad-hoc* è una rete privata wireless privata tra due peer, la mancanza di centralizzazione potrebbe comportare problemi di controllo
- **Non-traditional networks** -> reti wireless "personali", basate su protocolli differenti (e.g. Bluetooth, barcode readers), possono essere ascoltate o bucate
- **Identity theft** -> impersonificazione di un dispositivo attraverso il furto del suo indirizzo MAC (i.e. *MAC spoofing*)
- **MITM attacks** -> presenza di una terza entità all'interno di una comunicazione che si pensava privata, le reti wireless soffrono molto di questo rischio per loro natura
- **DoS** -> attacco che ha l'obiettivo di mettere fuori uso i dispositivi sulla rete, anche in questo caso le reti wireless sono vulnerabili
- **Network injection** -> attacchi che puntano a modificare le impostazioni di rete dei dispositivi in modo da ottenere dei vantaggi malevoli

## Wireless Security Measures
Ovviamente esistono delle contromisure per cercare di assottigliare (o addirittura eliminare) i rischi sopra-elencati.
Tali contromisure si possono applicare a diversi elementi della comunicazione wireless:
- contromisure sulla **trasmissione** -> costante rischio di ==ascoltatori o alterazione== 
	- *signal-hiding techniques* -> consiste nell'utilizzare tecniche che rendono più difficile l'identificazione degli accessi alla rete wireless; può essere sia fisica (e.g. nascondere gli AP) ma anche multimediale (e.g. non permettere il broadcasting SSID)
	- *encryption* -> la cifratura dei messaggi introduce un livello di sicurezza maggiore (sempre che le chiavi siano sicure, sempre lì si va a parare 😉)
- contromisure sui dispositivi fisici di accesso, i.e. **access points** -> il rischio maggiore è l'==accesso non autorizzato==
	- necessario introdurre degli standard di sicurezza, nello specifico *IEEE 802.1X* che introduce un protocollo di autenticazione solido
- contromisure sulle **reti**, quindi sull'insieme di routers ed endpoints -> comprende una serie di tecniche standard di sicurezza, come:
	- usare protocolli di cifratura, antivirus
	- installazioni di firewall per il controllo del traffico
	- cambio delle impostazioni di fabbrica dei dispositivi

---

# Mobile Device Security
La crescita esponenziale dei dispositivi mobile ha creato la necessità di metterli in sicurezza da eventuali rischi:
- *mancanza di controlli di sicurezza fisici* -> la possibilità di movimento del dispositivo lo espone a diversi rischi come il furto o l'accesso non autorizzato
- *uso di dispositivi non fidati* -> i dispositivi mobile vanno assunti come non sicuri, potrebbero essere modificati in modo malevoli da entità esterne
- *uso di reti non fidate* -> il collegamento a reti non fidate per accedere a risorse aziendali potrebbe essere pericoloso
- *uso di app non fidate* -> per natura è facile installare applicazioni non fidate che potrebbero causare danni
- *interazione con sistemi cloud non fidati* -> la sincronizzazione cloud (sempre più popolare) se effettuata con sistemi non fidati porta a problemi di sicurezza
- *uso di contenuto non fidato* -> uso di materiale non fidato potrebbe essere vettore di attacchi (e.g. QR code che puntano a siti malevoli)
- *uso di servizi di localizzazione* -> un utente malevolo potrebbe essere in grado i mantenere traccia della posizione di diversi dispositivi

Per cercare di limitare tutti i rischi sopra-elencati si possono applicare una serie di tecniche:
- **device security** -> uso di dispositivi pre-configurati secondo gli standard di sicurezza aziendali (e.g. antivirus, lock, PIN, password manager, etc.)
- **traffic security** -> uso di tecnologie di cifratura ed autenticazione; quindi implementazione di canali VPN, protocolli di sicurezza ed autenticazioni multifattore
- **barrier security** -> uso di dispositivi in grado di proteggere i confini della rete, come un firewall ed intrusion detection systems

---

# IEEE 802.11 Standard

> [!info] IEEE 802.X
> Lo standard IEEE 802.X introduce una serie di terminologie e regole con il tentativo di amministrare in modo sicuro le LAN

Nello specifico lo standard **IEEE 802.11** regola ed amministra le WLAN.

Alcune definizioni utili, definite da IEEE 802.11:
- ***Stazione*** -> Ogni dispositivo amministrato da IEEE 802.11 e identificato da un MAC
- ***Funzione di coordinamento*** -> Funzione che regola il traffico delle stazioni all'interno dei BSS associati
- ***Basic Service Set (BSS)*** -> Insieme di stazioni controllate da una singola funzione di coordinamento
- ***Distribution System (DS)*** -> Sistema che permette di interconnettere un insieme di BSSs e LANs tra di loro
- ***Access Point (AP)*** -> Ogni entità che provvede l'accesso al DS attraverso una connessione wireless
- ***MAC Protocol Data Unit (MPDU)*** -> L'unità di dati inviati tra due MAC peer attraverso il livello fisico
- ***Extended Service Set*** -> Insieme di BSSs che appaiono come singolo BSS rispetto al livello logico dell'architettura

![[ess.png]]


Lo standard 802.11b specifica il protocollo **Wi-Fi** (poi esteso in IEEE 802.11g), includendo anche i protocolli WPA e WPA2 utili alle procedure di autenticazioni.

## Architettura di IEEE 802.11
L'architettura di IEEE 802 è descritta da tre livelli.
![[stack-ieee802.png]]

### 1. Layer Fisico
Il livello fisico è il livello più basso dello standard e gestisce il dispositivo fisico che trasmette le informazioni tramite onde radio (e.g. l'antenna).

### 2. Layer Medium Access Control
Il secondo layer è incaricato di convertire i dati di alto livello ottenuti dal layer superiore e metterli a disposizione per l'invio fisico sulla rete.
- *in trasmissione (in uscita)* -> incapsula i dati ricevuti dal layer logico (sottoforma di MSDU) all'interno della MPDU, aggiungendo gli indirizzi fisici ed il controllo degli errori
- *in ricezione (in entrata)* -> disassembla il frame fisico ricevuto ed applica le procedure di controllo degli errori

Struttura MPDU:
![[mpdu.png]]
- *MAC Control* -> informazioni di controllo necessarie al funzionamento
- *MSDU* -> dati dal livello logico
- *CRC* -> utile al controllo degli errori avvenuti durante la trasmissione

### 3. Layer Logico
Livello responsabile del controllo degli errori attraverso sia attraverso il CRC sia del recupero di informazioni perse.
Inoltre è incaricato di incapsulare i dati nel MSDU.

## Scambio di messaggi in un DS
I due servizi coinvolti nel traffico all'interno di un DS sono:
- **Distribuzione** -> permette lo scambio di MPDUs tra BSS connesse dal DS
- **Integrazione** -> permette lo scambio di dati tra BSS e LAN cablate
	- deve integrare tutte le tecniche per eseguire le conversioni dei dati

I dispositivi mobili all'interno di un DS possono slittare da una BSS (cella) all'altra e tale spostamento deve essere gestito:
- *transizione tra BSS* (stesso ESS) -> è necessario riconoscere il cambio di posizione ma non dovrebbe causare problemi
- *transizione tra ESS* -> è probabile che i protocolli o le impostazioni cambino e quindi è possibile un momentaneo non funzionamento

Per inviare dei dati all'interno di un DS è necessario conoscere le informazioni della Stazione destinataria e quindi dell'AP associato.
- *Associazione* -> connessione preliminare tra Stazione ed AP, a questo punto l'AP può informare anche gli altri BSS
- *Re-associazione* -> 