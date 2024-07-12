# Wireless Security
Le connessioni wireless sono, dal punto di vista della sicurezza, molto critiche. Alcune definizioni:
- **canale** -> il canale ad onde radio è pubblico e il traffico non è "rinchiuso" in un cavo
	- è difficile proteggere le comunicazioni in broadcast da ascoltatori malevoli
	- è più facile sfruttare vulnerabilità presenti in protocolli di rete wireless
- **mobility** -> la mobilità dei dispositivi può essere un fattore di rischio
- **risorse** -> le risorse nei dispositivi mobili sono limitate e quindi maggiormente suscettibili ad attacchi DoS
- **accessibility** -> spesso sensori, telecamere oppure dispositivi wireless sono lasciati non protetti sulla rete (guarda [shodan.io](shodan.io)), rischiano sia via Internet sia fisicamente

## Wireless Network Threats
Le reti wireless possono essere soggette ad una grande gamma di rischi:
- **Accidental association** -> accesso non intenzionale ad una LAN diversa da quella voluta a causa di sovrapposizioni tra segnali
- **Malicious association** -> accesso ad un AP malevolo, apparentemente legittimo (e.g. reti pubbliche)
- **Ad-hoc networks** -> una rete *ad-hoc* è una rete wireless privata tra due peer, la mancanza di centralizzazione potrebbe comportare problemi di controllo
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
- contromisure sui dispositivi fisici di accesso, i.e. **access points AP** -> il rischio maggiore è l'==accesso non autorizzato==
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
- **traffic security** -> uso di tecnologie di cifratura ed autenticazione; quindi implementazione di canali VPN, protocolli di sicurezza ed autenticazioni multi-fattore
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
- *in trasmissione (in uscita)* -> incapsula i dati ricevuti dal layer logico (sotto forma di MSDU) all'interno della MPDU, aggiungendo gli indirizzi fisici ed il controllo degli errori
- *in ricezione (in entrata)* -> dis-assembla il frame fisico ricevuto ed applica le procedure di controllo degli errori

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
- *Re-associazione* -> permette la transizione tra un BSS all'altro aventi AP differenti
- *De-associazione* -> notifica di disconnessione (anche quando si lascia l'ESS o si spegne il dispositivo)

--- 

# IEEE 802.11i WLAN Security
Ogni Stazione all'interno del raggio di un BSS può, potenzialmente, inviare pacchetti sulla rete.
Diventa quindi ==necessario introdurre standard di sicurezza robusti==.
- **Wired Equivalent Privacy (WEP)** nel 1999 -> standard che introduce la privacy ma pieno di debolezze (e.g. usava RC4 per la confidenzialità e CRC per l'integrità)
- **Wi-Fi Protected Access (WPA)** nel 2003 -> aumenta la sicurezza introducendo anche l'autenticazione per le reti Wi-Fi
- **Robust Security Network (RSN)** anche chiamato ***WPA2/3*** -> standard complesso che estende la sicurezza nelle reti wireless

## Standard RSN
Lo standard RSN definisce i seguenti servizi, ad ogni servizio è associato un set di protocolli che ne permettono l'implementazione:
- **Authentication** and **Key Generation** -> *Extensible Authentication Protocol (EAP)*
	- mutua autenticazione
	- scambio delle chiavi di sessione
- **Access Control** -> *IEEE 802.1 Port-based AC*
- **Confidenzialità, Origin Auth, Integrità e Replay Protection** -> prima *TKIP* e poi *CCMP*
	- dati del livello MAC (secondo livello di IEEE 802.11) crittografati e controllata l'integrità

Ognuno di questi protocolli sfrutta diversi algoritmi di cifratura per raggiungere i propri scopi.

==RSN ha il compito di mettere in sicurezza solamente la comunicazione tra Stazione e il suo AP di riferimento.==

Le operazioni amministrate da RSN possono scomposte in cinque gruppi:
1. **Discovery**
2. **Authentication**
3. **Key Management**
4. **Protected Data Transfer**
5. **Connection Terminated**

![[rsn.png]]

### 1. Discovery
Lo scopo di questa fase è fare in modo che ==AP e Stazione si riconoscano e si accordino sulle policies di sicurezza sulla base delle quali creare una prima associazione==.

Nello specifico tali policies di sicurezza indicano:
- quale algoritmo di autenticazione utilizzare
- quale algoritmo di scambio delle chiavi sfruttare
- quale protocollo utilizzare per garantire confidenzialità ed integrità durante lo scambio dei messaggi veri e propri
Quindi, *la fase di discovery influenza tutte le fasi successive*.

La fase di **Discovery** si divide in tre micro-fasi:
1. **Network and security capability discovery** -> la Stazione scopre l'esistenza della rete e capisce le necessità di sicurezza implementate dall'AP, questo può farlo in due modi
	- attraverso un specifica richiesta all'AP, detta `probe request` 
	- attraverso il `beacon` inviato in broadcast periodicamente dall'AP
2. **Open system auth** -> scambio degli identificatori da parte della Stazione e dell'AP
3. **Association** -> la Stazione, scelte le specifiche di sicurezza, invia le proprie scelte all'AP attraverso una `Association Request` a cui seguirà una `Association Response` da parte dell'AP

### 2. Authentication
Durante questa fase la Stazione e l'AP eseguono la ==mutua autenticazione==. In questo modo si tenta di far comunicare sulla rete solo coloro che si sono identificati legittimamente.

Il protocollo che gestisce questa fase è *Extensible Authentication Protocol (EAP)*.
Esso si divide in due micro-fasi:
1. **EAP exchange** -> scambio di informazioni preliminare che ==permette l'autenticazione==, viene utilizzato il protocollo scelto durante la fase di Discovery. L'autenticazione coinvolge un AS centralizzato.
2. **Secure key delivery** -> infine l'==AS genera una MSK== (Master Session Key), che verrà spedita in modo sicuro alla Stazione

La **MSK** è una chiave segreta che l'AP condivide con ogni client, essa permette di generare tutte le altre chiavi utili.
La sua alternativa è la **Pre-Shared Key (PSK)**.

### 3. Key Management
Durante questa fase ==le chiavi utili alla comunicazione vengono generate== (a partire dalla MSK, quindi esiste una gerarchia delle chiavi) ==e distribuite alla Stazione== coinvolta.

Ci sono due tipi di chiavi:
- **Pairwise keys** -> utilizzate nelle comunicazione tra Stazione e AP
	- queste chiavi derivano dalla Pairwise Master Key che a sua volte deriva dalla MSK
	- sono tre chiavi, dette *Pairwise Transient Keys (PTK)*, che ==permettono la comunicazione sicura tra Stazione ed AP==, insieme queste chiavi garantiscono confidenzialità, autenticazione dell'origine ed integrità
- **Group keys** -> usate per le comunicazione in multicast (più utenti ma selezionati)
	- la gerarchia è più snella perché la Group Master Key (GMK) è generata direttamente dall'AP
	- dalla GMK deriva una singola chiave detta *Group Temporal Key (GTK)* che permette la comunicazione multicast sicura
	- la GTK sfrutta le chiavi pairwise per essere condivisa
	- ==la GTK è cambiata ogni volta che il dispositivo lascia la rete==


### 4. Protected Data Transfer
Per proteggere i dati da trasmette RSN sfrutta uno tra due protocolli:
- **Temporal Key Integrity Protocol (TKIP)** -> creato per sostituire WEP su dispositivi vecchi, garantisce
	- *integrità* -> attraverso un message integrity code (MIC)
	- *confidenzialità* -> attraverso RC4, cifrando MPDU e MIC
- **Counter Mode-CBC Mac Protocol (CCMP)** -> creato per dispositivi moderni, garantisce
	- *integrità* -> attraverso CBC-MAC (quindi Message Auth Code in modalità CBC di concatenazione)
	- *confidenzialità* -> attraverso AES in modalità CTR