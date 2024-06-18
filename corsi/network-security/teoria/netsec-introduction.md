# Definizioni ed Obiettivi

> [!info] Cybersecurity
> Un insieme di strumenti, politiche, concetti, salvaguardie, linee guida, approcci di gestione del rischio, azioni, formazione, pratiche migliori, assicurazioni e tecnologie utilizzate per proteggere l'ambiente cibernetico e i beni degli utenti e delle organizzazioni.

Distinguiamo due approcci alla sicurezza in base all'ambito:
- **Information Security** - fa riferimento specifico alla protezione delle informazioni
- **Network Security** - fa riferimento specifico alla protezione delle infrastrutture di rete e dei servizi che implementano

## Obiettivi
La sicurezza informatica si basa sul cercare di garantire costantemente 6 obiettivi specifici che si articolano differentemente in base all'ambito di applicazione, sono specificati qua: [[02_10_2023-introduzione#I Sei Pilastri]]

L'ambito che ci interessa maggiormente è la **Network Security**, e quindi, tali obiettivi assumono un carattere specifico:
- *Confidentiality* - assicura che utenti non autorizzati non abbiano accesso a risorse private
- *Integrity* - assicura che un servizio (o infrastruttura) svolga i compiti per il quale è stato progettato e costruito
- *Availability* - assicura che un servizio (o infrastruttura) sia sempre disponibile nei momenti in cui è stat progettata per esserlo; in sostanza cerca di evitare disservizi

---
# OSI Security Architecture
Definiamo gli elementi che caratterizzano l'architettura di sicurezza definita dal modello OSI.

> [!warning] Security Attacks
> Azioni che compromettono la sicurezza delle informazioni

> [!tip] Security Services
> Servizi che migliorano la sicurezza dei sistemi di elaborazione dati e dei trasferimenti di informazioni

> [!note] Security Mechanisms
> Processi o dispositivi che rilevano, prevengono, mitigano o recuperano da un Security Attack

## ⚠ Security Attack
Innanzitutto definiamo una sostanziale differenza tra **Threats** e **Attacks**:
- **Threats** - *Potenziali* violazioni della sicurezza che potrebbero causare danni sfruttando eventuali vulnerabilità
- **Attacks** - Tentativi *deliberati* di eludere i servizi di sicurezza e violare le politiche di sicurezza del sistema

In generale esistono due tipi di attacchi (ref.: [RFC 4949](https://datatracker.ietf.org/doc/html/rfc4949)): **Passivi** e **Attivi**.

### Attacchi Passivi
Tentativo di intercettare informazioni utili ma, per fare ciò, *il sistema vittima non viene intaccato*.

Spesso questi attacchi sono effettuati con l'obiettivo di individuare eventuali informazioni sensibili, credenziali o vulnerabilità del sistema, attraverso:
- eavesdropping
- analisi del traffico di rete

### Attacchi Attivi
Tentativo di modifica del flusso di dati o creazione di flussi falsi, con l'obiettivo di *alterare le risorse del sistema vittima* oppure di manomettere i servizi esposti.

Ci sono svariati tipi di attacchi attivi, ne distinguiamo alcuni:
- **Impersonation** - tentativo di impersonare un'entità diversa per accedere a risorse private
- **Replay** - tentativo di ritrasmettere pacchetti catturati in precedenza per ottenere autorizzazioni non legittime
- **Data Modification** - tentativo di modifica di pacchetti o messaggi per cercare di ottenere autorizzazioni non legittime
- **Denial Of Services** - tentativo di mettere fuori uso un servizio

## 🔥 Security Services
Ci sono svariati servizi, ognuno con il proprio compito, che permettono di aumentare il grado di sicurezza di un sistema o infrastruttura.

### Authentication
Assicura che le comunicazioni siano autentiche, *verificando l'identità delle entità* coinvolte, questo per cercare di evitare attacchi di impersonificazione.

Lo standard [X.800](https://www.itu.int/rec/T-REC-X.800-199103-I/en) stabilisce due servizi di autenticazione:
- **Peer Entity Auth** - Fornisce un meccanismo di conferma tra due entità pari, ovvero due entità che utilizzano lo stesso protocollo di comunicazione su sistemi diversi 
- **Data Origin Auth** - Fornisce la conferma dell'origine di un'unità di dati

### Access Control
Limitazione e *controllo dell'accesso ai sistemi* e alle applicazioni attraverso protocolli di comunicazione, basato sull'*identificazione e autenticazione* delle entità.

Per approfondire: [[20_11_2023-access-control]].

### Data Confidentiality
Protezione dei dati trasmessi da attacchi passivi, si possono cercare di proteggere intere comunicazioni oppure singoli messaggi.
Inoltre è inclusa la protezione del flusso di traffico dall'analisi, mascherando le informazioni che permettono di identificare le caratteristiche della comunicazione.

### Data Integrity
Assicurazione che i dati non siano alterati in modo non autorizzato durante la trasmissione.

Anche in questo caso è possibile implementare meccanismi *connection-oriented*, che mirano a proteggere intere comunicazioni e quindi insiemi di messaggi; oppure *connection-less*, che mirano a proteggere singoli payload o messaggi, disinteressandosi del contesto.

### Non-repudiation
Previene che mittenti o destinatari neghino di aver trasmesso o ricevuto un messaggio.

### Availability Service
Protegge i sistemi per garantirne la disponibilità, affrontando le preoccupazioni relative agli attacchi di DoS.
Il mantenimento della disponibilità fa grande affidamento sui servizi di [[#Access Control]].


## 🖋 Security Mechanisms
Tecnicamente sono gli strumenti che permettono di implementare i [[#🔥 Security Services]] nella pratica.

Ormai i meccanismi di sicurezza sono molti e di svariate topologie:
- algoritmi crittografici
- firme digitali per provare l'integrità delle informazioni trasferite
- protocolli di autenticazione per identificare le entità tra loro
- modifiche controllate dei messaggi per rendere più difficoltosa l'analisi
- controllo delle rotte di rete per intervenire in caso di problemi sul percorso che seguono i dati

In particolare gli algoritmi crittografici si snodano in diversi modi.

### Algoritmi crittografici
Innanzitutto un algoritmo crittografico sono procedure che permettono di modificare in base a diversi obiettivi.

Ad ogni obiettivo è associato una categoria di algoritmi crittografici:
- 