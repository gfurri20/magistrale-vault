# User Authentication

> [!info] Autenticazione Utente
> Il processo che verifica l'identità dichiarata dall'utente, dall'applicazione o dal sistema, utile per accedere ad un determinato servizio

L'autenticazione permette alle aziende di aumentare la sicurezza dei propri servizi, limitando l'accesso ai soli utenti autorizzati, inoltre:
$$\texttt{Message Authentication} \neq \texttt{User Authentication}$$
L'autenticazione del messaggio verifica che il messaggio non sia stato manomesso e che la sorgente sia autentica.

Esistono due tipi di processi ai autenticazione:
- **mutua autenticazione** -> autentica entrambe le entità (o tutte) comprese nella comunicazione
- **autenticazione one-way** -> coinvolge un trasferimento singolo di informazione da `A` a `B`

## Authentication Principles
Definiamo tre principi su cui si basa l'autenticazione:
- **Digital identity** -> rappresentazione univoca dell'utente in un determinato contesto, composta da un insieme di attributi
- **Identity proofing** -> processo che colleziona, valida e verifica la *digital identity* di un individuo
- **Digital authentication** -> processo che determina la validità di un mezzo di autenticazione utilizzato per validare la *digital identity*

## Authentication Factors
Un'utente può autenticarsi tramite uno (o una combinazione dei seguenti fattori):
- **qualcosa che si conosce** -> conoscenza di un segreto (e.g. password)
	- facile da usare
	- condivisibile e dimenticabile
	- facile da indovinare se banale
- **qualcosa che si possiede** -> entità fisica, posseduta, che può essere utilizzata come mezzo di autenticazione (e.g. USB token)
	- sicure se conservate adeguatamente
	- macchinose da usare
	- possono essere perse
	- possono essere duplicate
- **qualcosa che si è** -> identificazione attraverso un carattere biometrico (e.g. impronta digitale)
	- non possono essere condivise
	- il clone è difficile da fare
	- esistono falsi positivi e falsi negativi

Un processo di autenticazione può coinvolgere un singolo fattore, oppure una combinazione di fattori. Nel secondo caso si parla, appunto, di **autenticazione multi-fattore**.

## Replay Attacks
Il problema centrale dei processi autenticazione è che devono garantire:
1. **Confidenzialità** -> comunicazione criptata e ciò richiede l'esistenza di chiavi di sessione (quindi key exchange mechanisms)
2. **Timeliness** -> tempismo per evitare attacchi di tipo replay che potrebbero compromettere il servizio

Ci sono diverse modalità di attacco attraverso il replay dei messaggi:
1. re-invio più tardi nel tempo di un messaggio catturato
2. invio di un messaggio con timestamp valido nella finestra di tempo accettata
3. come (2) ma eliminando il messaggio originale, intercettandolo
4. reflections attacks

Per cercare di difendersi da queste tipologie di attacchi è possibile adottare diverse contromisure:
- utilizzare un *sequence number* per ordinare il flusso di messaggi, è una tecnica troppo onerosa che nono viene usata
- utilizzare dei *timestamps* per individuare messaggi e fresh e non, richiede la sincronizzazione dei clock
	- si potrebbe attaccare i clock per de-sincronizzare i dispositivi utente e quindi per sabotare il controllo della finestra temporale
- utilizzare delle *nonce*, ovvero delle stringhe alfanumeriche generate random che fungono da challenge/response

## User authentication con crittografia simmetrica
### Kerberos (Mutua Autenticazione)

>[!important] Kerberos
>Kerberos è un protocollo di mutua autenticazione centralizzato basato solo su chiavi simmetriche.

Utilizza un authentication server (AS) centrale per autenticare utenti con server e server con utenti.

L'autenticazione di una semplice postazione di lavoro non può sostituirsi all'autenticazione di un utente:
- un utente non autorizzato potrebbe utilizzare la postazione di un utente autorizzato
- un utente potrebbe alterare gli indirizzi IP sulla rete per cambiare le postazioni
- un utente potrebbe compiere un replay attack

