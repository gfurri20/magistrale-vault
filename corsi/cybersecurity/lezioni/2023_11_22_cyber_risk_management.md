Al giorno d'oggi la maggior parte delle aziende dipendono dalla tecnologia informatica, per quanto utile esse possono essere vettori di attacchi informatici e quindi predisporre dei rischi.

Diventa, quindi, necessario decidere quanto tempo e quanti soldi spendere per mettere in sicurezza le proprie tecnologie e i propri servizi.

Esistono requisiti specifici, descritti in apposite regolamentazioni, che esplicitano tutta una serie di tecniche per implementare un'efficiente **gestione dei rischi cibernetici** (e.g. ISO 31000, NIST 800-37, etc).

Sintetizzando, il cyber risk management è un processo che identifica, prioritizza, gestisce e monitora i **rischi** per i sistemi informatici.

> [!info]
>Un **rischio informatico** è qualsiasi tipo di azione, tecnologia, software o hardware con la capacità di minacciare il proprio sistema informatico.

Le procedure di Cyber Risk Management si dividono, generalemente, in diverse fasi:
1. **Frame Risk** - analisi iniziale per inquadrare il contesto dell'azienda
2. **Assess Risk** - identificazione dei potenziali rischi e valutazione degli stessi
3. **Respond to Risk** - valutazione della tecnica di gestione adatta
4. **Communicate the Risk** - condivisione delle valutazioni eseguite alle parti interessate
5. **Implement and Assure the Risk** - implementazione dei controlli di sicurezza
6. **Monitor the Risk** - monitoraggio e revisione dei sistemi di sicurezza adottatti

È importante notare che queste fasi non sono lineari e spesso si sovrappongono.

## #1 - Frame Risk
La prima fase consiste nell'attuare un analisi del contesto e dell'ambiente dell'azienda. In particolare vengono individuate le aree critiche di lavoro, ovvero quelle parti che potrebbero essere maggiormente soggette a rischi.

Inoltre vengono analizzati tutti i requisiti a cui l'azienda deve sottostare per imposizione delle diverse regolamentazioni.
Vengono anche definiti quei rischi accettabili.

## #2 - Assess Risk
Il Risk Assessment è una parte fondamentale del processo di Risk Management e consiste nell'==individuare tutti i possibili rischi e tutte le possibili vulnerabilità== a cui il sistema informatico di un'azienda potrebbe essere soggetto.

In aggiunta viene valutata la probabilità che un dato rischio (in gergo *likelihood*) si realizzi e l'impatto che avrebbe se si verificasse. Questo passaggio aiuta a determinare quali rischi devono essere affrontati per primi.

## #3 - Respond to Risk
Una volta valutati e priorizzati i rischi, il successivo passo è sviluppare un piano per mitigare quei rischi.

Ci sono diversi approcci possibili:
- accettare il rischio
- evitare il rischio
- trasferire il rischio
- trattare il rischio

Inoltre è necessario anche individuare quali sistemi di sicurezza possono essere utili:
- *procedural security* - controlli di sicurezza che mirano a mitigare i rischi attraverso l'applicazione di regolamenti e standards
- *phisical security* - controlli di sicurezza che mirano a mitigare i rischi fisici, tentando di proteggere strutture, laboratori ma anche personale
- *personnel security* - controlli di sicurezza che mirano a mitigare i rischi derivanti dal personale dell'azienda, come dipendenti scontenti, dipendenti ignari usati come vettori, email di phishing, social eng, etc.
- *technical security* - controlli di sicurezza che mirano a mitigare i rischi tecnologici/informatici (e.g. firewalls, antivirus, etc.)

## #4 - Communicate the Risk
Questa fase consiste nel comunicare a tutte le parti dell'azienda i rischi scoperti, i requisiti da implementare e tutto ciò che è stato deciso per prevenire il rischio.
Ovviamente la comunicazione di tali informazioni deve essere adattata al tipo di gruppo aziendale a cui le si comunicano.

