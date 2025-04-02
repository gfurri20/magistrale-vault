
Scaletta per report:
1. Cos'è un attacco ROP, rif. al paper di Campion
	- cronistoria della scoperta
		- 1996 - attacchi stack smashing
		- 1997 - return-to-libc by SolarDesign
		- 2000 - protezioni $W \oplus X$
		- 2007 - ROP
2. Esempi pratici, quindi i due esercizi dati spiegati nel dettaglio
	- analisi preliminare (checksec, disass, ghidra, codice sorgente)
	- tool usati per l'analisi dinamica dell'eseguibile
	- tool per la ricerca di gadgets (ropper)
	- fasi dell'attacco
	- script per l'exploit con pwntools
3. Attacchi che hanno sfruttato effettivamente la tecnica ROP (in questi casi come tecnica di offuscamento del flusso d'esecuzione)
	- PowerLoader
	- HTTPBrowser
4. Contromisure applicabili per arginare tali tipologie di attacchi
	- Addresses randomizations (eventuale bypass relativo tramite calcolo dell'offset)
	- Zipper Stack e ROPocop (accenno sul funzionamento)
5. ROP nel contesto ICS (per avere una visione attuale su ROP)

Bibliografia:
- [stack_smashing.pdf](https://inst.eecs.berkeley.edu/~cs161/fa08/papers/stack_smashing.pdf)
- [The geometry of innocent flesh on the bone | Proceedings of the 14th ACM conference on Computer and communications security](https://dl.acm.org/doi/10.1145/1315245.1315313)
- [Overview of an industrial control system environment contributes to... | Download Scientific Diagram](https://www.researchgate.net/figure/Overview-of-an-industrial-control-system-environment-contributes-to-this-direction-and_fig1_370224876)

Sitografia:
- [Bugtraq: Getting around non-executable stack (and fix)](https://seclists.org/bugtraq/1997/Aug/63)
- [New Wekby Attacks Use DNS Requests As Command and Control Mechanism](https://unit42.paloaltonetworks.com/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Evasive Maneuvers by the Wekby Group with Custom ROP-packing and DNS Covert Channels](https://www.anomali.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop)
- [PowerLoader Injection – Something truly amazing](https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html)
- [Matrix - Enterprise | MITRE ATT&CK®](https://attack.mitre.org/matrices/enterprise/)


---

Estratto dal seguente video: [ROP is DEAD! Kernel Driver Binary Exploitation](https://www.youtube.com/watch?v=mALEQkLegaE)

ROP è un metodo d'attacco di file binari usato per bypassare moderne tecniche di sicurezza, come Data Execution Prevention (DEP: is a security feature that prohibits the application from executing code from non-executable memory area) o NX, ovvero la non eseguibilità dello stack.

A causa di NX non sarebbe possibile sfruttare un buffer overflow per iniettare una shell ed eseguirla, quindi attacchi di questo tipo non funzionerebbero (vedi $W \oplus X$ nel primo paper).

Possiamo però concatenare diversi pezzettini di codice (preesistente nel binario) per eseguire ciò che ci pare attraverso il craft di una ropchain.


---

Source - [[1008.4099] Security Mitigations for Return-Oriented Programming Attacks](https://ar5iv.labs.arxiv.org/html/1008.4099)

>Address Space Layout Randomization (ASLR) as a countermeasure. ASLR renders the layout of an application’s address space less predictable because it relocates the base addresses of executable modules and other memory mappings.

>In order to prevent from effectively using such cases in the ROP attack we propose that every instruction with RET opcode inside of its body will be obfuscated in a special manner. Of course control transfer instructions or any other instructions that use immediate data offsets are an exception to this rule since the immediate displacements are calculated by the linker.



# Cronistoria
**1996: Pubblicazione di "Smashing The Stack For Fun And Profit" di Aleph One**
Nel novembre del 1996, Elias Levy, noto con lo pseudonimo Aleph One, pubblicò l'articolo "Smashing The Stack For Fun And Profit" nel numero 49 della rivista _Phrack_. Questo articolo fornì una dettagliata spiegazione delle vulnerabilità legate ai buffer overflow nello stack e illustrò come sfruttarle per eseguire codice arbitrario. L'articolo è considerato una pietra miliare nella comprensione e nell'evoluzione degli exploit basati su buffer overflow. ​[inst.eecs.berkeley.edu+3Wikipedia+3ethicsatwork.nd.edu+3](https://en.wikipedia.org/wiki/Elias_Levy?utm_source=chatgpt.com)

**1997: Introduzione degli attacchi "return-to-libc" da parte di Solar Designer**
Nel 1997, lo sviluppatore noto come Solar Designer introdusse la tecnica dell'attacco "return-to-libc". Questa metodologia permetteva agli aggressori di sfruttare le vulnerabilità di buffer overflow per reindirizzare il flusso di esecuzione verso funzioni esistenti nella libreria standard C (libc), come `system()`, evitando così la necessità di iniettare codice nello stack. Questo approccio rappresentò un metodo efficace per aggirare le protezioni che impedivano l'esecuzione di codice nello stack. ​[lettieri.iet.unipi.it+1hovav.net+1](https://lettieri.iet.unipi.it/hacking/code-reuse.pdf?utm_source=chatgpt.com)[Exploit Notes](https://exploit-notes.hdks.org/exploit/binary-exploitation/method/binary-exploitation-with-ret2libc/?utm_source=chatgpt.com)

**Anni 2000: Implementazione delle protezioni W⊕X (Write XOR Execute)**
In risposta agli attacchi basati su buffer overflow, vennero implementate protezioni di memoria come W⊕X, che impediscono alle regioni di memoria di essere sia scrivibili che eseguibili. Queste misure, tra cui la Data Execution Prevention (DEP), miravano a prevenire l'esecuzione di codice iniettato nello stack o nell'heap, aumentando la sicurezza dei sistemi contro exploit basati sull'iniezione di codice. ​

**2007: Presentazione del "Return-Oriented Programming" (ROP) da parte di Hovav Shacham**
Nel 2007, Hovav Shacham presentò il concetto di "Return-Oriented Programming" (ROP) nel suo lavoro intitolato "The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)". Questa tecnica avanzata consentiva agli aggressori di eseguire codice arbitrario combinando brevi sequenze di istruzioni già presenti nel programma, ciascuna terminante con un'istruzione di ritorno, aggirando così le protezioni W⊕X e DEP senza necessità di iniettare nuovo codice. ​[arXiv+3hovav.net+3Black Hat+3](https://hovav.net/ucsd/dist/geometry.pdf?utm_source=chatgpt.com)

Questi sviluppi evidenziano l'evoluzione continua delle tecniche di attacco e delle contromisure nel campo della sicurezza informatica, sottolineando l'importanza di una costante ricerca e aggiornamento per proteggere i sistemi dalle minacce emergenti.

Prova di commit