# Ingegneria dei requisiti

> [!info] Requisito
> Descrizione del servizio che il SW dovrà fornire all'utente

Esistono due tipi di requisiti:
- **User** -> cosa deve fare il sistema per supportare l'utente (esprimono una necessità intrinseca del business), tipicamente espressi in linguaggio naturale + qualche schemino
- **System** -> per gli addetti ai lavori, sono descritti in un doc. più strutturato e sono, a livello di dettaglio, più concreti

Spesso ad un user requirement corrispondono molteplici system requirements.

> [!info] Stakeholder
> Coloro che sono affetti, qualsiasi modo, dal sistema software. Dal medico che usa il SW fino al paziente che è semplicemente inserito.

***Requisito funzionale*** -> descrivono le funzionalità dei servizi che il sistema mette a disposizione
- reazione a diversi input
- funzionamento rispetto a svariate eventualità
- possiedono ==diversi livelli di astrazione==
- alcuni potrebbero essere ==ambigui== e quindi interpretati in maniera diversa
- Obiettivi:
	- devono essere *completi* -> ogni punto di appartenenza deve essere definito completamente
	- devono essere *consistenti* -> lo stesso concetto non deve essere sviluppato in maniera diversa
- In pratica:
	- i diversi stakeholders potrebbero avere necessità diverse
	- le inconsistenze non sono facili da trovare e serve un'analisi mirata

***Requisito non-funzionale*** -> esprimono caratteristiche del sistema rispetto a dei limiti/vincoli impostati da standard, contesto o necessità
- sono requisiti ma non sono funzionalità
- sono molto importanti perché ==vincolano il tipo di architettura== che dovremmo utilizzare
- un requisito non-funzionale ==può generare svariati requisiti funzionali==
- spesso si utilizzano delle tassonomie gerarchiche per individuare tutti i req. non funzionali (vedi slides)