## #5 - Implement and Assure the Risk
In questa fase sono comprese tutte le operazioni pratiche atte alla prevenzione del rischi:
- vengono installati e mantenuti i sistemi di sicurezza individuati
- vengono formati i gestori dei sistemi di sicurezza e i dipendenti
- i nuovi prodotti vengono creati con un'ottica orientata alla sicurezza
- esecuzione di test di sicurezza in base all'utilizzo dei diversi dispositivi

## #6 - Monitor Risk
Infine, dopo l'implementazione dei controlli di sicurezza, è importante monitorare continuamente gli ambienti per rilevare qualsiasi comportamento anomalo o attività sospetta. Inoltre, le procedure di gestione dei rischi della sicurezza informatica dovrebbero essere riviste e aggiornate regolarmente per riflettere i cambiamenti nelle minacce, nei sistemi e nelle politiche aziendali.

---

# Risk Assessment
Il Risk Assessment è la fase iniziale e fondamentale della gestione dei rischi. Fornisce una comprensione dei rischi esistenti e della loro potenziale gravità, che può, quindi, essere utilizzata per sviluppare e implementare strategie di gestione dei rischi. La gestione dei rischi, d'altra parte, è un processo continuo che utilizza le informazioni raccolte durante la valutazione dei rischi per identificare, analizzare e rispondere ai rischi in modo efficace.

Informalmente:

$$RiskAssessment\space\in\space RiskManagement$$
Anche per quanto rigaurda il Risk Assessment esitono diversi framework che organizzano le varie fasi (e.g. NIST 800-30).

