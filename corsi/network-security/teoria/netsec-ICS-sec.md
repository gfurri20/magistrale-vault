# Cyber-Physical Systems

>[!info] CPS
>Un sistema si dice cyber-fisico se un sistema fisico ed ingegneristico è monitorato, controllato ed integrato attraverso processi informatici.

Un CPS si compone di tre componenti:
- **Sensor Network** -> monitorano i fenomeni fisici derivanti dai processi fisici
- **Communication Network** -> utilizza i dati ricavati dalla Sensor Network per prendere decisione attraverso il sistema informatico
- **Actuator Network** -> implementa le decisioni prese dal sistema informatico sui processi fisici

![[cps.png]]

Un CPS deve possedere determinati standard:
- **Interoperabilità** -> abilità di un sistema di scambiare informazioni tra diversi componenti
- **Prevedibilità** -> garantisce un determinato grado di qualità
- **Affidabilità** -> garantisce un certo grado di correttezza
- **Sostenibilità** -> durabilità nel tempo
- **Dipendenza** -> grado di fiducia relativo a tutto il sistema
- ***Sicurezza*** -> integrità e confidenzialità

Possibili attaccanti di un CPS, ognuno con intenzioni diverse:
- cyber criminali
- dipendenti incazzati
- attivisti e terroristi
- governi (e.g. stuxnet)

---
# Industrial Control Systems (ICS)
Un ICS è un sistema di automazione che provvede al controllo e al monitoraggio delle funzioni all'interno di un'azienda.
Una rete di ICS compone un CPS.

Un ICS si compone di diversi elementi:
- **HMI** -> interfaccia utente di visualizzazione e controllo
- **Stazioni dei dipendenti** -> supervisione e controllo dei processi
- **ICS servers** -> per diverse utilità
- **Controller** -> interfaccia tra il sistema informatico e i sensori che raccolgono i dati

## Protocolli Industriali
I protocolli di comunicazione utilizzati a livello industriale sono stati creati senza introdurre nessun tipo di sicurezza. Al giorno d'oggi è fondamentale e quindi è stato necessario intervenire su tali protocolli per garantirla.

Alcuni protocolli industriali sono:
- *Modbus
- *DNP3*
- *Fieldbus*

Esistono due tipi di reti:
- **routable** -> utilizzano i protocolli di rete definiti da TCP/IP o ISO/OSI
	- includono anche protocolli non routable trasformati (e.g. DNP3 over TCP)
- **non routable** -> si basano su comunicazioni seriali, su bus o point-to-point e sono tipiche dei sistemi industriali

Una PLC potrebbe essere collegata simultaneamente ai sensori attraverso una rete non routable e ad uno switch attraverso una rete routable. 



