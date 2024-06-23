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
- SHA - Secure Hash Algorithms
	- funzione one way hash senza chiave, creata dal NIST all'inizio degli anni 90
	- esistono diverse versioni che si differenziano in base al numero di bit che compongono il digest in output, fino a SHA-512
	- divide il messaggio in blocchi e computa l'hash blocco per blocco utilizzando, nella formula l'hash del blocco precedente
- HMAC - key-Hashed Message Authentication Code



