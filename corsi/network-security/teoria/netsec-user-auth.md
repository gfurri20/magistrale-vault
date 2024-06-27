# User Authentication

> [!info] Autenticazione Utente
> Il processo che verifica l'identità dichiarata dall'utente, dall'applicazione o dal sistema, utile per accedere ad un determinato servizio

L'autenticazione permette alle aziende di aumentare la sicurezza dei propri servizi, limitando l'accesso ai soli utenti autorizzati, inoltre:
$$\texttt{Message Authentication} \neq \texttt{User Authentication}$$
L'autenticazione del messaggio verifica che il messaggio non sia stato manomesso e che la sorgente sia autentica.

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

# Kerberos
Kerberos è un **servizio di mutua autenticazione centralizzato**. Utilizza un authentication server (AS) centrale per autenticare utenti con server e server con utenti.
Fa affidamento **solamente all'uso di chiavi simmetriche** di sessione.

L'autenticazione di una semplice postazione di lavoro non può sostituirsi all'autenticazione di un utente:
- un utente non autorizzato potrebbe utilizzare la postazione di un utente autorizzato
- un utente potrebbe alterare gli indirizzi IP sulla rete per cambiare le postazioni
- un utente potrebbe compiere un replay attack

Kerberos si prepone essere:
- **Sicuro** -> un ascoltatore malevolo non riesce ad ottenere abbastanza informazioni per impersonare un utente
- **Reliable** -> un AS può essere immediatamente rimpiazzato da server di backup
- **Transparent** -> idealmente un utente non sa che l'inserimento della semplice password comporta un processo gestito da Kerberos
- **Scalable** -> dovrebbe essere in grado di supportare un largo numero di utenti e servers

## Kerberos v.4 Architecture
L'ultima specifica della versione 4 di Kerberos specifica 4 attori:
- il **client** che possiede una propria `password` di accesso
- **AS** (Authentication Server) centralizzato, che conosce le `password` di tutti gli utenti all'interno della rete
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
- $K_{c,v}$ -> la chiave simmetrica condivisa tra client e servizio
- $K_{v,as}$ -> la chiave simmetrica condivisa tra servizio e AS
- $K_{v,tgs}$ -> la chiave simmetrica condivisa tra servizio e TGS
- $K_{as,tgs}$ -> la chiave simmetrica condivisa tra AS e TGS
