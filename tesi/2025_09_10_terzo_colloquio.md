- Trovare un altro modo per passare dati alla LLM
	- come passare una time series nello specifico
	- https://arxiv.org/pdf/2402.01801

**Qual è il modo migliore per dargli i dati?**
Dobbiamo creare un framework per scrivere domande chiare e che ritornino una risposta valutabile (e.g. SI o NO)

Domande da implementare:
1) Questa è la scansione ottenuta osservando per un tot (indicare) di tempo il contenuto dei registri di 3 PLC (l’attaccante ha fatto la scansione e sa benissimo quante PLC ha scansionato) di un sistema industriale. Riesci a capire l’ambito di applicazione del sistema industriale (Risposta: sistema di trasporto liquidi)
2) Supponendo che il sistema industriale sia un sistema di filtraggio delle acque che usa sicuramente delle vasche, riesci a capire quante vasche sono coinvolte nel sistema?
3) Riesci ad associare le 3 PLC alle vasche che pensi di aver individuato?
4) In effetti le vasche sono tre. Riesci ad individuare quali registri delle PLC sono dedicati alle misure e quali alle attuazioni, per ciascuna vasca? 
5) In effetti le vasche sono tre. Riesci ad individuare se ci sono registri delle PLC utilizzati per memorizzare altri informazioni significative, come setpoint o altro?
6) Considerato che le vasche sono tre, riesci a dedurre se esiste una connessione fisica, ovvero dei tubi, che colleghino due o più vasche? (questa è una informazione che nel nostro paper non siamo in grado di derivare)
7) Supponendo di aver individuato i registri dedicati a contenere le misure e le attuazioni per ciascuna vasca, riesci a costrure per ciascuna vasca, un grafico che spieghi come queste grandezze, misure e attuazioni, evolvono al passare del tempo?
8) Riesci a costrurmi un grafico che rappresenti il funzionamento dell’intero sistema al passare del tempo?
9) Per ciascuna vasca, riesci ad estrapolare degli invarianti che mettano in relazione le misure con le attuazioni? 
10) Riesci ad estrapolare degli invarianti significativi che leghino il contenuto dei registri dell’intero sistema industriale?

Fare delle domande che però permettano una risposta precisa.

Domanda: qual è il modello migliore? https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
- Qwen  
- Mistral
- Deepseek
- Llama

Alcuni modelli potrebbero permette la risposta schematizzata (e.g. in JSON) 
Framework python di openai.

