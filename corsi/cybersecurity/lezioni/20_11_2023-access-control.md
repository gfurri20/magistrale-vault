Il controllo degli accessi è un elemento fondamentale per quanto riguarda la sicurezza informatica.
Esso permette di prevenire l'uso non autorizzato delle risorsa da parte di utenti malintezionati.

Attraverso l'**autenticazione** e l'**autorizzazione**, i criteri del controllo d'accesso assicurano che gli utenti siano effettivamente chi dicono di essere e che abbiano l'accesso appropriato solo alle informazioni di cui necessitano.

Coinvolge gli utenti e i gruppi di utenti all'interno di un sistema informatico.

Nello specifico, i principi su cui si basa il controllo degli accessi sono tre:
- **Autenticazione** (Authentication), processo di verifica di un'identità rivendicata da un entità o per un'entità del sistema.
- **Autorizzazione** (Authorization), processo di verifica dei diritti e dei permessi che un'entità posside nei confronti di una risorsa di un sistema.
- **Rendicontabilità** (Accountability), processo di registrazione degli accessi che un'entità svolge rispetto ad una risorsa del sistema.

Ogni **sistema di controllo degli accessi** deve essere in grado di mettere in pratica, in modo efficiente, tali principi.

Ogni sistema di controllo degli accessi si compone di tre elementi che lo caratterizzano:
- **Access Control Policies**, definiscono le regole per il controllo degli accessi
- **Access Control Models**, formalizzano le regole descritte dalla Access Control Policy adottata
- **Access Control Mechanisms**, implementano l'Access Control Model nel sistema informatico

# Access Control Policies (abbr. ACP)
Le ACP definiscono le regole, ad alto livello, per il controllo degli accessi, nello specifico stabiliscono gli individui in grado di modificare gli accessi consentiti.

Gli elementi che compongono una ACP sono tre:
- *soggetto*, l'entità che può accedere all'*oggetto* (e.g. utente o processo)
- *oggetto*, l'elemento/risorsa su cui è applicato un controllo degli accessi (e.g. file, directories, website)
- *permesso*, la modalità attraverso la quale il *soggetto* accede all'*oggetto*

# Access Control Models (abbr. ACMod)
I modelli di controllo degli accessi sono tecniche che regolano chi o cosa può visualizzare o utilizzare risorse in un ambiente informatico.
Sostanzialmente implementano le regole imposte dalle ACP; ogni tipo di ACMod lo fa, però, in modo diverso; ognuno con i propri pro e contro.

Esistono diverse implementazioni per gli ACMod che si differenziano in base agli accessi:
- **Discretionary Access Control (DAC)**, accesso basato sull'identità del *soggetto*
- **Mandatory Access Control (MAC)**, accesso basato sulle proprietà di sicurezza dell'*oggetto* e sulle autorizzazione del *soggetto*
- **Role-Based Access Control (RBAC)**, accesso basato sul ruolo del *soggetto*
- **Attribute-Based Access Control (ABAC)**, accesso basato sugli attributi del *soggetto*, dell'*oggetto* e anche del contesto

## Discretionary Access Control (DAC)
Nel modello DAC gli accessi sono basati dull'identità del *soggetto*; in cui l'accesso a un sistema o a una risorsa è determinato dai proprietari o dagli amministratori del sistema, dei dati o del set di risorse.
Il DAC si dice "discretionary", ovvero discrezionario, perché gli utenti, ==a loro discrezione== appunto, hanno la capacità di assegnare privilegi ad altri utenti.
La concessione e la revoca, comunque, vengono gestite da una policy amministrativa.

Per salvare i permessi quando si usa DAC si possono sfruttare modi diversi.

Di solito si utilizza una, cosiddetta, **access matrix**; ovvero una matrice le cui righe corrispondono ai *soggetti* e le cui colonne corrispondono agli *oggetti*:

|  | news.doc | fun.com | photo.png |
| :--: | :--: | :--: | :--: |
| alice | r | rw | r |
| bob | rw | rw | rw |
| charlie |  |  |  |
| dave |  | r |  |

Altrimenti, è possibile utilizzare le liste, quest'ultime possono essere organizzate o in base all'*oggetto* (**access control list**) oppure in base al *soggetto* (**capability list**).

Le **access control lists** organizzano i permessi in base agli *oggetti*, quindi per ogni *oggetto* nel sistema esiste una lista:

