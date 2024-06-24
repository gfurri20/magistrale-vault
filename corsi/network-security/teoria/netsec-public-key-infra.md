La sicurezza di una comunicazione crittografata dipende dalla segretezza delle chiavi, quindi è necessario utilizzare un sistema di gestione delle chiavi adeguato.

# Cryptographic Key Management

> [!info] Cryptographic Key Management
> Insieme di processi, protocolli ed attività utente atte alla gestione ed amministrazione delle chiavi di un sistema crittografico.

Comprende la generazione, protezione, trasferimento, scambio e uso delle chiavi.
==La sicurezza di un sistema crittografico dipende dal sistema che gestisce le chiavi.==

## Symmetric Key Distribution
Per fare in modo che un sistema crittografico simmetrico funzioni tra due host è necessario condividere la stessa chiave.

Una tecnica di distribuzione è considerata adeguata se:
- la condivisione delle chiavi è privata verso i soli host coinvolti
- gli aggiornamenti di chiavi sono frequenti per evitare di usare sempre la stessa

La distribuzione delle chiavi simmetriche può essere implementata sia attraverso crittografia simmetrica sia attraverso quella asimmetrica.

### Using Symmetric Cryptography
Dati due entità `A` e `B` esistono diverse possibilità di distribuzione delle chiavi simmetriche:
1. trasferimento fisico diretto tra `A` e `B`
2. trasferimento fisico mediante entità di terze parti `C`
3. trasferimento virtuale della chiave nuova diretto tra `A` e `B`, crittografando con la chiave precedente
4. trasferimento virtuale della chiave nuova mediante entità di terze parti `C`
Le prime due opzioni coinvolgono un trasferimento fisico e quindi sono utili solo in casi specifici, su Internet è un metodo inutilizzabile.

Diventa fondamentale, quindi, gestire delle entità di terze parti, dette **Key Distribution Centers** (KDC).

> [!info] Key Distribution Center
> Entità terza che genera o/e distribuisce le chiavi simmetriche di sessione per permettere la comunicazione sicura tra altre due entità

Nello specifico, il KDC, può operare in due modalità:
1. *modalità di traduzione* -> la chiave di sessione $K_s$ è generata da `A`, il `KDC` non farà altro che inoltrare a `B` la chiave (il `KDC` potrebbe anche relegare ad il compito di fare il forward)
2. *modalità di distribuzione* -> la chiave di sessione $K_s$ è generata da il `KDC` a seguito di una richiesta specifica:
	1. il `KDC` può inoltrare sia ad `A` che a `B`
	2. il `KDC` può inoltrare ad `A` che si occuperà di fare il forward

![[kdc.png]]
Le chiavi simmetriche di sessione possono essere distribuite lungo una gerarchia, le chiavi più in basso sono usate maggiormente ma devono essere cambiate spesso (i.e. **ephemeral keys**); mentre le chiavi più in alto permettono la generazione delle chiavi sottostanti e possiedono un ciclo di vita maggiore (i.e. **master keys**).

### Using Asymmetric Cryptography
Uno degli usi più utili della crittografia simmetrica è proprio lo scambio di chiavi.
Ci sono diversi approcci per lo scambio di chiavi di sessione tramite crittografia simmetrica.

#### Simple Approach

![[simple-key-exchange.png]]

1. `Alice` genera la coppia chiave pubblica, privata: $\{PU_a, PR_a\}$ e la invia a bob allegandola ad un proprio identificatore `Bob` -> $\{PU_a, ID_a\}$
2. `Bob` genera la chiave di sessione $K_s$, la incapsula con la chiave pubblica di `Alice`, e successivamente la invia ad `Alice` -> $E_{PU_A}(K_s)$
3. `Alice` decripta con la propria chiave privata ed ottiene $K_s$
4. Infine entrambi scartano le chiavi asimmetriche usate

Questo approccio, però, è vulnerabile ad attacchi MITM in quanto ==le chiavi non sono autenticate== ed un eventuale utente malevolo potrebbe interporsi nella comunicazione ed impersonare gli host.

![[mitm-simple-key-exchange.png]]

Il risultato è che `Alice` e `Bob` pensano di parlare privatamente tra di loro ma in realtà sono ascoltati da `Evil`.

#### Advance Approach
Per ==aggiungere confidenzialità ed autenticità== (ed evitare attacchi di tipo replay) è necessario migliorare lo scambio di messaggi, aggiungendo delle nonce.

Questo approccio rimane ancora vulnerabile ad alcuni attacchi MITM.

![[adv-asym-key-exchange.png]]


## Asymmetric Key Distribution
Anche le chiavi pubbliche asimmetriche devono poter essere condivise, per fare ciò si possono usare diverse tecniche:
1. *Public Announcement* -> condivisione in broadcast delle chiavi pubbliche
	-  approccio conveniente ma chiunque può condividere chiavi pubbliche
	- alcuni utenti malevoli potrebbero impersonare un altro utente ma distribuire la propria chiave pubblica
2. *Publicly Available Directory* -> mantenimento delle chiavi pubbliche in una repository pubblica gestita da un'entità autorizzata centrale
	- la registrazione della chiave e l'accesso alla repo devono essere autenticati
	- se un utente malevolo scopre la chiave privata della repository allora tutte le altre chiavi cadono
3. *Public-Key Authority* -> introduce l'incapsulamento dei messaggi dell'authority attraverso la propria chiave privata, in questo modo i messaggi sono autenticati
	- vengono introdotti timestamp e nonce per evitare attacchi replay
	- la comunicazione è caratterizzata da un maggior numero di messaggi perché è necessario eseguire le richieste
	- è buona pratica refreshare le chiavi spesso (aumenta il traffico)
	- l'==authority rimane un collo di bottiglia== a causa dell'alto rischio che corre
1. *Public-Key Certificates* -> vengono introdotti dei **certificati** che permettono lo scambio delle chiavi senza la l'obbligo di contattare l'authority ad ogni scambio
	- un ==certificato è composto da la chiave pubblica, un identificatore dell'owner e da una firma dell'autorità di fiducia==, detta certification authority
	-  l'utente presenta la propria chiave pubblica all'autorità e riceve il proprio certificato che potrà essere condiviso agli altri host
	- gli altri host, ricevuto il certificato, potranno verificarlo con la chiave pubblica della certification authority

Un certificato si presenta come:
$$C_A = E_{PR_{auth}}(T, ID_A, PU_A)$$
Il leak di una chiave privata non comporterebbe danni perché basterebbe rimuovere la validità al certificato di colui che ha perso la chiave, questo grazie alla presenza del `timestamp` all'interno del certificato che funge come data di scadenza.

Per gestire la formattazione dei certificati è stato creato uno standard universale chiamato: **X.509**.

### X.509 Certificates
