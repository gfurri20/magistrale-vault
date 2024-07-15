La crittografia simmetrica prevede l'uso di una singola chiave segreta che permette di criptare e decriptare i messaggi.

![sym_crypto_img](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Simple_symmetric_encryption.png/640px-Simple_symmetric_encryption.png)

I requisiti principali sono due:
- una **chiave segreta**
- un **algoritmo** di crittografia simmetrico **robusto**
==La sicurezza della crittografia simmetrica dipende dalla segretezza della chiave, non dall'algoritmo.==

Spesso le funzioni di cifratura vengono svolte da chip dedicati.

Gli algoritmi simmetrici di cifratura si dividono, principalmente, in due categorie:
- **cifrari a blocchi**
- **cifrari a flusso**

Uno dei problemi principali dei cifrari simmetrici è la segretezza della chiave, nel senso che essa deve essere distribuita mantenendo la segretezza; difatti una delle funzionalità dei cifrari Asimmetrici è proprio quello di distribuzione delle chiavi simmetriche.

Tipicamente le chiavi sono distribuite su una gerarchia che individua:
- **chiavi di sessione** - utilizzate per cifrare dati specifici di una singola sessione, poi scartate
- **chiavi master** - utilizzate per incapsulare chiavi di sessione a scopi di condivisione

## Pseudo-random numbers
Tutti i protocolli di rete fanno un ampio uso dei generatori di numeri casuali, se pensiamo alle chiavi di cifratura non sono altro che sequenze di numeri generati pseudo-casualmente.

Un generatore di numeri random deve garantire, durante la fase di "creazione":
- **Randomness** - il tasso di casualità di un numero è definito da:
	- distribuzione *uniforme* dei bit (di equal probabilità per ogni bit)
	- *indipendenza* tra sequenze diverse
- **Unpredictability** - impossibilità (almeno pratica) di prevedere le possibili future generazioni

I generatori di numeri casuali si dividono in:
- **TRNG (True Random Number Generators)** - basati su fenomeni fisici
- **PRNG (Pseudo Random Number Generators)** - basati su algoritmi deterministici (necessitano di un seed spesso generato da un TRNG)
- **PRF (Pseudo Random Functions)** - basati su algoritmi deterministici ed influenzati dal contesto in cui operano (necessitano di un seed spesso generato da un TRNG)​

## Cifrari a blocchi
Tale approccio è il più comune e consiste nel dividere il payload in blocchi di egual misura e processare un blocco alla volta, sequenzialmente.

Alla base dei cifrari a blocchi c'è la cosiddetta **Feistel Network**, che permette di introdurre un certo grado di *confusione* e *diffusione* durante la procedura crittografica.
Entrambi i concetti sono stati definiti da Shannon.

>[!info] Diffusione
> Cerca di rendere inefficace l'analisi statistica del testo, aumentando la differenza che c'è tra il plain-text ed il cipher-text

>[!info] Confusione
> Cerca di aumentare il grado di separazione tra il plain-text, la chiave di cifratura e il cipher-text, aumentando al massimo l'ambiguità in uscita

La rete di Feistel processa i dati attraverso una *serie di round*, ad ogni round viene applicata in ordine, un'operazione di sostituzione e, successivamente, una trasposizione. (per approfondire: [Feistel Network](https://www.tutorialspoint.com/cryptography/feistel_block_cipher.htm)).

I principali algoritmi di crittografia simmetrici sono:
- **DES** (**D**ata **E**ncryption **S**tandard)
- **Triple DES**
- **AES** (**A**dvanced **E**ncryption **S**tandard)

### DES
DES è stato il primo standard di crittografia simmetrico, al giorno d'oggi non è più usato perché considerato **non sicuro**.

Utilizza una versione semplificata della rete di Feistel a 16 round con chiavi di 56 bits (in realtà la chiave è 64 bit ma 8 sono bit di controllo).

La causa principale che lo rende insicuro è proprio la chiave da 56 bits, facilmente attaccabile anche a forza bruta.

### Triple DES
Triple DES non è altro che la ripetizione tripla di DES, questo con l'obiettivo di aumentare la grandezza della chiave, aggregando tre chiavi da 56 bits. In totale 168 bits.
In questo modo non era necessario andare a modificare l'algoritmo per aumentare la grandezza della chiave.

In questo modo, però, l'inefficienza aumenta a causa della tripla applicazione di DES.

![TDES](https://www.splunk.com/content/dam/splunk-blogs/images/en_us/2023/02/triple-des2.png)

### AES
AES è lo standard di crittografia simmetrica a blocchi più recente (1997). Aumenta la sicurezza e l'efficienza di TDES (3 applicazioni di DES significa essere tre volte più lento), significativamente, attraverso blocchi di 128 bits e chiavi che variano da 128, 192 e 256 bits.

Inoltre AES non si basa sulla rete di Feistel perché elabora i blocchi in parallelo per massimizzare l'efficienza. Ovviamente i principi di *confusione* e *diffusione* sono mantenuti.

### Block processing
Un algoritmo di crittografia simmetrica processa un blocco alla volta.
Quindi è possibile utilizzare modalità di processing dei blocchi differente, nello specifico ne esistono quattro:
- **ECB** -> Ogni blocco di plain-text è cifrato indipendentemente usando la stessa chiave, il che può portare a problemi di sicurezza per messaggi lunghi e strutturati
	- blocchi con lo stesso testo vengono cifrati con lo stesso cipher-text (attacchi padding oracle)
	- NON usa un IV (initialization vector)
- **CBC** -> Ogni blocco di plain-text è XORato con il blocco cifrato precedente prima di essere cifrato, migliorando la sicurezza (non al massimo perché soffre ancora contro attacchi di bit-flipping).
- **CFB** -> Il plain-text è diviso in segmenti e ogni segmento è cifrato separatamente ed influenzato dal segmento precedente attraverso diverse operazioni (tra cui shifts e xors)
- **CTR** -> Permette la *cifratura parallela* dei blocchi, migliorando l'efficienza hardware e software.
	- l'i-esimo blocco è acceduto random, aumentando le prestazioni
	- è sicuro almeno tanto quanto gli altri processing
	- richiede l'implementazione solo dell'algoritmo di cifratura e non di de-cifratura

## Cifrari a flusso
I cifrari simmetrici a flusso (stream ciphers) sono un tipo di crittografia simmetrica che cifra i dati un bit o un byte alla volta.

Sfruttano una chiave di flusso (**keystream**) che viene combinata con il plain-text tramite un'operazione di XOR per produrre il cipher-text.
La chiave di flusso deve essere il più simile possibile ad una sequenza di numeri random, in modo da rendere il cipher-text il più ambiguo possibile rispetto al testo originale.

Oggi giorno un keystream accettabile, per essere considerato sicuro, è almeno lungo 128 bits.

Un esempio di algoritmo di cifratura simmetrica a flusso è **RC4**, veniva utilizzato in SSL perché sfruttava l'uso di permutazioni random.

## Dove Crittografare
Le funzionalità di crittografia possono essere impiegate a diversi livelli del modello ISO/OSI:
- **Link Enc** - ai livelli 1 e 2
	- cifra e decifra dati su ogni singolo link della rete
- **End-to-End Enc** - ai livelli 3, 4, 5, 6 e 7
	- i dati vengono cifrati dal mittente originale e decifrati dal destinatario finale







