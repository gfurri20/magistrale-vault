*Laboratorio in cui analizziamo dei malware assegnati nel 2022 per l'esame.*

# 1. Analisi Dinamica e di Rete
Analisi dinamica del malware
	`VirusShare_ffeea3fd4f30f807ada1c4e89d270724`

**analisi dinamica:**
1. Avvio di Regshot
2. Avvio di ProcMon
3. 1° snapshot con regshot
4. avvio scansione con procmon (lente)
5. avvio del malware (spacchettato) per qualche minuto
6. stop scansione procmon
7. 2° snapshot regshot e compare

Analizziamo il file di regshot:
- Ci sono chiavi sotto Windows/CurrentVersion/Run che servono per ottenere la persistenza
- Il malware ha modificato anche il registro CurrentUser, aggiungendo le stesse chiavi, con lo stesso nome ed eseguibili.

Passiamo all'analisi con processMonitor.
Aggiungiamo dei filtri:
- *ProcessName* is `VirusShare_...`
- *Operation* is:
	- `WriteFile`
	- `RegSetValue`
	- `SetDispositionInformationFile`
	- `ProcessCreate`

Vediamo che il malware, oltre a impostare i registri già visti su RegShot, va a modificare:
- `Start Page` di `InternetExplorer` impostandola su `blank`
- `ProxyBypass`
- aggiunge un file html, `d5.log`, `dialer.dat`, `ppc.dat`

*(Per l'analisi di rete bisognava impostare le due VM in modo da catturare il traffico, non l'ho fatto)*
Vediamo la cattura del traffico di rete (file `pcapng`)
- filtro: `dns`
	da qui vediamo gli url contattati, alcuni legittimi altri no
- filtro: `http.request`
	vediamo lo scaricamento del file `d5.php` da siti diversi (quelli risolti precedentemente tramite dns)
	

---
# 2. Reverse Engineering di una funzione
function: `sub_4029FC` dello stesso virus

**IDA**
La funzione va a aprire le chiavi di registro sotto 
```
... \\CurrentVersion\\Run
``` 
sotto "Local machine"

Se il malware non ha privilegi elevati deve creare la chiave sotto *current user*
Altrimenti va ad aggiungere la chiave Microsoft Internet Acceleration Utility con il codice `iae.exe`

Lo ripete per tutte le chiavi viste

Va anche a modificare la chiave `StartPage` a `about:blank`

---
# 3. Analisi di un file pdf
filename: `d1c2cc0ca653df[...]1ea924e8ebdb7af0699a7ab909fd.pdf`

>[!info] Suggerimento
>Usare il cheatsheet presente su Moodle!

Elenco dei comandi usati:

`exiftool <pdfFile>`
non ci dice molto

`yara -w -s -m <index.yar> <pdfFile>`
non ci dice molto, vediamo solo `Big_Numbers1`

`pdfid.py <pdfFile>`
contiene file embedded e del codice Javascript

`pdf-parser.py --search openaction <pdfFile>`
L'oggetto che cerchiamo è il 7

`pdf-parser.py -o 7 <pdfFile>` 
non ci fa vedere l'ogetto

`pdf-parser.py --search js <pdfFile>` ci dice che il codice js è nell'oggetto 1 (filter: FlateDecode)

`pdf-parser.py --object 1 -f -w <pdfFile>`
ci dovrebbe dare l'oggetto decodificato. Vediamo che esporta un oggetto con un nome particolare, lo salva in locale e lo esegue. 
Cerchiamo questo oggetto.

`pdf-parser.py --search embeddedfile <pdfFile>`
vediamo che si trova nell'oggetto 37

`pdf-parser.py --object 37 -f -w -d obj37 <pdfFile>`
ci estrae l'oggetto nel file `obj37`

`file obj37` 
ci dice che è un file cifrato (e protetto da password)

`msoffcrypto-crack.py obj37`
vediamo che la pwd è `VelvetSweatshop`. Questa password fa sì che i documenti vengano decifrati in automatico quando aperti

`msoffcrypto-tool obj37 decrypt -p VelvetSweatshop`
ci genera un file chiamato `decrypted`

`file decrypted`
ci dice che è un file Excel 2007

`oledump.py decrypted`
vediamo che il file contiene un oggetto binario. Ci sono due cartelle, supponiamo che il file sia in quella più grande (A2)

`oledump.py -s A2 -d decrypted > excel.bin`
questo estrae il file binario

Possiamo ipotizzare che tale binario possa essere dello *shell-code*.

`xorsearch -W excel.bin`
è in grado di trovare l'original entry point dello shell-code `0x24D`

`scdbgc /f excel.bin /foff 24D`
simula l'esecuzione dello shell-code a partire dall'entry point
Possiamo vedere le Windows API usate dallo shellcode:
- `LoadLibraryW`
- `GetProcAddress`
- `ExpandEnvironmentStringsW`
C'è un URL da cui scaricare un file e una cartella in cui tale file viene salvato.
