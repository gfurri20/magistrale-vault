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

## Cifrari a blocchi
Tale approccio è il più comune e consiste nel dividere il payload in blocchi di egual misura e processare un blocco alla volta, sequenzialmente.

Alla base dei cifrari a blocchi c'è la cosiddetta **Feistel Network**, che permette di introdurre un certo grado di *confusione* e *diffusione* durante la procedura crittografica.
Entrambi i concetti sono stati definiti da Shannon.

>[!info] Diffusione
> Cerca di rendere inefficace l'analisi statistica del testo, aumentando la differenza che c'è tra il plain-text ed il cipher-text

>[!info] Confusione
> Cerca di aumentare il grado di separazione tra il plain-text, la chiave di cifratura e il cipher-text, aumentando al massimo l'ambiguità in uscita

La rete di Feistel processa i dati attraverso una serie di round, ad ogni round viene applicata in ordine, un'operazione di sostituzione e, successivamente, una trasposizione. (per approfondire: [Feistel Network](https://www.tutorialspoint.com/cryptography/feistel_block_cipher.htm)).

I principali algoritmi di crittografia simmetrici sono:
- **DES** (**D**ata **E**ncryption **S**tandard)
- **Triple DES**
- **AES** (**A**dvanced **E**ncryption **S**tandard)

### DES
DES è stato il primo standard di crittografia simmetrico, al giorno d'oggi non è più usato perché considerato **non sicuro**.

Utilizza una versione semplificata della rete di Feistel a 16 round con chiavi di 56 bits (in realtà la chiave è 64 bit ma 8 sono bit di controllo).

La causa principale che lo rende insicuro è proprio la chiave da 56 bits, facilmente attaccabile anche a forza bruta.

### Triple DES
TripleDES non è altro che la ripetizione tripla di DES, questo con l'obiettivo di aumentare la grandezza della chiave, aggregando tre chiavi da 56 bits. In totale 168 bits.
In questo modo non era necessario andare a modificare per 


