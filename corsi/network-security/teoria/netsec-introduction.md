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
Innanzitutto, un algoritmo crittografico è una procedura che permette di cifrare i dati per cercare di renderli visibili solo a coloro che sono autorizzati.

Gli algoritmi di crittografia possono essere divisi in diverse categorie.
- Reversibilità del payload:
	- algoritmi **reversibili** - cripta i dati in una maniera tale che possano essere decriptati
	- algoritmi **irreversibili** - cripta di dati in modo che non possa essere recuperato il contenuto originale, questi meccanismi vengono utilizzati per implementare protocolli di hashing e firma digitale
- Tipologia di operazioni che vengono applicate al testo da cifrare:
	- **Sostituzioni** - ogni elemento all'interno del testo da cifrare è mappato ad un *diverso* elemento
	- **Trasposizioni** - gli elementi del testo da cifrare sono ri-arrangiati nel testo cifrato, senza perdita di informazione
	- **Ibridi** - applica entrambe le operazioni precedenti in diversi stages
- Numero di chiavi crittografiche che vengono utilizzate durante il processo di codifica:
	- **Keyless** - nessuna chiave
	- **Single Key** - singola chiave di cifratura
	- **Two Keys** - coppia di chiavi distinte

#### Cryptanalysis
Un sistema di crittografia è considerato computazionalmente sicuro se:
1. Il **costo** per rompere il cifrario supera il valore delle informazioni cifrate
2. Il **tempo** richiesto per rompere il cifrario supera la vita utile delle informazioni

#### Key-less
Gli algoritmi key-less non utilizzano chiavi. I più famosi sono funzioni che trasformano informazioni in hash o digest.
Gli hash spesso vengono usati per verificare l'integrità di un file oppure per salvare le password nei database.
Inoltre, fanno parte di questa categoria i generatori di numeri (pseudo)-random.

#### Single Key
Ref.: [[netsec-symmetric-crypto]]
Gli algoritmi Single Key sono dipendenti da una chiave singola segreta.
Tendenzialmente quando si parla di Single Key Algorithms si fa riferimento agli algoritmi di **crittografia simmetrica**.

Questo tipo di sistemi utilizzano la stessa chiave segreta per criptare e decriptare il contenuto.

A loro volta si dividono in:
- **cifrari a blocchi** - cifra il payload dividendolo in blocchi di lunghezza prefissata (e.g. DES)
- **cifrari a flusso** - cifra il payload operando sulla sequenza di bit che compongono il payload
- **message authentication code (MAC)** - nello specifico il MAC è un'entità, che viene allegata al payload, che permette di verificare l'integrità del messaggio. Per validare il messaggio viene svolto un controllo tra il MAC calcolato dal messaggio ricevuto ed il MAC allegato

#### Two Key
Ref.: [[netsec-public-key-crypto]]
Gli algoritmi Two Key fanno affidamento su due chiavi dette, rispettivamente, *chiave pubblica* e *chiave privata*.
Fanno riferimento agli algoritmi di **crittografia asimmetrica**.

A loro volta si sotto-strutturano in:
- **Digital Signature Algorithm** - generano una firma che permette di verificare l'autenticità del messaggio
- **Key Exchange** - permettono di implementare protocolli per lo scambio di chiavi simmetriche
- **User Authentication** - permettono di implementare protocolli di autenticazione utente

---

# Network Security
La Network Security mira a proteggere due elementi fondamentali:
- La **comunicazione** tra entità - attraverso specifici protocolli che definiscono standard e procedure che governano l'ordine di trasmissione dei dati (e.g. HTTPS)
- I **dispositivi** fisici - attraverso strumenti che hanno l'obiettivo di analizzare il traffico in entrata ed uscita del dispositivo

Per proteggere i dispositivi fisici ci sono tre possibilità
- **Firewall** - soluzione HW/SW che permette di limitare gli accessi o il traffico ai dispositivi in base a delle *politiche di sicurezza*, sostanzialmente agisce da filtro
- **Intrusion detection** - soluzione HW/SW che analizza il traffico sulla rete con l'obiettivo di individuare eventuali attacchi in corso
- **Intrusion prevention** - soluzione HW/SW creata per rilevare attività sospette, tentativi di attacco oppure rischi di sicurezza

---

# Trust Model
La messa in sicurezza di un'infrastruttura non è sicuramente un processo banale, e spesso introduce dei gradi di complessità che tendono anche ad appesantire i processi esposti.

Quindi, alcune volte è utile prendersi dei rischi e "fidarsi" del fatto che se anche avviene un'attacco esso causa danni limitati o, comunque, reversibili.

Per questo motivo viene definito un **modello di fiducia** che specifica quali rischi un'organizzazione si permette.

>[!info] Fiducia
>La fiducia è la confidenza che un'entità agirà in modo da non compromettere la sicurezza dell'utente del sistema di cui quell'entità fa parte.

Definiamo tre concetti rilevanti che caratterizzano un **modello di fiducia**.
1. **Affidabilità (Trustworthiness)** - caratteristica di un'entità che riflette il grado di merito di fiducia che tale entità possiede
2. **Propensione a fidarsi (Propensity to trust)** - tendenza a essere disposti a fidarsi degli altri in una vasta gamma di situazioni e obiettivi di fiducia. Questo suggerisce che ogni individuo ha un livello di base di fiducia che influenzerà la sua disponibilità a fare affidamento sulle parole e azioni degli altri
3. **Rischio (Risk)** - misura in cui un'entità è minacciata da una circostanza o evento potenziale, e tipicamente una funzione di:
    - gli impatti negativi che sorgerebbero se la circostanza o l'evento si verificasse
    - la probabilità di occorrenza

Inoltre possiamo specificare il concetto di fiducia nei confronti di tre diverse entità:
- fiducia nei confronti dell'**individuo** - l'individuo può essere interno (il dipendente) oppure esterno (i clienti)
- fiducia nei confronti di altre **aziende** - spesso un'azienda fa affidamento su sistemi e servizi offerti da aziende esterne attraverso una *relazione di fiducia*
- fiducia nei confronti del **sistema informativo** - la robustezza del sistema informatico che le aziende adottano

Una *relazione di fiducia* può essere stabilità in diversi modi:
- attraverso un'azienda authority che assicura il tasso di fiducia
- attraverso una relazione di fiducia già esistente o storicamente solida



