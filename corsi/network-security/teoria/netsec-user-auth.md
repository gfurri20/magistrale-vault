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
