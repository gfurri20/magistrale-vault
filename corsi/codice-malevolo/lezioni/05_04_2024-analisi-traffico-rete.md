Oggi facciamo filosqualo.

Filtro creato per non dimenticare:
`http.request or ssl.handshake.type == 1`

Per pigliare il server name tls:
TLS > Handshake Protocol > Extension: Server Name > Server Name

## 1. Analisi dei pacchetti HTTP
Filtro: `http.request or http.response`

Si vede che viene scaricato un file `.dll`, presumibilmente per infettare la macchina.

## 2. Analisi del restante traffico
Di solito in un attacco DDoS si cerca di sbrodolare un sacco di pacchetti di \[SYN\] verso un host, usiamo il seguente filtro per cercare informazioni:
`tcp.analysis.flags`

Altri protocolli interessanti sono:
- FTP (la richiesta di STOR salva i file)
	- il filtro `ftp-data` evidenzia file multimediali trasmessi
- SAMBA

## Cambiare impostazioni di rete
Su REMnux:
1. `sudo nano /etc/netplan/01-netcfg.yaml`
2. impostare il dhcp a `no`
3. inserire `addresses: [10.0.0.1/24]`
4. `sudo netplan apply`
5. modificare il file `/etc/inetsim/inetsim.conf`
6. scommentare `start_service`
7. scommentare `start_service dns`
8. scommentare `service_bind_address` e aggiungere `0.0.0.0`
9. scommentare `dns_default_ip` e mettere `10.0.0.1`
10. `sudo systemctl disable systemd-resolved`
11. `sudo systemctl mask systemd-resolved`
12. `sudo systemctl stop systemd-resolved`
13. `sudo inetsim` per simulare i servizi di rete

Su la WinVM:
1. modificare gli IP nella configurazione dell'interfaccia di rete