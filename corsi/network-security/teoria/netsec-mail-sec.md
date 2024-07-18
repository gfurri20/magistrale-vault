# Mail Architecture
Lo scambio di mail da `Alice` a `Bob` coinvolge molteplici attori e protocolli:
1. `Alice` si interfaccia con un client di posta elettronica detto, in gergo, **Message User Agent (MUA)**
2. Il MUA inoltra il messaggio ad un host incaricato di trasmetterlo sulla rete: il **Mail Submission Agent (MSA)** (potrebbe anche essere integrato nel MUA)
3. L'email per raggiungere `Bob` deve passare attraverso la rete, quindi il sistema lo inoltra attraverso una serie di **Message Transfer Agent (MTA)**
4. Prossima alla destinazione, la mail raggiunge un **Message Delivery Agent (MDA)** che funge da end-point per la mail
5. L'MDA trasferisce la mail ad un **Message Store (MS)** al quale `Bob` può accedere, per scaricare la mail, attraverso il proprio MUA
L'insieme di tutti i MSA, MTA e MDA formano il **Message Handling System (MHS)**, incaricato di trasferire la mail sulla rete.

![[mail-arch.PNG]]

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
	- permette di firmare le mail in modo da garantire **non-ripudiabilità** sulle mail inviate da uno specifico dominio
	- la mail di un utente è firmata attraverso la chiave privata del dominio mittente
	- l'MDA destinatario interroga il DNS per ottenere la chiave pubblica del dominio mittente
- ***DMARC*** -> mette a conoscenza della sorgente delle policy applicate da SPF e DKIM
	- specifica le policies attraverso le quali le mail di un determinato dominio devono essere gestite
	- standardizza il modo in cui i riceventi eseguono il controllo dell'autenticazione attraverso DKIM e SPF

![[email-sec-protocols.png]]


## Secure/Multipurpose Internet Mail Extension (S/MIME)
Introduce un livello di sicurezza su MIME. Per fare ciò implementa diverse funzionalità, sfruttando svariati protocolli di cifratura:
- *Digital signature* (Autenticazione) -> usa RSA per creare un digest del contenuto della mail
- *Message Encryption* (Confidenzialità) -> usa AES per cifrare il messaggio attraverso una ==one-time session key== (trasferita con RSA)
- *Compression* -> compressione utile alla trasmissione
	- permette di guadagnare spazio (funziona bene con base64)
- *Email Compatibility* ->utilizza base64 per rendere "universale" il contenuto
S/MIME utilizza certificati X.509 per la gestione delle chiavi pubbliche, segue l'architettura basata sull'interazione con le CA.

#### Autenticazione
L'autenticazione di una mail è implementata attraverso la firma digitale, sostanzialmente viene prodotto l'hash del messaggio che verrà cifrato con la chiave privata della sorgente.
Tale firma può essere allegata direttamente con il messaggio, oppure inviata separatamente.

Il destinatario userà la chiave pubblica della sorgente per validare l'integrità del messaggio.

#### Confidenzialità
Ogni chiave di cifratura del messaggio viene utilizzata una singola volta, ==per ogni messaggio viene generata una nuova chiave==.
La chiave viene incapsulata attraverso la chiave pubblica della destinazione.
![[smime-flow.png]]

#### Migliorie di sicurezza
S/MIME, introduce inoltre quattro funzionalità aggiuntive per aumentare il grado di sicurezza:
- *Signed receipts* -> prova dell'avvenuta consegna (una ricevuta firmata digitalmente)
- *Security labels* -> indica il grado di confidenzialità del messaggio
- *Secure mailing lists* -> applica confidenzialità al messaggio da inviare per ogni destinatario presente
- *Signing certificates* -> associa in modo sicuro il certificato della sorgente con la propria firma, attraverso uno specifico attributo

---

# Domain Name System (DNS)
DNS è un servizio che permette di individuare l'associazione tra un hostname ed un indirizzo IP, e.g. `acdraldon.it` -> `77.39.210.53`.

Ne fanno ampio uso sia i MUA che gli MTA per individuare il loro prossimo hop sulla rete.

