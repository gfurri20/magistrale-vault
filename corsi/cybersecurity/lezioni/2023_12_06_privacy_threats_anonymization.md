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
- **Explicit identifiers** -> identifica specificamente un utente (e.g. username, CI identifier)
- **Quasi-identifiers** -> attributo anagrafico o informativo di un individuo (e.g. data di nascita, CAP)
- **Sensitive attributes** -> informazioni personali private sensibili (e.g. malattie, stipendio, segreti in generale)

L'obiettivo è quello di andare a sanificare queste informazioni in modo da renderle non collegabili ai soggetti effettivi.

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

| Nome | Età                            | Genere  | Domicilio  | Religione | Malattia         |
| ---- | ------------------------------ | ------- | ---------- | --------- | ---------------- |
| *    | <span style="color:green">20-30</span> | <span style="color:green">Femmina</span> | <span style="color:green">Tamil Nadu</span> | *         | Cancro           |
| *    | <span style="color:blue">20-30</span> | <span style="color:blue">Femmina</span> | <span style="color:blue">Kerala</span>     | *         | Infezione virale |
| *    | <span style="color:green">20-30</span> | <span style="color:green">Femmina</span> | <span style="color:green">Tamil Nadu</span> | *         | TBC              |
| *    | <span style="color:red">20-30</span>  | <span style="color:red">Maschio</span> | <span style="color:red">Karnataka</span>  | *         | nessuna          |
| *    | <span style="color:blue">20-30</span> | <span style="color:blue">Femmina</span> | <span style="color:blue">Kerala</span>     | *         | Cardiopatia      |
| *    | <span style="color:red">20-30</span>  | <span style="color:red">Maschio</span> | <span style="color:red">Karnataka</span>  | *         | TBC              |
| *    | <span style="color:magenta">età ≤ 20</span> | <span style="color:magenta">Maschio</span> | <span style="color:magenta">Kerala</span>     | *         | Cancro           |
| *    | <span style="color:red">20-30</span>  | <span style="color:red">Maschio</span> | <span style="color:red">Karnataka</span>  | *         | Cardiopatia      |
| *    | <span style="color:magenta">età ≤ 20</span> | <span style="color:magenta">Maschio</span> | <span style="color:magenta">Kerala</span>     | *         | Cardiopatia      |
| *    | <span style="color:magenta">età ≤ 20</span> | <span style="color:magenta">Maschio</span> | <span style="color:magenta">Kerala</span>     | *         | Infezione virale |

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
Il modello di $l$-diversity gestisce alcuni dei punti deboli del modello k-anonymity in cui le identità protette al livello di k-individui non equivalgono a proteggere i corrispondenti valori sensibili che sono stati generalizzati o soppressi, specialmente quando i valori sensibili all'interno di un gruppo mostrano omogeneità.
Il modello $l$-diversity aggiunge la promozione della diversità intragruppo per i valori sensibili nel meccanismo di anonimizzazione.

Ogni classe di equivalenza (i.e. tuple di quasi-identificatori equivalenti) deve avere almeno $l$ *valori sensibili ben rappresentati*.

==La distribuzione delle informazioni sensibili per ogni classe di equivalenza deve essere il più simile possibile all'intero DB.==

Distinguiamo due definizioni di *valori sensibili ben rappresentati*:
- **Distinct l-diversity** -> devono esistere almeno $l$ valori sensibili distinti per ogni classe di equivalenza
- **Entropy l-diversity** -> oltre ad avere un numero adeguato di valori sensibili distinti, diventa necessario distribuire in maniera il più uniforme possibile i valori stessi, si definisce il concetto di *entropia*, ovvero il numero minimo di valori sensibili per ogni classe come il logaritmo di $l$: $log(l)$.


## t-closeness
Il modello t-closeness estende il modello $l$-diversity trattando distintamente i valori di un attributo tenendo conto della distribuzione dei valori dei dati per quell'attributo.

Una classe di equivalenza gode di t-closeness se la distanza tra la distribuzione di un attributo sensibile appartenente alla classe e la distribuzione dell'attributo nell'intera tabella è minore o uguale ad una treshold t.
