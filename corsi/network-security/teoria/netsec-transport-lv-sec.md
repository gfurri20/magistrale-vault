Spesso i web server esposti sulla rete sono potenziali punti di accesso per un attaccante.

Si possono introdurre meccanismi di sicurezza a diversi livelli dello stack ISO/OSI:
- **IPSec** -> a livello IP (lv. 3)
- **SSL/TLS** -> a livello TCP (lv. 4)
- a livello applicazione esistono una grande varietà di protocolli (e.g. Kerberos o i protocolli di mailing sicuro)

# TLS (Transport Layer Security)
TLS è uno standard di Internet ed è l'evoluzione di **SSL**.
Si compone di una serie di protocolli che fanno affidamento a TCP.

## TLS Architecture
Individuiamo due entità principali:
- **TLS connection** -> relazione tra peer
	- ogni connessione è associata ad una sessione
- **TLS session** -> relazione tra client e server
	- necessità una *fase di handshake*
	- vengono stabilite dei parametri di crittografia comune a tutte  le comunicazioni facenti parti di una sessione
	- evitano la trasmissione continua di parametri di sicurezza

Lo **stato** di una TLS connection è rappresentato dai seguenti parametri:
- `session identifier` -> identifica una connessione
- `peer certificate` -> certificato X.509 del peer
- `cipher spec` -> specifiche del cifrario e del MAC utilizzato
- `master secret` -> segreto condiviso tra peer

Lo **stato** di una TLS session è rappresentato dai seguenti parametri:
- `server and client random`
- `server/client MAC secret` -> chiave MAC usata dal server/client
- `server/client write key` -> chiave simmetrica condivisa
- `IV` -> creato durante la fase di handshake
- `sequence numbers` -> sia il client che il server mantengono un sequence number per identificare l'ordine dei messaggi (resettato al comando di `change cipher`)

## TLS Protocols
TLS individua due protocolli uno per la creazione della sessione, **Handshake Protocol**, e uno per il trasferimento delle informazioni, **Record Protocol**.

### Handshake protocol
Utilizza la crittografia asimmetrica per trasferire informazioni tra client e server, tra cui la versione utilizzata, i cifrari utilizzati e le chiavi segrete.
Opzionalmente implementa la mutua autenticazione.

Fase (1) - scambio di informazioni preliminari:
1. $Client \rightarrow Server$ `client_hello`:  info condivise di sessione (e.g. versione, ID sessione, cipher suite)
2. $Server \rightarrow Client$ `server_hello`: info condivise
Fase (2) - il server invia il certificato ed inizia lo scambio di chiavi:
3. $Server \rightarrow Client$ `certificate`: catena X.509
4. $Server \rightarrow Client$ `server_key_exchange`: inizia lo scambio di chiavi
5. $Server \rightarrow Client$ `certificate_request`: richiede il certificato del client
6. $Server \rightarrow Client$ `server_hello_done`
Fase (3) - il client procede all'invio del certificato se richiesto e delle informazioni di scambio chiavi
7. $Client \rightarrow Server$ `certificate`: catena X.509 del client
8. $Client \rightarrow Server$ `client_key_exchange`: conclude lo scambio di chiavi di sessione
9. $Client \rightarrow Server$ `certificate_verify`: firma digitale del certificato client
Fase (4) - cambio del cifrario (opzionale) e terminazione dell'handshake
10. $Client \rightarrow Server$: `change_cipher_spec`
11. $Client \rightarrow Server$ `finished`
12. $Server \rightarrow Client$ `change_cipher_spec`
13. $Server \rightarrow Client$ `finished`

### Record Protocol
Usa le chiavi simmetriche condivise attraverso l'handshake per introdurre **confidenzialità** (cifrario simmetrico), **integrità** (attraverso i MAC) e **autenticità** (certificati X.509) durante lo scambio di messaggi.

I dati seguono un processo preciso prima di essere inviati:
1. *Frammentazione* dei dati in gruppi
2. Ogni gruppo viene *compresso* e gli viene *allegato il MAC* prodotto dal frammento compresso
3. Messaggio compresso e MAC vengono *crittografati* attraverso le chiavi simmetriche di sessione
4. Al payload crittografato viene *aggiunto un TLS record header* (i.e. metadati) e spedito sulla rete 

## TLS Attack
Anche TLS può essere bersaglio di attacchi:
- attacco all'handshake
- attacco al record e ai dati
- attacco alla PKI (Public Key Infrastructure)

## TLS v1.3