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