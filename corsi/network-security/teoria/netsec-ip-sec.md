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
- **Internet Key Exchange (IKE)** -> protocollo di gestione e condivisione delle chiaci specifico di IPsec
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
- la seconda utilizza il canale di comunicazione ISAKMP, instaurato precedentemente, per negoziare le Security Associations [[netsec-ip-sec#Gestione delle policies]].

## Gestione delle Security Associations
La comunicazione IPsec fa affidamento alle **Security Associations (SA)**, ovvero delle connessioni logiche tra sorgente e destinatario, influenzate da determinati parametri di sicurezza.

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


## ESP

### Tunnel Mode

### Transport Mode