Un sistema DNS si compone di quattro elementi principali:
- *domain name space* -> una struttura ad albero che mantiene i riferimenti agli hostname registrati
- *DNS database* -> contiene le associazioni tra IP e nomi
	- contengono i **resource records** (i.e. nome, IP, info aggiuntive sugli host)
	- strutturati in modo gerarchico, specificando i nomi tra il punto `.` si livellano gli host (e.g. `tickets.acdraldon.it` è un sotto-dominio di `acdraldon.it`)
	- sono database distribuiti per garantire ridondanza
- *Name servers* -> gestiscono e distribuiscono le informazioni possedute da un determinato name space
	- ogni server può mantenere una cache degli RR per agevolare determinate interrogazioni
- *Resolvers* -> permettono la comunicazione tra name servers e client
![[dns-scheme.png]]
Esistono diversi tipi di Resource Record, ognuno con una funzionalità diversa:
- `A` -> associa hostname con IPv4
- `AAAA` -> associa hostname con IPv6
- `CNAME` -> specifica degli eventuali alias per un host
- etc.

## DNSSEC
Una richiesta DNS vanilla potrebbe essere intercettata, un attaccante potrebbe restituire un IP di un server malevolo a client ignari, quindi è necessario introdurre un grado di sicurezza.
Garantisce protezione end-to-end attraverso l'uso di firme digitali, introducendo **integrità** ed **autenticazione**.

L'**amministratore DNS** della zona firmerà digitalmente ogni gruppo di RR. ==Per verificare l'integrità della chiave pubblica dell'amministratore è necessario scendere la catena di fiducia partendo da una zona DNS sicura==. La chiave pubblica di una zona fidata è detta **trust anchor**.

DNSSEC amplia l'insieme dei RR:
- **DNSKEY** -> contiene la chiave pubblica dell'amministratore di zona
- **RRSIG** -> firma digitale di un RR
- **NSEC** -> conferma firmata della NON esistenza di un RR
- **DS** -> delegato che firma un RR, per garantire la condivisione tra le varie zone

## DANE
Lo scopo di DANE è quello di ==sostituire la dipendenza alle CA facendo affidamento sulla sicurezza fornita da DNSSEC==.
Sostanzialmente è un modo per introdurre i certificati X.509 nel sistema di sicurezza specificato da DNSSEC, ignorando le CA.

Il punto più debole di un sistema PKI sono proprio le CA più in alto nella gerarchia, se viene bucate una di esse allora i problemi di sicurezza si propagherebbero verso il basso.

DANE definisce un nuovo tipo di RR, detto **TLSA**, che può essere usato per autenticare i certificati TLS: quando un client riceve un certificato, interroga i TLSA RR di riferimento per quel dominio e compara le caratteristiche per validare il certificato.

## Sender Policy Framework (SPF)
SPF è lo standard per un dominio mittente di identificare e dichiarare i mittenti di posta elettronica.

==SPF consente al proprietario di un dominio di definire le regole per identificare i server autorizzati a mandare e-mail con un indirizzo del mittente in quel dominio==, utilizzando opportuni SPF resource records del DNS.

**Lo scopo principale di SPF è fornire un meccanismo per verificare l'autenticità dell'origine di un'email, attraverso i RR DNS.**

e.g.:
1. Server `220 foo.com SMTP Ready`
2. Client `HELO mta.example.net`
3. Server `250 OK`
4. Client `MAIL FROM:<alice@example.org>`
5. Server `OK`
6. ...
7. Client `From: alice.sender@example.net` (Header) 

Il mittente utilizza il tag `MAIL FROM:<alice@example.org>` indicando che il messaggio ha origine nel dominio `example.org`.
L'header specifica, però, l'indirizzo `alice.sender@example.net`.

**Il receivers utilizza un RR di tipo SPF verso `example.net` per controllare che `alice@example.org` sia un indirizzo mail valido.**

Un dominio mittente è obbligato a verificare l'identità di tutti i mittenti per quel dominio e ad aggiungere tutte le informazioni nel DNS database (e.g. un range di indirizzi IPv4 verificati come mittenti).