Kerberos si prepone essere:
- **Sicuro** -> un ascoltatore malevolo non riesce ad ottenere abbastanza informazioni per impersonare un utente
- **Affidabile** -> un AS può essere immediatamente rimpiazzato da server di backup
- **Trasparente** -> idealmente un utente non sa che l'inserimento della semplice password comporta un processo gestito da Kerberos
- **Scalabile** -> dovrebbe essere in grado di supportare un largo numero di utenti e servers

#### Kerberos v.4 Architecture
L'ultima specifica della versione 4 di Kerberos specifica 4 attori:
- il **client** che possiede una propria `password` di accesso
- **AS** (Authentication Server) centralizzato, che conosce le `password` (di solito salvate hashate) di tutti gli utenti all'interno della rete
- **TGS** (Ticket-Granting Server) che distribuisce un `ticket` agli utenti autorizzati dall'AS rispetto ad uno specifico servizio
- il **servizio** a cui l'utente è interessato ad accedere a cui verrà presentato il `ticket`, anche il server del servizio ha l'obbligo di autenticarsi nei confronti del client

Esistono due tipi di `ticket`:
- il `granting-ticket` ovvero l'autorizzazione concessa dal AS a ottenere il `ticket` di servizio dal TGS
- il `ticket` di servizio che è un oggetto distribuito dal TGS che viene generato previa autenticazione dell'utente per ogni specifico servizio offerto sulla rete.
Un utente che ottiene un `ticket` per un determinato servizio può salvarlo per ri-utilizzarlo più avanti nel tempo (entro una certa scadenza). In questo modo non si affolla di richieste né l'AS né il TGS.

==In sostanza con l'autenticazione un utente può richiedere più ticket e con un ticket un utente può richiedere più accessi al servizio.==

Kerberos v.4 si basa su DES e quindi individuiamo le chiavi simmetriche usate per la codifica:
- $K_{c,as}$ -> la chiave simmetrica ottenuta dalla `password` dell'utente condivisa tra client e AS
- $K_{c,tgs}$ -> la chiave simmetrica condivisa tra client e TGS
- $\textcolor{green}{K_{c,v}}$ -> la chiave simmetrica condivisa tra client e servizio
- $K_{v,as}$ -> la chiave simmetrica condivisa tra servizio e AS
- $K_{v,tgs}$ -> la chiave simmetrica condivisa tra servizio e TGS
- $K_{as,tgs}$ -> la chiave simmetrica condivisa tra AS e TGS
![[kerberos-v4-scenario.png]]
Gli oggetti principali sono:
- il `granting-ticket`, ovvero il ticket utile per ottenere il `ticket` di servizio, è codificato con la chiave tra AS e TGS, quindi il client non può fare altro che inoltrarlo
$$\textcolor{blue}{Ticket_{tgs} = \{K_{c,tgs}, ID_c, AD_c, ID_{tgs}, TS_2, LT_2\}_{K_{as,tgs}}}$$
- `autenticatore` tra client e TGS, ovvero un oggetto che permette di provare che il client che ha eseguito la richiesta è anche colui che riceverà il ticket di servizio
$$\textcolor{orange}{Auth_{c,tgs} = \{ID_c, AD_c, TS_3\}_{K_{c,tgs}}}$$
- il `ticket` di servizio, ovvero il ticket utile per ottenere l'accesso al servizio desiderato, è codificato con la chiave tra servizio e TGS, quindi il client non può fare altro che inoltrarlo
$$\textcolor{red}{ Ticket_v = \{\textcolor{green}{K_{c,v}}, ID_c, AD_c, ID_v, TS_4, LT_4\}_{K_{v,tgs}} }$$
- `autenticatore` tra client e servizio, ovvero un oggetto che permette di provare che il client che utilizza il ticket è anche colui che l'ha richiesto
$$\textcolor{violet}{Auth_{c,v} = \{ID_c, AD_c, TS_5\}_{K_{c,v}}}$$

