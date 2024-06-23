L'obiettivo è difendersi dagli attacchi passivi ed attivi. Grazie alla semplice crittografia dei payload possiamo aumentare la garanzia di difesa contro gli attacchi passivi.

Gli attacchi attivi, d'altro canto, mirano a manipolare la comunicazione e non sempre la crittografia permette la massima protezione, e.g. attacchi di bit flipping possono permettere all'attaccante di modificare il payload a piacere.

# Message Authentication
Le procedure di Message Auth permettono di verificare che i messaggi ricevuti siano autentici:
1. verificano che l'origine sia autentica
2. verificano che il messaggio non sia stato manipolato

Lo scopo è quello di produrre un vero e proprio **fingerprint** del payload.

Questo si può fare in due modalità:
- *introducendo la crittografia* - il messaggio è cifrato
	- i due client condividono la chiave segreta, in questo modo solo chi la possiede può decriptare correttamente il payload (può essere rubata la chiave)
	- si possono introdurre codici di verifica, numeri di sequenza e timestamp per cercare di aumentare la sicurezza
- *senza la crittografia* - il messaggio è lasciato in chiaro, viene semplicemente autenticato
	- non c'è confidenzialità (potrebbe essere letto da altri)
	- viene aggiunto un `authentication tag` che permetterà di verificare l'originalità del messaggio

## One Way Functions
Questo `authentication tag` è generato da una **One Way Hash Function** che prende in input, solamente, il messaggio e genera una sequenza alfanumerica di lunghezza fissata detta *digest*. Non serve una chiave.

La caratteristica principale delle One Way Hash Functions è che, attraverso il solo digest non è possibile ricomporre il payload originale.

Quindi si prende il payload, si genera il suo digest e lo si allega al payload.
Si può aggiungere un layer crittografico in tre diverse modalità:
1. crittografia simmetrica
2. crittografia asimmetrica
3. usando un valore segreto condiviso

![[message_auth_modes.png]]
Dove:
- $K$ - chiave simmetrica
- $PR_a$ - chiave privata di $a$
- $PU_a$ - chiave pubblica di $a$
- $H$ - funzione one way che genera il digest

### Caratteristiche di correttezza
Una funzione one way hash $H$ per essere considerata **sicura** deve possedere delle caratteristiche precise:
1. $H$ può applicarsi ad *input* di *qualsiasi lunghezza*
2. $H$ produce un *output* di *lunghezza fissata*
3. $\forall x.H(x)$ è relativamente *facile da calcolare*
4. $\forall h . H(x) = h$ è computazionalmente *difficile trovare $x$*
5. $\forall x . H(x)$ è computazionalmente difficile trovare $y$ tale che $H(x) = H(y)$, in gergo si dice che $H$ è *debolmente resistente alle collisioni*
6. è computazionalmente difficile trovare una coppia $x, y$ tale che $H(x) = H(y)$, in gergo si dice che $H$ è *fortemente resistente alle collisioni*

Una secure one way functions può essere attaccata attraverso due tipi di approcci:
- **crypto-analysis** - sfrutta le eventuali falle logiche di un algoritmo
- **brute-force** - prova tutte le combinazioni, quindi la forza di un algoritmo dipende dalla lunghezza del digest

Ci sono *diverse implementazioni* di one way hash functions:
- **SHA** - Secure Hash Algorithms
	- funzione one way hash senza chiave, creata dal NIST all'inizio degli anni 90
	- esistono diverse versioni che si differenziano in base al numero di bit che compongono il digest in output, fino a SHA-512
	- divide il messaggio in blocchi e computa l'hash blocco per blocco utilizzando, nella formula l'hash del blocco precedente
	- si adatta poco ad essere un MAC, in quando non è stato progettato per questo scopo
- **HMAC** - key-Hashed Message Authentication Code
	- introduce una *chiave* nel processo di generazione del digest
	- *non utilizza una funzione hash specifica*, questo rende possibile una sostituzione nel caso in cui una funzione hash divenisse insicura
	- viene utilizzato in protocolli sicuri di Internet come IPSec e TLS
	- il messaggio viene suddiviso in blocchi di lunghezza fissata $n$. Viene poi selezionata una chiave segreta $K$. Se questa risulta essere più lunga di $n$ bit, a questa viene applicata la funzione $H$.
- **CMAC**
	- il MAC viene generato attraverso un algoritmo di crittografia simmetrica
	- di solito usa la modalità CBC di gestione dei blocchi

	![CMAC-CBC](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/CBC-MAC_structure_%28en%29.svg/600px-CBC-MAC_structure_%28en%29.svg.png)

- **CCM** - utilizza i cifrari a blocchi per creare il MAC, segue una procedura detta "authenticate-then-encrypt":
	- CMAC crea il message authentication code
	- successivamente il messaggio e il MAC creato vengono uniti e criptati usando la modalità CTR, rif.: [[netsec-symmetric-crypto#Block processing]]
	- questo metodo, quindi, garantisce ==confidenzialità== e ==autenticità== simultaneamente

# Public Cryptography
La crittografia a chiave pubblica (o semplicemente crittografia asimmetrica) non prevede la manipolazione diretta dei bit ma fa uso di **funzioni matematiche**.
Diffie e Hellman, nel 1976, furono i primi a teorizzare e sperimentare tale approccio.

La sostanza è semplice: ad ogni individuo sono associate **due chiavi**, una **privata** ed un **pubblica**. La prima è in possesso del singolo soggetto, mentre la seconda è, appunto, di dominio pubblico.

I tre usi più comuni sono:
1. *digital signature* - utilizzo della chiave privata per crittografare un payload, in questo modo il payload sarà leggibile da tutti coloro che possiedono la chiave pubblica, questo garantisce **autenticità**
		![digital-sign](https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Private_key_signing.svg/375px-Private_key_signing.svg.png)
1. *public-key encryption* - utilizzo della chiave pubblica per crittografare un payload, in questo modo solo chi possederà la rispettiva chiave privata potrà accedere al payload, ciò garantisce **confidenzialità**
		![public-key-enc](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Public_key_encryption.svg/375px-Public_key_encryption.svg.png)
1. *key exchange* - utilizzo combinato delle chiavi asimmetriche per lo scambio sicuro di eventuali chiavi simmetriche
		![key-exchange](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Public_key_shared_secret.svg/375px-Public_key_shared_secret.svg.png)

Esistono diverse implementazioni pratiche:

| Implementazione  | enc/dec | digital sign | key exchange |
| ---------------- | ------- | ------------ | ------------ |
| *Diffie-Hellman* |         |              |              |
