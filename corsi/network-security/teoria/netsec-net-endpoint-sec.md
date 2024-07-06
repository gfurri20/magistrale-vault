Esistono diverse tecniche per aggiungere sicurezza direttamente sugli end-host.
# Firewalls
**Un firewall permette di proteggere i flussi di traffico in entrata e in uscita** rispetto ad una rete, attraverso delle regole dette policies:
- definisce un collo di bottiglia che filtra il traffico con l'obiettivo di proteggere la rete da ogni possibile minaccia
- permette di monitorare eventi di sicurezza
- aggiunge sicurezza a quei servizi che non la implementano per natura (e.g. NAT)

Limiti di un firewall:
- inutile in caso di attacchi che lo bypassano
- inutile in caso di attacchi originati all'interno della rete

Esistono diverse tecniche attraverso le quali un firewall controlla il traffico:
- **Service Control** -> controllo sul tipo di servizio interrogato
- **Direction Control** -> controllo sulla direzione del flusso rispetto al servizio richiesto
- **User Control** -> controllo sul flusso generato da un determinato utente
- **Behavior Control** -> controllo su determinati comportamenti dei flussi (e.g. spam control)

Esistono quattro principali tipologie di firewall:
- **Packet Filtering**
- **Stateful Inspection**
- **Application Proxy**
- **Circuit-level Proxy**

## Packet Filtering Firewall
Un firewall di tipo Packet Filtering applica un insieme di regole ad ogni pacchetto IP in entrata e in uscita, in base al risultato della regola decide se inoltrare il pacchetto oppure se scartarlo.
Le regole controllano determinati parametri degli header IP o TCP, come l'indirizzo IP, il protocollo di livello trasporto, il numero della porta, eccetera.

Ogni insieme di regole è caratterizzato da una **regola di default**:
- `Discard` -> whitelist (ciò che non è espresso è scartato)
- `Forward` -> blacklist (ciò che è espresso è scartato)

| Action    | in-host | in-port | out-host | out-port | comment                        |
| --------- | ------- | ------- | -------- | -------- | ------------------------------ |
| `allow`   | `*`     | `*`     | `*`      | `25`     | Permette ogni connessione SMTP |
| `discard` | `*`     | `*`     | `*`      | `*`      | Default `discard`              |
e.g. questa policy permette solo connessioni (in/out) SMTP, tutto il resto è scartato.

Vantaggi:
- è una tecnica molto semplice da implementare
- rimane trasparente all'utente
- molto veloce

Svantaggi:
- 




---

# Intrusion Detection Systems (IDS)






---

# Malware