Individuiamo ulteriori elementi:
- $LT_x$ -> lifetime, ovvero una scadenza di validità
- $AD_x$ -> l'indirizzo IP (o del protocollo usato) di $x$

Il passaggio (6) dell'immagine permette di garantire la **mutua autenticazione**, non è sempre obbligatorio, dipende dalle impostazioni e policies.

#### Kerberos Realms
L'insieme di tutti gli utenti associati ad un determinato AS e TGS è detto Kerberos Realm, all'interno di quest'ultimo esistono molteplici servizi ai quali i client possono accedere.

Potrebbe succedere che un utente voglia accedere ad un servizio presente su un Realm diverso da quello a cui appartiene, in questo caso il TGS locale non produrrà il `ticket` di servizio ma bensì un `remote-ticket` che potrà essere presentato ad un TGS esterno per ottener il `ticket` di servizio esterno utile per accedere al servizio non locale desiderato.

Ovviamente questo metodo necessità di un numero elevato di chiavi tra entità.

## Kerberos v.5
Kerberos v.5 apporta delle migliorie tecniche alla v.4:
- sostituisce DES con **AES**
- migliora i $LT_x$ aggiungendo una data di inizio ed una di fine
- authentication forwarding, permette all'utente di accedere a più servizi in modo transitivo senza ri-eseguire l'autenticazione
- **migliora l'autenticazione tra Realms**, utilizzando meno chiavi
- rimuove la doppia cifratura nei messaggi (2) e (4) per snellire il processo
- aggiunge dei meccanismi che garantiscono **integrità**
- rende più difficoltosi attacchi di brute-force sulla password (non li evita)

---

## User authentication con crittografia asimmetrica

### Mutua autenticazione
Possiamo individuare alcuni protocolli di mutua autenticazione basati su chiave pubblica/privata:
- **Denning Sacco protocol** [[netsec-public-key-infra#Denning-Sacco Protocol]] -> utilizza un AS centralizzato per distribuire i certificati ma richiede la sincronizzazione veritiera dei clock
- **Woo Lam protocol** -> con questo approccio vengono usate delle nonce al posto dei timestamp
Entrambi i protocolli hanno comunque delle debolezze e questo dimostra quanto sia difficile creare un protocollo solido di autenticazione.

### Autenticazione one-way
L'autenticazione one-way nella sua forma più semplice stabilisce se un token di autenticazione generato da `A` sia effettivamente inviato al destinatario `B`.

Vediamola per gradi.

Possiamo garantire **non repudiabilità** e **authentication** con questo payload:
$$A \rightarrow B: \{msg, [msg]_{PRa,}, [Cert_a]_{PR_{as}}\}$$
Quindi `B`:
1. Utilizza la chiave pubblica di `AS` per recuperare $Cert_a$ e quindi la chiave pubblica di A $PU_a$
2. Successivamente usa la chiave pubblica di `A` per verificare la signature

Se si vuole introdurre anche la **confidenzialità** allora si incapsula tutto con la chiave pubblica di `B`:
$$A \rightarrow B: \{msg, [msg]_{PRa,}, [Cert_a]_{PR_{as}}\}_{PU_b}$$
Si può introdurre un ulteriore grado di sicurezza utilizzando un one-time pad e quindi una one-time key $K$:
$$A \rightarrow B: \{\{msg\}_K, [msg]_{PRa,}, [Cert_a]_{PR_{as}}, K\}_{PU_b}$$
---

# Federated Identity Management
Un concetto che permette di utilizzare un'identità comune per molteplici servizi.

==L'obiettivo è quello di associare ad ogni utente un'identità (insieme di attributi) che può essere utilizzata per essere autenticati su diversi servizi.==
Questa è la base delle tecnologie e dei protocolli di **SSO** (Single Sign On), che permettono molteplici accessi attraverso una singola autenticazione.

Quando un utente vuole accedere ad un servizio attraverso SSO, viene interrogato un server detto **Identity Provider** che, previa autenticazione, preleverà l'identità dell'utente.
Tale identità verrà inoltrata al **Service Provider** che provvederà ad aprire la sessione con l'utente.