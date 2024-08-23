# Tassonomia della Privacy di Solove
La tassonomia della privacy di Daniel Solove è un framework teorico che classifica le diverse minacce alla privacy, rendendole più comprensibili e sistematiche. Solove suddivide le violazioni della privacy in quattro categorie principali.
- ***Information Collection*** -> raccolta delle informazioni dell'individuo
	- **Surveillance** -> raccolta di informazioni individuali attraverso l'osservazione, l'ascolto e la registrazione delle attività umane
	- **Interrogation** -> raccolta di informazioni attraverso questionari o domande
- ***Information Processing*** -> gestione delle informazioni
	- **Aggregation** -> combinazione di informazioni relative ad una singola persona
	- **Identification** -> assegnazione delle informazioni ad una persona
	- **Insecurity** -> negligenza nella conservazione delle informazioni personali
	- **Secondary use** -> uso alternativo, senza consenso, delle informazioni raccolte
	- **Exclusion** -> esclusione di un utente alla gestione delle proprie informazioni
- ***Information Dissemination*** -> distribuzione delle informazioni
	- **Breach of Confidentiality** -> rottura della confidenzialità a discapito della fiducia tra soggetti
	- **Disclosure** -> pubblicazione di informazioni sensibili relative a determinati individui (**Exposure** -> informazioni intime personali)
	- **Increased Accessibility** -> aumento dell'accessibilità delle informazioni
	- **Blackmail** -> ricatti attraverso info personali
	- **Appropriation** -> impersonificazione di persone attraverso informazioni intercettate
	- **Distortion** -> condivisione di false informazioni
- ***Invasion***
	- **Intrusion** -> invasione della vita privata di una persona
	- **Decisional Interference** -> intrusione governativa nelle decisioni private di una persona

Questa classificazione è il tentativo di rendere meno vago il concetto di privacy e di ampliare la letteratura relativa.

---

# Privacy Enhancing Technologies (PETS)

>[!info] PETS
>Strumenti, meccanismi ed architetture che tentano di mitigare il problemi relativi alla privacy

Essendo un insieme di strumenti trovano applicazione sia lato utente che lato organizzazione, mettendo a disposizione una vasta gamma di possibilità.

Si individuano diverse tecnologie, atte alla protezione della privacy:
- **Data Protection** -> progettazioni di sistemi che minimizzano il numero di informazioni personali raccolte e sfruttate; inoltre aiutano a mantenere la compliance con le regolamentazioni (e.g. rende difficile la possibilità di infrangere le regolamentazioni)
	- sistemi di cifratura
	- autenticazione ed autorizzazione degli utenti (e.g. sistemi AC)
	- mantenimento di log ed audit
	- eliminazione sicura di dati ed informazioni per cui è stata richiesta la cancellazione
- **User Awareness** -> permettono all'utente di avere il totale controllo sulle informazioni e sulle circostanze attraverso le quali esse vengono condivise ed utilizzate
	- privacy by design
	- controlli della privacy facili ed intuitivi
	- privacy policy chiare e coincise
- **Anonymity** -> tecnologie di anonimizzazione
	- DB anonymization: k-anonymity, l-diversity, t-closeness
	- communications: onion networks, mixnets
	- credentials: Idemix

---

# Data Anonymization

>[!info] Data Anonymization
>Processo di sanitizzazione delle informazioni con lo scopo di aumentare la privacy utente, all'interno di una specifica struttura dati.

Gli attributi che caratterizzano le informazioni personali di un individuo si dividono in diverse categorie:
- **Explicit identifiers** -> identifica specificamente un utente (e.g. username, IP address)
- **Quasi-identifiers** -> attributo anagrafico o informativo di un individuo (e.g. data di nascita, CAP)
- **Sensitive attributes** -> informazioni personali private sensibili (e.g. malattie, stipendio, segreti in generale)

L'obiettivo è quello di andare a sanificare queste informazioni in modo da renderle non collegabili ai soggetti effettivi.

