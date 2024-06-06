La Cyber Kill Chain è un concetto che descrive in modo generale le fasi di un attacco informatico, dalla raccolta iniziale di informazioni fino al danno che ne consegue per la vittima.
Descrive il ciclo di vita di un attacco in 7 fasi ed è stata creata per studiare, categorizzare e mitigare gli attacchi.

Queste fasi vanno ad esaminare l'attacco più nel profondo e non si limita a vederlo come un blocco monolitico.
Talune volte le fasi non sono chiare da distinguere perché alcuni passaggi dell'attacco in questione rasentano i limiti di fasi adiacenti.
In ogni caso, fornisce un ottimo schema di lettura e catalogazione delle fasi di un attacco informatico.

## 1. Reconnaissance
Questa fase consiste nella raccolta di informazioni relative all'obiettivo, al target. Ciò può essere fatto in maniera passiva, ovvero non interagendo con il target oppure in maniera attiva, interagendo con il target.
Un esempio di reconnaissance passiva è [Shodan.io](shodan.io) che permette di acquisire informazioni sulle macchine esposte sulla rete; mentre un esempio di reconnaissance attiva è l'uso del comando `nmap`.

## 2. Weaponization
Durante questa fase di inizializzazione l'attaccante acquisisce gli strumenti per eseguire l'attacco.
Ciò può comprendere la creazione di un malware oppure l'uso di software già esistenti che confezionano attacchi basati su vulnerabilità note.
Per esempio metasploite è un framework che permette di creare automaticamente attacchi basandosi su un insieme di vulnerabilità note.

## 3. Deliver
In questa fase l'attaccante distribuisce il malware (o comunque il software dannoso) al target. Tale operazione può avvenire attraverso svariati vettori d'attacco, come per esempio mail di phishing, dispositivi fisici, eccetera.

## 4. Exploitation
La fase di exploitation consiste nello sfruttare una o più vulnerabilità, sul target, attraverso il malware prodotto, con l'obiettivo di ottenere l'accesso non autorizzato al sistema.

## 5. Installation
Durante questa fase l'attaccante cerca di instaurare persistenza all'interno dell'ambiente target. Per fare ciò installa il malware sfruttando le vulnerabilità presenti, l'obiettivo è quello di creare una backdoor.

> **Backdoor** - An undocumented way of gaining access to computer system. A backdoor is a potential security risk. [NIST glossary](https://csrc.nist.gov/glossary/term/backdoor)

## 6. Command & Control (C2)
Questa fase consiste nell'installare un canale di comunicazione tra target ed attaccante. In questo modo l'utente malevolo ha la possibilità di mantenere il controllo del dispositivo vittima anche da remoto, con lo scopo di proseguire l'attacco.

## 7. Actions & Objectives
Corrisponde alla fase finale, fase in cui l'attaccante raggiunge l'obiettivo prefissato che svariare dal furto di dati sensibili fino alla distruzione dell'ambiente target.
In realtà sono molti di più i possibili obiettivi: scovare le credenziali utente, scalare i privilegi, eseguire movimento laterale nell'ambiente del target, criptare i dati e chiedere il riscatto, ...

----
# MITRE Att&ck Matrix
L'istituto MITRE ha catalogato una vastissima lista di attacchi per rendere pubbliche le tecniche e i metodi effettivi utilizzati dagli attaccanti.

Questa lista è chiamata **MITRE Att&ck Matrix** e raggruppa le tecniche di attacco note, **raggruppandole per tattiche**.

Quindi **tecnica $\neq$ tattica**; infatti la tattica comprende svariate tecniche, per esempio la tattica di *Initial Access* include le tecniche di Phishing, Content Injection, eccetera.  

La matrice è divisa in due parti:
- **Pre-Att&ck**: raggruppa le fasi precedenti ad un attacco, quindi quelle fasi che comprendono soprattutto l'acquisizione di informazioni
- **Att&ck**: raggruppa le tecniche utilizzate durante l'effettivo attacco, divise per categorie

In realtà la Pre-Att&ck Matrix, che descriveva le tattiche di *Reconnaissance* e Initial Access, è ormai inclusa nella **Att&ck Matrix**; difatti il MITRE la identifica come deprecata.

## Att&ck Matrix
La MITRE Att&ck Matrix (abbr. AM) divide le tecniche, non solo per piattaforma, ma anche per categoria, è possibile individuare tutte le fasi della Cyber Kill Chain all'interno delle categorie rappresentate dalla AM.

Per ogni tecnica la AM ci fornisce diverse informazioni:
- una descrizione generale della tecnica
- le possibili sotto-tecniche
- esempi di procedure, quindi esempi di attacchi che hanno sfruttato tale tecnica durante la fase di *Initial Access*
- esempi di possibili mitigazioni ripristinare i sistemi dai danni
- esempi di possibili metodi di rilevamento dell'uso della tecnica

Ogni sotto-tecnica estende la tecnica padre, descrivendo una specifica implementazione.

All'interno della AM sono descritti anche svariati gruppi di hacker che hanno agito sul territorio mondiale.
Per ogni gruppo sono indicate le campagne di attacchi svolte e le tecniche che sono state utilizzate per metterle in pratica.

Gli hacker spesso sono motivati dalle seguenti ragioni:
- politica interna o mondiale (e.g. guerre)
- culturale/religiosa
- orgoglio nazionale
- terrorismo
- lucro (e.g. ransomware)

Sempre più spesso questi gruppi di hacker offrono servizi anche alle persone comuni attraverso il concetto di *Attack As A Service*, proprio come un semplice servizio legale.





