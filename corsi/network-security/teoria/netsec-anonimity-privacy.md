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
> Lo stato di **non essere identificabile rispetto ad un insieme di soggetti**, in questo caso tra gli utenti di Internet.
> Tale insieme di soggetti è detto **anonymity set**.

Più è grande l'anonymity set più lo stato di anonimato acquisito è robusto.   

Due caratteristiche dell'anonimato sono:
- l'impossibilità di collegare l'identità con l'azione (**unlinkability**)
- l'impossibilità di affermare se una certa azione è avvenuta (**unobservability**)
	- si possono utilizzare degli *pseudonimi* come meccanismo leggero

Esistono diversi tipi di attacchi che potrebbero rompere l'anonimato:
- analisi passiva del traffico
- analisi attiva del traffico tramite l'aggiunta di pacchetti al traffico
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
Esegue le stesse azioni di un proxy (padding + cifratura), aggiungendo meccanismi in grado di mischiare il traffico.

ARRIVATO a pagina 17 della dispensa



## Routing Randomizzato