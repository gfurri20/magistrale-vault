Sicurezza a livello applicazione:
- HTTPS
- SSH
Sicurezza livello trasporto:
- TLS

Sicurezza livello rete: **IPsec**

# IPsec
Internet Protocol (IP) non è un protocollo sicuro:
- possibile source spoofing
- possibili replay attacks
- manca confidenzialità ed integrità

IPsec introduce diversi servizi:
- **Confidenzialità** -> cifrando i dati
- **Integrità** -> i router calcolano hash e checksum per il controllo dei dati
- **Autenticazione** -> introdotte firme digitali e certificati
- *Access Control*

==IPsec permette di instaurare un canale sicuro unidirezionale per le applicazioni comunicanti su qualsiasi tipo di rete (da LAN a Internet), aggiungendo filtri di pacchetti che operano attraverso delle policy.==

IPsec mette in sicurezza tutte quelle applicazioni che fanno uso del livello di rete:
- è alla base delle VPN
- accesso sicuro ad Internet

Va installato in tutti quei dispositivi che interagiscono con i pacchetti a livello rete, quindi end-point ma anche routers.

IPsec si compone di diversi sotto-protocolli che permettono il corretto funzionamento:
- Authentication Header (AH) -> deprecato in favore di ESP
	- garantiva l'autenticazione del messaggio
- **Encapsulating Security Payload (ESP)** -> permette l'incapsulamento dell'header e del trailer
	- garantisce confidenzialità e autenticazione
- **Internet Key Exchange (IKE)** -> protocollo di gestione e condivisione delle chiavi specifico di IPsec
- Algoritmi di cifratura generici
- Ulteriori protocolli di gestione
	- **gestione delle policy di sicurezza**
	- gestione delle informazioni

## Architettura di IPsec
I protocolli elencati in precedenza sono parte di IPsec e lavorano in sinergia. Possiamo descrivere l'architettura attraverso le macro-fasi del protocollo:
1. scambio delle chiavi attraverso **IKE**
2. estrazioni dei parametri di sicurezza dai database incaricati
3. instaurazione delle security association
4. comunicazione protetta attraverso **ESP**

![[ip-sec-arch.PNG]]

## IKE
Il protocollo IPsec inizia con lo scambio iniziale delle chiavi, atto ad instaurare un canale sicuro per la condivisione dei parametri di sicurezza.

IKE mette a disposizione due modalità di gestione:
- **manuale** -> l'amministratore imposta le chiavi fisicamente all'interno dei sistemi coinvolti
	- adatto ad ambienti locali
- **automatizzato** -> scambio delle chiavi attraverso la rete utilizzando protocolli adibiti
	- adatto a scambi su Internet

Nello specifico la modalità automatizzata fa uso di due protocolli:
- **Oakley key determination protocol** -> protocollo di scambio chiavi basato su Diffie-Hellman
- **ISAKMP** -> protocollo di gestione delle chiavi