>[!info] Classe di equivalenza
>Si dice classe di equivalenza un insieme di individui aventi la stessa tupla di quasi-identificatori (anche anonimizzati)
## k-anonymity
Si dice che la versione anonimizzata di un DB possiede la proprietà di **k-anonymity** se le informazioni, per ogni persona contenutevi, non possono essere distinte da almeno altri $k-1$ soggetti le cui informazioni compaiono nel rilascio di dati stesso.

Questa tecnica venne ideata nel 1998 e tentava di risolvere il seguente problema: _"Forniti dei dati strutturati sul campo, produrre un rilascio dei dati con garanzie scientifiche che le persone che sono i soggetti ai quali i dati si riferiscono non possano essere identificate nuovamente mentre i dati rimangono di utilità pratica"_.

Esempio di $\textit{2-anonymity}$ per la tupla di **quasi-identificatori**: $\texttt{(eta', sesso, domicilio)}$:

| Nome      | Età | Genere  | Domicilio  | Religione | Malattia         |
| --------- | --- | ------- | ---------- | --------- | ---------------- |
| Ramsha    | 30  | Femmina | Tamil Nadu | Induista  | Cancro           |
| Yadu      | 24  | Femmina | Kerala     | Induista  | Infezione virale |
| Salima    | 28  | Femmina | Tamil Nadu | Musulmano | TBC              |
| Sunny     | 27  | Maschio | Karnataka  | Parsi     | non malato       |
| Joan      | 24  | Femmina | Kerala     | Cristiano | Cardiopatia      |
| Bahuksana | 23  | Maschio | Karnataka  | Buddista  | TBC              |
| Rambha    | 19  | Maschio | Kerala     | Induista  | Cancro           |
| Kishor    | 29  | Maschio | Karnataka  | Induista  | Cardiopatia      |
| Johnson   | 17  | Maschio | Kerala     | Cristiano | Cardiopatia      |
| John      | 19  | Maschio | Kerala     | Cristiano | Infezione virale |

La tabella in forma anonima si può trasformare in:

| Nome | Età                                         | Genere                                     | Domicilio                                   | Religione | Malattia         |
| ---- | ------------------------------------------- | ------------------------------------------ | ------------------------------------------- | --------- | ---------------- |
| *    | <span style="color:green">20-30</span>      | <span style="color:green">Femmina</span>   | <span style="color:green">Tamil Nadu</span> | *         | Cancro           |
| *    | <span style="color:blue">20-30</span>       | <span style="color:blue">Femmina</span>    | <span style="color:blue">Kerala</span>      | *         | Infezione virale |
| *    | <span style="color:green">20-30</span>      | <span style="color:green">Femmina</span>   | <span style="color:green">Tamil Nadu</span> | *         | TBC              |
| *    | <span style="color:red">20-30</span>        | <span style="color:red">Maschio</span>     | <span style="color:red">Karnataka</span>    | *         | nessuna          |
| *    | <span style="color:blue">20-30</span>       | <span style="color:blue">Femmina</span>    | <span style="color:blue">Kerala</span>      | *         | Cardiopatia      |
| *    | <span style="color:red">20-30</span>        | <span style="color:red">Maschio</span>     | <span style="color:red">Karnataka</span>    | *         | TBC              |
| *    | <span style="color:magenta">età ≤ 20</span> | <span style="color:magenta">Maschio</span> | <span style="color:magenta">Kerala</span>   | *         | Cancro           |
| *    | <span style="color:red">20-30</span>        | <span style="color:red">Maschio</span>     | <span style="color:red">Karnataka</span>    | *         | Cardiopatia      |
| *    | <span style="color:magenta">età ≤ 20</span> | <span style="color:magenta">Maschio</span> | <span style="color:magenta">Kerala</span>   | *         | Cardiopatia      |
| *    | <span style="color:magenta">età ≤ 20</span> | <span style="color:magenta">Maschio</span> | <span style="color:magenta">Kerala</span>   | *         | Infezione virale |

Le tecniche utilizzate per implementare $\textit{k-anonymity}$ sono:
- **Generalizzazione** -> sostituzione dei quasi-identificatori attraverso intervalli o ampliando la categoria
	- $\texttt{eta' 29}$ --> $\texttt{eta' 20-30}$
- **Soppressione** -> eliminazione totale o parziale di informazioni per aumentare il grado di anonimizzazione
	- $\texttt{CAP 24542}$ -> $\texttt{CAP 24***}$
	- $\texttt{CAP 24542}$ -> $\texttt{CAP *****}$

Ovviamente il grado di anonimato e l'utilità delle informazioni potrebbero crescere in maniera inversamente proporzionale tra loro; diventa necessario fare un ==trade-off tra privacy ed utilità==, nel rispetto delle regolamentazioni.

Attacchi contro database k-anonimizzati, essi derivano dal fatto che non vengono protetti i dati se info mancanti sono presenti altrove oppure se l'attaccante ha a disposizione il background.
- **Homogeneity Attack** -> sfrutta il caso in cui tutti i valori per un valore sensibile all'interno di un set di k record sono identici. In tali casi, anche se i dati sono stati k-anonimizzati, è possibile prevedere esattamente il valore sensibile per l'insieme di k record
- **Background Attack** -> sfrutta un'associazione tra uno o più attributi di quasi-identificatore con l'attributo sensibile per ridurre l'insieme dei possibili valori per l'attributo sensibile


## l-diversity
Il modello $l$-diversity è un'estensione del modello k-anonymity.

Il **problema principale della k-anonymity** è che non importa quanto alto sia il valore rappresentato da k, se i dati non sono distribuiti uniformemente allora **rimane possibile identificate gli individui**.

Esempio: data una tabella a cui è stata applicata k-anonymity con $k = 3$.

| Age                                   | ZIP                                    | Disease |
| ------------------------------------- | -------------------------------------- | ------- |
| <span style="color:green">2*</span>   | <span style="color:green">476**</span> | Cancer  |
| <span style="color:green">2*</span>   | <span style="color:green">476**</span> | Cancer  |
| <span style="color:green">2*</span>   | <span style="color:green">476**</span> | Cancer  |
| <span style="color:blue">40-50</span> | <span style="color:blue">4790*</span>  | Cancer  |
| <span style="color:blue">40-50</span> | <span style="color:blue">4790*</span>  | Flu     |
| <span style="color:blue">40-50</span> | <span style="color:blue">4790*</span>  | Flu     |
Se un eventuale attaccante conosce alcuni dati su Bob (background attack) come $\texttt{(age = 22, ZIP = 47655)}$, allora intuisce facilmente che Bob ha il cancro.

> Ogni classe di equivalenza deve avere almeno $l$ *valori sensibili differenti*.

Nell'esempio la classe di equivalenza in blu possiede 2-diversity.

==La distribuzione delle informazioni sensibili per ogni classe di equivalenza deve essere il più simile possibile all'intero DB.==

Distinguiamo due definizioni di *valori sensibili ben rappresentati*:
- **Distinct l-diversity** -> devono esistere almeno $l$ valori sensibili distinti per ogni classe di equivalenza
- **Entropy l-diversity** -> oltre ad avere un numero adeguato di valori sensibili distinti, diventa necessario distribuire in maniera il più uniforme possibile i valori stessi, si definisce il concetto di *entropia*, ovvero il numero minimo di valori sensibili per ogni classe come il logaritmo di $l$: $log(l)$.

Il **problema** principale **della l-diversity** è che **ignora la semantica**, nel senso che rimane comunque possibile associare ad un individuo (attraverso un background attack) una serie di caratteristiche.

Nella successiva tabella, avendo a disposizione i quasi-identificatori di Bob, non sappiamo quale malattia abbia Bob di preciso, ma è sicuro che Bob abbia qualche tipo di problema di salute; inoltre è possibile intuire che Bob percepisce un salario di "bassa categoria".

| Age                                   | ZIP                                    | Salary | Disease       |
| ------------------------------------- | -------------------------------------- | ------ | ------------- |
| <span style="color:green">2*</span>   | <span style="color:green">476**</span> | 3K     | Cancer        |
| <span style="color:green">2*</span>   | <span style="color:green">476**</span> | 5K     | Heart Disease |
| <span style="color:green">2*</span>   | <span style="color:green">476**</span> | 2K     | Flu           |
| <span style="color:blue">40-50</span> | <span style="color:blue">4790*</span>  | 22K    | Cancer        |
| <span style="color:blue">40-50</span> | <span style="color:blue">4790*</span>  | 19K    | Flu           |
| <span style="color:blue">40-50</span> | <span style="color:blue">4790*</span>  | 23K    | Flu           |

## t-closeness
Il modello t-closeness estende il modello $l$-diversity con l'obiettivo di migliorare il procedimento di anonimizzazione di un database.

Per cercare di uniformare le distribuzioni relative alle informazioni sensibili si utilizza una metrica detta **Earth Mover's Distance**. Tale metrica ==permette di calcolare il lavoro che si compie per trasformare una distribuzione in un'altra.==

Calcolare tale metrica su dati numerici ordinati è facile, dati i seguenti salari:
$$\texttt{ D = \{3K, 4K, 5K, 6K, 7K, 8K, 9K, 10K, 11K\} }$$
e le seguenti classi di equivalenza:
- $\texttt{P1 = \{3K, 4K, 5K\}}$
- $\texttt{P2 = \{6K, 8K, 11K\}}$

Diventa necessario calcolare quale delle due distribuzione si avvicina maggiormente alla distribuzione originale $\texttt{D}$.
Per farlo si utilizza una formula specifica, tralasciando i calcoli si ottiene che $\texttt{P2}$ ha un coefficiente pari a $0.167$ mentre $\texttt{P1}$ pari a $0.375$.
In conclusione $\texttt{P2}$ ha una distribuzione più simile a quella originale.

Calcolare la metrica su elementi non numerici diventa più complicato perché è necessario introdurre una gerarchia ad albero degli elementi.

La distanza tra le distribuzioni si ottiene andando a mettere in relazione la distanza tra la prima categoria in comune che contiene entrambi gli elementi esaminati.

==Quindi il valore _t_ che definisce la t-closeness non è altro che il valore che va a rappresentare la distanza tra le varie distribuzioni.==

---

# Differential Privacy
I tre approcci visti sopra hanno i loro problemi, ciò ci conduce ad affermare che la semplice anonimizzazione non basta.

Una prima contromisura può essere quella di permettere solo queries di aggregazione, evitando di fatto interrogazione che potrebbero ledere la privacy degli individui.
Il problema sta nell'inserimento di un nuovo record, il quale potrebbe essere identificabile calcolando le differenze tra i risultati delle interrogazioni di aggregazione, tale tipo di attacco è detto **Reconstruction attack**.

Per evitare la sopra-specificata problematica si può ricorrere al concetto di **Differential Privacy**: essa permette di quantificare il tasso di rischio associato alla privacy rispetto alle pubblicazioni che presentano dati elaborati per preservare la privacy.

Si cerca, quindi, di introdurre del rumore (in gergo noise) all'interno delle distribuzione per viziare i risultati delle aggregazioni, per fare ciò si utilizza una laplaciana.

Esistono due luoghi di applicazione del rumore:
- **Local Differential Privacy** -> il rumore viene applicato localmente al dispositivo utente, successivamente i dati "sporchi" verranno inviati al db. Questo garantisce un rumore maggiore.
- **Global/Centralized Differential Privacy** -> il rumore viene applicato direttamente al database


