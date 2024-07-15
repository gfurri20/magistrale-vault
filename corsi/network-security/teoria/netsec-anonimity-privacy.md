Internet è, per natura, una rete pubblica, ognuno potrebbe essere in grado di intercettare informazioni.
==Ogni sistema di crittografia non nasconde le identità che stanno comunicando.==

L'anonimato può essere utile in diverse occasioni:
- per proteggere la privacy, magari attraverso un sistema di AC
- per rendere mail non tracciabili
- intelligence ed indagini
- trasferimento di valute elettroniche
- sistemi di voto anonimo
# Anonimato

> [!info] Anonimato
> Lo stato di **non essere identificabile rispetto ad un insieme di soggetti**, in questo caso tra gli utenti di Internet. Tale insieme di soggetti è detto **anonymity set**.

Più è grande l'anonymity set più lo stato di anonimato acquisito è robusto.   

Due caratteristiche dell'anonimato sono:
- l'impossibilità di collegare l'identità con l'azione (**unlinkability**)
- l'impossibilità di affermare se una certa azione è avvenuta (**unobservability**)
	- si possono utilizzare degli *pseudonimi* come meccanismo leggero

Esistono diversi tipi di attacchi che potrebbero rompere l'anonimato:
- analisi passiva del traffico
- analisi attiva del traffico tramite l'aggiunta di pacchetti
- compromissioni di nodi di rete (e.g. routers)
	- diventano indispensabili meccanismi di ridondanza


## Anonymization Proxy
Un primo modo per costruire un canale anonimo è quello di introdurre dei proxies che tentano di anonimizzare il traffico.

Il mittente interagisce con il solito traffico, è il proxy che si occupa dei meccanismi di anonimizzazione.
Il destinatario riceverà, dal proxy, i pacchetti in broadcast. Solamente il destinatario legittimo sarà in grado di capire le informazioni.

Ovviamente questo metodo rende il proxy un punto cruciale del sistema e quindi possibile vittima di attacchi.
Inoltre è sempre possibile eseguire l'analisi del traffico.

### Proxies in cascata
Per aumentare la sicurezza si potrebbe costruire una rete di proxies in cascata, facendo in modo che ogni entità conosca solamente il precedente ed il prossimo hop.

Più livelli si introducono più il sistema sarà lento e pesante.

Inoltre è ancora possibile l'analisi del traffico.


## Reti MIX
Le reti MIX nascono nel 1981 con l'obiettivo di creare un canale che garantisse l'anonimato in un ambiente ostile.
Nasce come un meccanismo per garantire l'anonimato nelle mail (non si può se no lo spam è un casino assurdo).

Grazie a questi meccanismi **un attaccante non è in grado di associare un messaggio ricevuto ad un messaggio inviato**, anche conoscendo gli utenti.

L'elemento principale è il ***MIX server***, che processa ogni oggetto.
Esegue le stesse azioni di un proxy (padding + cifratura), aggiungendo meccanismi in grado di mischiare il traffico, nel ==tentativo di vanificare l'analisi del traffico==.

Azioni compiute dai server mix:
1. agisce su blocchi di **lunghezza costante**, quindi aggiunge padding oppure splitta il messaggio
2. nasconde l'ordine di arrivo, spedendo in output gli elementi in gruppi (i.e. **batches** di output)
3. blocca informazioni ripetute per **prevenire replay attacks**
4. necessita di un **anonymity set di grandi dimensioni**, in caso contrario si potrebbe fare in modo che i client inviino spesso messaggi fasulli
5. possibilità di garantire **non-ripudiabilità inviando delle ricevute** relative ai messaggi, grazie a tale oggetto anche il client può autenticare l'invio

Come per i proxies, un singolo mix server, potrebbe essere un bersaglio interessante, quindi è consigliabile utilizzare diversi mixer all'interno della rete.

### Mixnet
Una rete composta da un insieme di mixer in cascata è detta **mixnet**.

Un pacchetto che attraversa una mixnet, viene cifrato ad ogni mixer, finché non raggiunge la destinazione.
Inoltre, ogni mixer, aggiunge le proprie contromisure per evitare replay attack o l'analisi del traffico.

Ovviamente il grande numero di mixer da attraversare potrebbe rendere il traffico pesante, a causa del numero di cifrature/de-cifrature da effettuare (il numero di chiavi è elevato).

Vantaggi:
- **alto livello di anonimato**
	- non c'è correlazione tra pacchetti in input ed in output ad un mixer
	- accetta mixer malevoli
	- se l'anonymity set è piccolo basta introdurre del traffico falso
- il tracciamento di un messaggio è prevenuto dai messaggi fasulli
- i replay attack sono prevenuti dai filtri appositi

***+ anonimato, - prestazioni*** (alta latenza, costoso computazionalmente)

Si potrebbe cercare di diminuire la latenza stabilendo, attraverso delle chiavi asimmetrica, un canale di comunicazione basato su chiavi simmetriche.


## Routing Randomizzato
Un altro approccio è quello di nascondere i messaggi randomizzando il routing del pacchetto.

I router non sanno se il mittente del pacchetto che ricevono è il vero mittente oppure un altro router.

### Onion Routing
L'**Onion Routing** permette di randomizzare il percorso scegliendo una sequenza di router casualmente.
Questa tecnica ammette anche la presenza di alcuni router malevoli.

Ogni router incapsula le informazioni ricevute con la propria chiave pubblica, ed invia il pacchetto al prossimo hop, unico host di cui è a conoscenza il router.

Un esempio di software che sfrutta l'onion routing è `Tor`.

Tor, per aumentare le prestazioni, instaura un canale simmetrico con ogni router facente parte del percorso.
In questo modo il client possiederà tante chiavi simmetriche quanti sono gli hop del percorso di routing che deve seguire il pacchetto.

Tor ha delle difficoltà:
1. molteplici applicazioni condividono lo stesso percorso
2. un router tor non richiede privilegi di amministratore, è facile per tutti creare il proprio router
3. esistono dei directory servers che gestiscono i router sulla rete

Si cerca di creare un **Location Hidden Server (LHS)**, ovvero un server capace di comunicare sulla rete ma che non si sa dove si trovi fisicamente, o da chi sia gestito:
- accessibile ovunque
- resistente alla censura
- resistente ad attacchi DoS

Ogni LHS è associato a degli **introduction points**, ovvero dei dispositivi che permettono l'accesso al server.
Tali dispositivi hanno un ciclo di vita breve e vengono spesso sostituiti.

Per ottenere l'accesso ad un introduction point è necessario contattare il server di lookup.

1. il client crea un circuito sicuro (a cipolla) fino al punto detto *rendezvous*
2. sempre il client invia ad un *intro point* l'indirizzo del rendezvous e le autorizzazioni necessarie
3. se il server associato all'intro point utilizzato decide di voler parlare con il client si **instaura un circuito sicuro tra rendezvous e server**

