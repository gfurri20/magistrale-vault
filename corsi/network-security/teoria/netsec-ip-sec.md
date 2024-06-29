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
- Authentication Header -> deprecato in favore di ESP
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
2. estrazioni delle policies dai database incaricati
3. scambio dei vincoli imposti dalle policies per quella connessione
4. comunicazione protetta attraverso **ESP**

### IKE

### Gestione delle policies

### ESP


## IPsec Tunnel Mode



## IPsec Transport Mode


