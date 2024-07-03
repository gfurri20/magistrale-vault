# Mail Architecture
Lo scambio di mail da `Alice` a `Bob` coinvolge molteplici attori e protocolli:
1. `Alice` si interfaccia con un client di posta elettronica detto, in gergo, **Message User Agent (MUA)**
2. Il MUA inoltra il messaggio ad un host incaricato di trasmetterlo sulla rete, il **Mail Submission Agent (MSA)** (potrebbe anche essere integrato nel MUA)
3. L'email per raggiungere `Bob` deve passare attraverso la rete, quindi il sistema lo inoltra attraverso una serie di **Message Transfer Agent (MTA)**
4. Prossima alla destinazione, la mail raggiunge un **Message Delivery Agent (MDA)** che funge da end-point per la mail
5. L'MDA trasferisce la mail ad un **Message Store (MS)** al quale `Bob` può accedere, per scaricare la mail, attraverso il proprio MUA
L'inseme di tutti i MSA, MTA e MDA formano il **Message Handling System (MHS)**, incaricato di trasferire la mail sulla rete.

## Protocolli Mail
Esistono due protocolli usati per il trasferimento delle mail:
- **SMTP** -> caricamento e trasferimento della mail su Internet
	- protocollo client/server text-based
	- incapsula la mail e la inoltra tra i diversi MTA
	- ESMTP è la versione estesa del 2008
- **POP3** e **IMAP** -> trasferimento dei messaggi tra mail server, di solito vengono usati per scaricare le mail da MS a MUA
	- POP3 permette di *scaricare* una mail da un MS (TCP:110)
	- IMAP permette di *accedere* alle mail su un MS (TCP:143)
		- aggiunge autenticazione ed ulteriori funzionalità rispetto a POP

## Struttura del messaggio
Un messaggio che trasporta una mail elettronica si compone di (ref. [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322)):
- *involucro* -> insieme di informazioni utili per la trasmissione della mail sulla rete
- *contenuto* -> contenuto della mail
	- all'interno del contenuto sono presenti degli header (e.g. mail destinazione) che permettono di costruire l'involucro

## MIME
**SMTP presenta diverse limitazioni** tra cui:
- non è possibile trasmettere file eseguibili
- limita i caratteri speciali
- limita la grandezza di una singola mail

Per sopperire a queste limitazioni si è creato un protocollo che estende le possibilità di trasmissione mail: **Multipurpose Internet Mail Extensions (MIME)**.

MIME implementa:
- **cinque nuovi header** per introdurre informazioni sul body della mail
	- `MIME-Version` -> versione del protocollo
	- `Content-Type` -> descrizione dei dati contenuti nel body
	- `Content-Transfer-Encoding` -> modalità di encoding utilizzata
	- `Content-ID` -> ID per identificare entità MIME
	- `Content-Desc` -> descrizione degli oggetti contenuti
- supporto per **svariati formati multimediali** (e.g. immagini, video, audio, binaries, etc.)
- supporto per diversi **sistemi di encoding** (e.g. ASCII, binary, base64, etc.)

---
# Email Security Threats
Anche le mail possono essere soggette a rischi di vario genere:
- *Authenticity-related* -> accesso non autorizzato a sistemi mail aziendali
- *Integrity-related* -> modifica non autorizzata del contenuto
- *Confidentiality-related* -> condivisione non autorizzata di mail private
- *Availability-related* -> malfunzionamento del sistema
- *Phishing-related* -> tentativo di scam tramite mail per diversi scopi

Per contrastare (o limitare) questi rischi è necessario introdurre una serie di protocolli atti alla sicurezza:
- ***STARTTLS*** -> estende SMTP attraverso TLS, garantendo confidenzialità, integrità, autenticazione e non-ripudiabilità sull'intero messaggio
- ***S/MIME*** -> garantisce confidenzialità, integrità, autenticazione e non-ripudiabilità all'intero body del messaggio
- ***DNSSEC*** -> garantisce autenticazione ed integrità sui messaggi DNS
- ***DANE*** -> introduce un nuovo metodo di scambio chiavi per DNSSEC, permette di certificare i domini associati ad uno specifico IP
- ***Sender Policy Framework (SPF)*** -> associa un dominio ad un insieme di indirizzi IP
- ***DKIM*** -> permette agli MTA di firmare digitalmente alcuni header del body del messaggio SMTP
- ***DMARC*** -> mette a conoscenza della sorgente delle policy applicate da SPF e DKIM

![[email-sec-protocols.png]]


## Secure/Multipurpose Internet Mail Extension (S/MIME)
Introduce un livello di sicurezza su MIME. Per fare ciò implementa diverse funzionalità, sfruttando svariati protocolli di cifratura:
- *Digital signature* (Autenticazione) -> usa RSA per creare un digest del contenuto della mail
- *Message Encryption* (Confidenzialità) -> usa AES per cifrare il messaggio attraverso una ==one-time session key== (trasferita con RSA)
- *Compression* -> compressione utile alla trasmissione

#### Autenticazione
L'autenticazione di una mail è implementata attraverso la firma digitale, sostanzialmente viene prodotto l'hash del messaggio che verrà cifrato con la chiave privata della sorgente.
Tale firma può essere allegata direttamente con il messaggio, oppure inviata separatamente.

Il destinatario userà la chiave pubblica della sorgente per validare l'integrità del messaggio.

#### Confidenzialità
Ogni chiave di cifratura del messaggio viene utilizzata una singola volta, ==per ogni messaggio viene generata una nuova chiave==.
La chiave viene protetta attraverso la chiave pubblica della sorgente.
![[smime-flow.png]]