Il Risk Assessment di compone di quattro parti, secondo il gloassario del [NIST](https://csrc.nist.gov/glossary/term/risk_assessment):
- **assessment risk process**, quindi di identificazione dei rischi per le operazioni organizzative, per i beni organizzativi, per gli individui, per altre organizzazioni e per la Nazione, derivanti dal funzionamento di un sistema informativo
- **risk model**, ovvero i possibili fattori di rischio pratici (e.g. malware)
- **assessment approach**, ovvero l'approccio utilizzato per valutare il rischio e i suoi fattori di rischio che contribuiscono, anche ==in modo quantitativo, qualitativo== o semiquantitativo
- **analysis approach**, ovvero l'approccio utilizzato per definire l'orientamento o il punto di partenza della valutazione del rischio, il livello di dettaglio nella valutazione e il modo in cui vengono trattati i rischi dovuti a scenari di minaccia simili

Il **risk model** nello specifico ha il compito di individuare svariati attributi dei rischi:
- *assets*, gli obiettivi o le risorse fisiche che possono essere prede
- *vulnerabilities*, ovvero tutti quei bug o errori involontari che potrebbero essere sfruttati per eseguire attacchi cibernetici
- *threat actors*, ovvero i papabili attaccanti o gruppi di attaccanti che potrebbero essere interessati a sfruttare le vulnerabilità esistenti sul sistema
- *threats*, le evenutali minacce che possono essere giunte al sistema informatico
- *likelihood*, le probabilità che una minaccia/vulnerabilità venga sfruttata oppure che l'attacco avvenga correttamente
- *impact*, le conseguenze che un attacco ben riuscito provoca sul sistema informatico

*Likelihood* e *Impact* sono due aspetti fondamentali che devono poter essere stimati per implementare le corrette misure di sicurezza, per fare ciò si segue una metodologia creata da OWASP: **OWASP Risk Rating Methodology**.

---

# OWASP Risk Rating Methodology
> L'Open Web Application Security Project (OWASP) è un progetto online che produce articoli, metodologie, documentazione, strumenti e tecnologie gratuite e accessibili nel campo della sicurezza delle applicazioni web. È guidato da una fondazione senza scopo di lucro chiamata The OWASP Foundation.

Questa metodologia fornisce diversi fattori per stimare la probabilità che venga sfruttato un rischio (*likelihood*) e l'impatto che potrebbe avere (*impact*).

La *likelihood* è stimata attraverso due fattori:
- threat agent factors - fattori relativi alle minacce
- vulnerability factors - fattori relativi alle vulnerabilità

Anche l'*impact* è misurato attracerso due fattori:
- fattori tecnici
- fattori di business

I livelli rischio sono misurati assegnado un valore, compreso tra 0 e 9, dove 0 è il livello più basso e 9 il livello più alto:

| Livelli numerici | Classe di rischio |
| :--: | :--: |
| $[0, 3)$ | <span style="color:#00b050">LOW</span> |
| $[3, 6)$ | <span style="color:#ffc000">MEDIUM</span> |
| $[6, 9]$ | <span style="color:#ff0000">HIGH</span> |
Il rischio totale viene calcolato mettendo insieme *likelihood* ed *impact*.

## Likelihood - Threat agent factors
Questi fattori sono correlati agli attaccanti coinvolti e mirano a stimare la probabilità di un attacco di successo da parte dei cosiddetti threat actors.

Essi includono:
- **Skill Level** - livello di abilità tecniche possedute dal gruppo di attaccanti. <small>Può variare da "No technical skills (1)" a "Security penetration skills (9)"</small>
- **Motive** - livello di motivazione del gruppo per trovare e sfruttare la vulnerabilità. <small>Può variare da "Low or no reward (1)" a "High reward (9)"</small>
- **Opportunity** - quantità e qualità delle risorse e delle opportunità a disposizione degli attaccanti per trovare e sfruttare le vulnerabilità. <small>Può variare da "Full access or expensive resources required (0)" a "No access or resources required (9)"</small>
- **Size** - grandezza del gruppo di attaccanti. <small>Può variare da "Developers (2)" a "Anonymous Internet users (9)"</small>

## Likelihood - Vulnerability factors
Questi fattori sono correlati alla vulnerabilità stessa e mirano a stimare la probabilità che la vulnerabilità venga scoperta ed esplicitata.

Essi includono:
- **Ease of Discover** - facilità con la quale un gruppo di attaccanti può ==scoprire== la vulnerabilità. <small>Può variare da "Practically impossible (1)", "Difficult (3)", "Easy (7)", "Automated tools available (9)"</small>
- **Ease of Exploit** - facilità con la quale un gruppo di attaccanti può ==sfruttare== la vulnerabilità. <small>Può variare da "Theoretical (1)", "Difficult (3)", "Easy (5)", "Automated tools available (9)". Può variare da "Theoretical (1)", "Difficult (3)", "Easy (5)", "Automated tools available (9)"</small>
- **Awareness** - livello di conoscenza della vulnerabilità da parte del gruppo di attaccanti. <small>Può variare da "Unknown (1)", "Hidden (4)", "Obvious (6)", "Public knowledge (9)"</small>
- **Intrusion Detection** - probabilità che un tentativo di sfruttamento venga rilevato. <small>Può variare da "Active detection in application (1)", "Logged and reviewed (3)", "Logged without review (8)", "Not logged (9)"</small>

## Impact - Technical factors
Questi fattori sono correlati all'impatto tecnico della vulnerabilità se fosse sfruttata e mirano a stimare la magnitudo dell'impatto sul sistema.
Come si nota facilmente essi si rifanno a [[i-sei-pilastri]] della sicurezza informatica.

Essi includono:
- **Loss of Confidentiality** - quantità ed importanza dei dati che potrebbero essere trafugati. <small>Può variare da "Minimal non-sensitive data disclosed (2)", "Minimal critical data disclosed (6)", "Extensive non-sensitive data disclosed (6)", "Extensive critical data disclosed (7)", "All data disclosed (9)"</small>
- **Loss of Integrity** - quantità di dati che possono essere danneggiati o eliminati. <small>Può variare da "Minimal slightly corrupt data (1)", "Minimal seriously corrupt data (3)", "Extensive slightly corrupt data (5)", "Extensive seriously corrupt data (7)", "All data totally corrupt (9)".</small>
- **Loss of Availability** - quantità ed importanza dei servizi che potrebbero essere persi. <small>Può variare da "Minimal secondary services interrupted (1)", "Minimal primary services interrupted (5)", "Extensive secondary services interrupted (5)", "Extensive primary services interrupted (7)", "All services completely lost (9)"</small>
- **Loss of Accountability** - livello di tracciabilità delle azioni compiute nel sistema dagli attaccanti. <small>Può variare da "Fully traceable (1)", "Possibly traceable (7)", "Completely anonymous (9)"</small>

## Impact - Business Impact factors
Questi fattori sono correlati all'impatto finanziario e operativo dell'azienda se una particolare vulnerabilità venisse sfruttata.

Essi includono:
- **Financial Damage** - impatto finanziario che lo sfruttamento di una vulnetabilità potrebbe comportare. <small>Può variare da "Minimal financial impact (2)", "Significant financial impact (6)", "Maximum financial impact (9)"</small>
- **Reputation Damage** - impatto alla reputazione dell'azienda che lo sfruttamento di una vulnerabilità potrebbe comportare. <small>Può variare da "Minimal reputation impact (2)", "Significant reputation impact (6)", "Maximum reputation impact (9)"</small>
- **Non-compliance** - impatto legale e di conformità alle regolamentazioni che una vulnerabilità potrebbe avere sull'azienda. <small>Può variare da "Minimal legal and compliance impact (2)", "Significant legal and compliance impact (6)", "Maximum legal and compliance impact (9)"</small>
- **Privacy Violation** - quantità di persone di cui verrebbe violata la privacy nel caso in cui venisse sfruttata una vulnerabilità. <small>Può variare da "One
individual (3)", "hundreds of people (5)", "thousands of people (7)", "millions of people (9)"</small>

---

# Risk Assessment - NIST 800-30
La valutazione del rischio secondo il framework NIST 800-30 è un processo strutturato che guida l'identificazione, la valutazione e la prioritizzazione dei rischi per le operazioni dell'organizzazione, i suoi asset, le persone, altre organizzazioni e la nazione, risultanti dall'operazione e dall'uso dei sistemi informativi organizzativi.

Il processo di valutazione del rischio NIST 800-30 è composto da quattro fasi principali:
1. **Prepare for Assessment** - l'obiettivo di questa fase consiste nell'individuare il contesto della valutazione dei rischi, identificando:
	- scopo dell'assessment
	- assunzioni e vincoli
	- **risk model**, **assessment approach** e **analysis approach** per essere usati durante la valutazione
2. **Conduct Risk Assessment** - identificazione delle fonti di minacce, degli eventi di minaccia, delle vulnerabilità e delle condizioni predisponenti, identificando e catalogando:
	- le sorgenti delle minacce (e.g. il gruppo di attaccanti)
	- i threat event, ovvero quelle situazioni che potrebbero potenzialemente portare sgradevoli conseguenze
	- le vulnerabilità che i threat event possono sfruttare e il loro possibile livello di impatto
	- le probabilità che un threat event si verifichi
	- l'impatto che si potrebbe verificare ai danni dell'azienda
	- il rischio totale di un eventuale attacco sfruttando uno specifico threat event
3. **Communicate Results** - comunicazione dei risultati della valutazione del rischio agli stakeholder pertinenti. Questo può includere la preparazione di un rapporto dettagliato sulla valutazione del rischio
4. **Maintain the Risk Assessment** - monitoraggio continuo dei rischi e l'aggiornamento della valutazione del rischio in base ai risultati del monitoraggio. Questo processo continuo permette di mantenere la valutazione del rischio aggiornata e pertinente