IKE si divide in due fasi:
1. instaura il canale di comunicazione sicuro ISAKMP attraverso lo scambio delle chiavi, utilizzando Oakley
2. utilizza il canale di comunicazione ISAKMP, instaurato precedentemente, per negoziare le Security Associations [[netsec-ip-sec#Gestione delle policies]].

## Gestione delle Security Associations
La comunicazione IPsec fa affidamento alle **Security Associations (SA)**, ==ovvero delle connessioni logiche tra sorgente e destinatario, influenzate da determinati parametri di sicurezza.==

Ogni SA è univocamente identificata da:
- un *security parameters index* -> identificativo generico di una SA
- *IP dst address* -> IP dell'end-point con cui si stabilisce la SA
- *security protocol id* -> identifica l'uso di AH o ESP

Ogni SA è parametrizzata da delle policies, ovvero da un insieme di regole. La gestione delle policies è il risultato dell'interazione tra il **Security Association Database** e il **Security Policy Database**.

### Security Association Database
Definisce i parametri associati ad ogni SA, alcuni dei parametri sono:
- `security parameters index`
- `sequence number counters` -> genera il sequence number che caratterizza l'header ESP o AH
- `anti-replay window` -> per individuare un eventuale replay attack
- `IPsec mode` -> identifica la modalità d'uso di IPsec
- altre informazioni utili

### Security Policy Database
Contiene le policy che relazionano la gestione di un determinato traffico IP rispetto ad una specifica SA.

Ogni entry nel SPD è definita da un insieme di IP e da un insieme di protocolli di livelli superiori, detti *selettori*. Quest'ultimi vengono utilizzati per filtrare il traffico in uscita di una specifica SA.

| #   | Protocol | Local IP  | Port | Remote IP  | Port | Action        |
| --- | -------- | --------- | ---- | ---------- | ---- | ------------- |
| 1   | UDP      | 1.2.3.101 | 500  | *          | 500  | `BYPASS`      |
| 2   | TCP      | 1.2.3.101 | *    | 1.2.4.0/24 | *    | `PROTECT:ESP` |
| 3   | *        | *         | *    | *          | *    | `DISCARD`     |
In questo caso all'interno del SPD sono specificate 3 policies, il processo che si occupa di analizzare il pacchetto in uscita dovrà scorrere ogni regola sequenzialmente, se il pacchetto combacia allora verrà eseguita l'operazione specificataa in **Action**. Vediamo l'esempio:
1. la prima regola lascia passare tutti i pacchetti che usano il protocollo UDP, originari da `1.2.3.101:500` verso ogni IP esterno ma diretto alla porta `500`
2. la seconda regola protegge i pacchetti compatibili attraverso l'uso di ESP
3. la terza regola è la **regola di default** che scarta tutti quei pacchetti che non hanno trovato compatibilità nelle regole precedenti.

==Quando un pacchetto deve essere protetto allora si interroga il SAD per ottenere la procedura di crittografia attraverso ESP oppure per instaurare delle nuove SA attraverso IKE.==

Anche per i pacchetti in input è possibile definire dei filtri attraverso delle policies.

### SA bundles
Le SA possono essere raggruppate in bundles, ovvero una sequenza di SA che specificano le caratteristiche che un determinato tipo di traffico IP deve avere.

==Sostanzialmente è possibile incapsulare SA dentro altre SA creando questi SA bundles.== In questo modo le proprietà di ogni SA si sovrappongono.

Come detto ESP non integra immediatamente l'autenticazione, se lo fa autentica direttamente il cipher-text.

Ci sono altri modi, attraverso i bundle, per garantire autenticazione dopo la cifratura:
- **Transport Adjacency** -> permette un solo livello di combinazione
	- applica più protocolli di sicurezza allo stesso pacchetto IP
	- applica prima ESP senza autenticazione
	- successivamente AH
	- introduce overhead
- **Iterated Tunneling** -> permette molteplici livelli innestati di combinazioni
	- con questa modalità l'autenticazione viene eseguita sul plain-text quindi prima della cifratura
	- prima viene applicato AH in transport mode
	- e successivamente ESP in tunnel mode

## ESP
ESP (successore di AH) è il protocollo che **permette l'incapsulamento** vero e proprio dei dati. Esso cifra sempre i dati applicazione e l'header TCP, ma gestisce gli header IP in base alla modalità di utilizzo scelta.

Potrebbe essere aggiunto del *padding* ai dati, nel caso in cui l'algoritmo di cifratura necessitasse di lunghezze specifiche.

AH garantiva "out-of-the-box" l'autenticazione, mentre ESP no. Con ESP è il primo utente che allega il campo autenticazione, nel caso avesse necessità di farlo. ==La procedura di autenticazione in ESP viene eseguita sul cipher-text.==

### AH
AH è effettivamente il predecessore di ESP ma non introduceva cifratura, **garantiva solo integrità**.

Quindi permetteva solo di introdurre canali autenticati ma non confidenziali.

### Transport Mode
Nella modalità trasporto ==l'header IP originario non viene incluso nei dati cifrati==, quindi sostanzialmente non viene toccato.
![[ipsec-tranport.png]]
- `Orig IP hdr` -> l'header IP originale che non viene cifrato, resta in chiaro
- `ESP hdr` -> l'header ESP non viene cifrato ma solamente autenticato
- `TCP` -> l'header TCP
- `Data` -> i dati contenuti nel messaggio
- `ESP trlr` -> trailer ESP che contiene l'eventuale padding e le info sul prossimo pacchetto
- `ESP auth` -> il digest dei parametri hashati con HMAC

Con questa modalità non vengono creati nuovi pacchetti. La procedura di autenticazione in ESP viene eseguita sul cipher-text in reti in cui l'incremento della grandezza di un pacchetto potrebbe causare problemi.
Alle volte, questa modalità, ==potrebbe essere vittima di analisi del traffico==.

Spesso usato per le **remote-access VPNs**.

### Tunnel Mode
Nella modalità tunnel ==l'header IP originario viene anch'esso incapsulato==, producendone uno nuovo, quindi si viene a creare un nuovo pacchetto IP più grande.
![[ipsec-tunnel.png]]

In questa modalità l'intero pacchetto IP è protetto e quindi nessun router o dispositivo intermedio riesce ad accedere al pacchetto IP originario.
Dato che si aggiunge `New IP hdr` allora il pacchetto IP nuovo ==potrebbe possedere diverse sorgente e destinazione==.

Questa modalità viene implementata tra due *security gateways* e non direttamente tra gli host. In questo modo si semplifica la distribuzione delle chiavi.

Spesso usato per **site-to-site VPN**.

### Anti-replay Mechanism
Si può introdurre un controllo basato su una finestra a scorrimento per cercare di prevenire replay attacks.

Grazie ad un meccanismo basato sull'introduzione dei sequence numbers è possibile gestire i pacchetti in modo da evitare di prendere in considerazioni eventuali duplicati.

Solo i pacchetti il cui sequence number è all'interno di un intervallo sono considerati validi.