|  | news.doc |
| :--: | :--: |
| alice | r |
| bob | rw |

|  | fun.com |
| :--: | :--: |
| alice | rw |
| bob | rw |
| dave | r |

|  | photo.png |
| :--: | :--: |
| alice | r |
| bob | rw |

Le **capability lists** organizzano i permessi al contrario, quindi in base ai *soggetti*. Per ogni *soggetto* nel sistema esiste una lista:

|  | news.doc | fun.com | photo.png |
| :--: | :--: | :--: | :--: |
| alice | r | rw | r |

|  | news.doc | fun.com | photo.png |
| :--: | :--: | :--: | :--: |
| bob | rw | rw | rw |

|  | news.doc | fun.com | photo.png |
| :--: | :--: | :--: | :--: |
| charlie |  |  |  |

|  | news.doc | fun.com | photo.png |
| :--: | :--: | :--: | :--: |
| dave |  | r |  |

I vantaggi di un approccio DAC sono (ref. [access-control](https://www.techtarget.com/searchsecurity/definition/access-control)):
1. **Fluidità**: il DAC consente una grande flessibilità perché i proprietari possono decidere chi ha accesso alle risorse in base alle loro esigenze personali o di gruppo.
2. **Personalizzazione**: i proprietari possono personalizzare i livelli di accesso per ciascun utente, consentendo così un controllo più granulare.

Gli svantaggi di un approccio DAC sono:
1. **Mancanza di controllo centralizzato**: non esiste un controllo centralizzato. Ciò significa che se un utente abusa dei suoi privilegi, può essere difficile per l'amministratore del sistema intervenire.
2. **Difficoltà di gestione**: la gestione dei diritti di accesso può diventare difficile a causa della sua natura decentralizzata. Man mano che il numero di utenti aumenta, la gestione dei diritti di accesso diventa sempre più complessa.
Anche gli approcci a lista hanno degli svantaggi:
- le access control list fanno fatica a mostrare un riepilogo dei permessi di uno specifico *soggetto*
- le capability list, al contrario, fanno fatica a mostrare un riepilogo dei permessi di uno specifico *oggetto*

---

## Mandatory Access Control (MAC)
Questo è un modello di sicurezza in cui i diritti di accesso sono regolamentati da un'**autorità centrale** basata su diversi livelli di sicurezza. Viene spesso utilizzato in ambienti governativi e militari.
Il MAC concede o nega l'accesso agli oggetti di risorsa in base alla classificazione di sicurezza dell'informazione dell'utente o dispositivo (e.g. top-secret, classified, unclassified, eccetera).

Vantaggi del MAC:
1. **Sicurezza**: fornisce un alto livello di sicurezza poiché l'accesso alle risorse è rigorosamente controllato da un'autorità centrale. Questo rende molto difficile per un utente non autorizzato accedere a risorse sensibili
2. **Consistenza**: poiché le decisioni di accesso sono prese da un'unica autorità centrale, ci sono meno possibilità di conflitti o inconsistenze nelle decisioni di accesso.

Svantaggi del MAC:
1. **Complessità**: può essere complesso da implementare e gestire, soprattutto in ambienti con un gran numero di utenti e risorse. L'assegnazione di classificazioni di sicurezza ai sistemi e alle risorse può richiedere molto tempo e sforzo.
2. **Overhead**: può creare un overhead significativo a causa della necessità di monitorare continuamente le attività degli utenti e applicare le decisioni di accesso. Questo può avere un impatto sulle prestazioni del sistema.

In sintesi, mentre il MAC offre un alto livello di sicurezza e consistenza, presenta la sfida di gestire efficacemente le decisioni di accesso in ambienti complessi.

---

## Role-Based Access Control (RBAC)
Questo è un meccanismo di controllo degli accessi ampiamente utilizzato che si basa su una struttura complessa di assegnazioni di ruolo, autorizzazioni di ruolo e permessi di ruolo per regolare l'accesso dei dipendenti ai sistemi.
Un **ruolo** non è altro che ==un insieme di permessi== relativi alle risorse.

Ci sono diverse famiglie di modelli RBAC:
- $RBAC_0$ - ogni utente ha un ruolo e ogni ruolo ha un set di permessi. Non esistono relazioni tra i ruoli o tra gli utenti. Questo modello è ==molto semplice da implementare==, ma può diventare complicato da gestire se l'organizzazione cresce e i ruoli diventano più complessi.
- $RBAC_1$ - estende $RBAC_0$ aggiungendo la gerarchia dei ruoli: oltre ai ruoli, esistono anche relazioni tra gli utenti e i ruoli. Quindi, un utente può avere più ruoli e un ruolo può essere assegnato a più utenti. Questo modello ==è più flessibile== di $RBAC_0$, ma può diventare più complesso da gestire.
- $RBAC_2$ - estende $RBAC_1$ aggiungendo i vincoli: oltre alle relazioni tra gli utenti e i ruoli, vengono introdotti dei vincoli sugli incarichi. Questo modello offre la ==massima flessibilità==, ma è anche il più complesso da implementare e gestire. La separazione degli incarichi può avvenire in due modi: statica e dinamina. Nella separazione statica un utente non può essere assegnato a più di un ruolo appartenenti allo stesso insieme (e.g. dato l'insieme {studente, professore} un utente non può essere entrambi). Nella separazione dinamica, invece, un utente non può avere più di un ruolo appartente allo stesso set nella stessa sessione.

Vantaggi del RBAC:
1. **Flessibilità**: offre un alto grado di flessibilità poiché gli utenti possono essere assegnati a uno o più ruoli in base alle loro esigenze. Qualsiasi modifica nella struttura aziendale o nelle autorizzazioni può essere rapidamente comunicata a tutti gli utenti, rendendo ==facile l'aggiornamento dei ruoli== corrispondenti.
2. **Efficienza**: riducendo la quantità di lavoro e l'incidenza di errori, l'RBAC aumenta l'efficienza del sistema informatico e degli altri dipendenti. Non sono più necessarie modifiche manuali, gestione degli errori, tempi di attesa o richieste di autorizzazioni individuali.
3. **Sicurezza**: i diritti di accesso sono definiti esclusivamente in base al ruolo, impedendo in questo modo che ai singoli dipendenti siano conferite autorizzazioni eccessive. Questo corrisponde al cosiddetto principio PoLP, ossia Principle of Least Privilege.
4. **Trasparenza**: Il nome dei ruoli è solitamente semplice da capire, rafforzando la trasparenza e la comprensibilità per gli utenti.

Svantaggi del RBAC:
1. **Configurazione impegnativa**: la fase di conversione delle strutture aziendali nel modello RBAC è particolarmente impegnativa.
2. **Numero elevato di ruoli**: per le aziende più grandi, l'RBAC può portare a un numero elevato di ruoli, il che può rendere la ==gestione complessa==.

---
## Attribute-Based Access Control (ABAC)
Questa è una metodologia che gestisce i diritti di accesso valutando un insieme di regole, politiche e relazioni utilizzando gli attributi degli utenti, dei sistemi e del contesto ambientale.

Vantaggi dell'ABAC:
1. **Flessibilità**: offre un alto grado di flessibilità poiché le decisioni di accesso possono essere basate su una serie di attributi, inclusi quelli dell'utente, del sistema e dell'ambiente. Questo permette di creare ==regole di accesso molto dettagliate e personalizzate==.
2. **Scalabilità**: è molto scalabile e si adatta facilmente all'innovazione. Non è necessario che un amministratore aggiorni le policy esistenti per consentire l'accesso a nuove risorse. Questo significa che l'ABAC ==può facilmente adattarsi a cambiamenti nell'organizzazione o nel sistema==.

**Svantaggi dell'ABAC**:
1. **Complessità**: può essere complesso da implementare e gestire, soprattutto in ambienti con un gran numero di utenti e risorse. La gestione di una serie di attributi può richiedere molto tempo e sforzo.
2. **Rischio di errore umano**: come per qualsiasi altro modello di controllo degli accessi, l'errore umano rappresenta un rischio con l'ABAC. Se gli attributi non vengono gestiti correttamente, possono portare a decisioni di accesso non corrette.

In sintesi, mentre l'ABAC offre un alto grado di flessibilità e scalabilità, presenta la sfida di gestire efficacemente una serie di attributi in ambienti complessi.

---
# XACML (eXtensible Access Control Markup Language)
Lo XACML è uno standard pubblicato da OASIS (ente per la standardizzazione in ambito informatico), che fornisce un linguaggio, basato su XML, in grado di:
- scrivere le policy, ovvero le regole
- scrivere le richieste e le risposte
- definire tipi, funzioni e algoritmi
- definire profili basati su ABAC
==Quindi XACML è lo standard per la specifica di modelli ABAC.==

XACML definisce due entità:
- *soggetto*, ovvero colui che intende accedere alle risorse (e.g. utente, processo, website, etc.)
- *risorse*, ovvero gli elementi a cui il soggetto intende accedere (e.g. file, database, etc.)

XACML, inoltre, si predispone di un'architettura precisa, composta da diversi elementi logici:
- **PEP** (Policy Enforcement Point), protegge una risorsa ed inoltre controlla gli accessi sulla base della verifica delle policy
- **PDP** (Policy Decision Point), riceve le varie richieste di accesso e, in base alle policy, decide se autorizzarle o meno
- **PIP** (Policy Information Point), fornisce le informazioni rispetto agli attributi e quindi rispetto alle autorizzazioni
- **PAP** (Policy Administrator Point), crea e immagazina le policy di sicurezza
Queste entità si interfacciano ad un **context handler** che ha il compito di tradurre le policy dalla loro forma nativa in XACML e viceversa.

Il flusso di autorizzazione funziona in questo modo:
1. il PAP crea le policy e le mette  a disposizione del PDP
2. la richiesta viene passata al PEP
3. il PEP inoltra la richiesta al context handler, aggiungendo in caso attributi aggiuntivi
4. il context handler normalizza in XACML la richiesta e la manda al PDP
5. il PDP richiede eventuali info su soggetto, azione, risorsa al context handler
	6. il context handler invia la richiesta di info al PIP
	7. il PIP ottiene gli attibuti richiesti
	8. il PIP ritorna gli attributi richiesti al context handler
	9. opzionalemente il PIP aggiunge la risorsa
	10. il context handler invia gli attributi richiesti al PDP
11. il PDP esegue la decisione, la allega al response context ed invia quest'ultimo al context handler
12. il context handler traduce la risposta da XACML al linguaggio nativo di PEP e gliela invia
13. il PEP adempie gli obblighi
14. se l'accesso è consentito viene resa disponibile la risorsa, altrimenti no

## Componenti di XACML
XACML è basato su XML, quindi i suoi componenti seguono la sintassi dei linguaggi di markup.

L'elemento principale è il `<PolicySet>`, ovvero un insieme di `<Policy>`. Ogni polici è costituita da:
- `<Target>`, associa una risorsa richiesta ad una policy
- `<Rule>`, condizioni di test degli attributi rispetto alle policy
- `<Obligation>`, operazioni da eseguire a seguito di autorizzazione

L'elemento `<Policy>` è il più piccolo elemento che può essere elaborato dal PDP.

Le `<Rule>` vengono combinate tra di loro per specializzare le decisioni di autorizzazioni.
Esistono diversi algoritmi di combinazione:
- **deny-overrides**, *Deny* ha priorità su *Permit*
	- se tutte le decisioni sono *Indeterminate* -> *Indeterminate*
	- se tutte le decisioni sono *Permit* -> *Permit*
	- altrimenti -> *NotApplicable*
- **permit-overrides**, *Permit* ha priorità su *Deny*
	- se tutte le decisioni sono *Indeterminate* -> *Indeterminate*
	- se tutte le decisioni sono *Deny* -> Deny
	- altrimenti -> *NotApplicable*
- **first-applicable**, l'effetto risultato è quello della prima policy che ha `<Target>` a true
- **only-one-applicabile**, si applica solo all'elemento `<PolicySet>`
	- se nessuna policy si può applicare -> *NotApplicable*
	- se più di una policy è applicabile -> *Indeterminate*
	- se c'è solo una policy applicabile -> si applica la decisione estratta da tale policy

Come specificato sopra XACML permette di rappresentare richieste e risposte.

La `<Request>` incapsula la richiesta di decisione che deve essere inoltrata al PDP:
- `<Attributes>`, info aggiuntive di soggetto, risorsa, azione e ambiente
- `<Category>`, specifica se gli attributi sono associati al soggetto
	- l'elemento `<Attribute>` descrive l'attributo
- `<Content>`, la risorsa incapsulata

La `<Response>` incapsula la decisione di autorizzazione prodotta dal PDP>
- `<Decision>`, il risultato della valutazione della `<Request>`
- `<Obligation>`, obblighi che devono essere soddisfatti dal PEP