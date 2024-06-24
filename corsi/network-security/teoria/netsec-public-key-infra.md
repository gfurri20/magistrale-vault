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
