
Scaletta per report:
1. Cos'è un attacco ROP, rif. al paper di Campion
	- origine e storia
	- parentesi su attacchi return-to-libc
	- funzionamento
2. Esempi pratici, quindi i due esercizi dati spiegati nel dettaglio
	- analisi preliminare (checksec, disass, ghidra, codice sorgente)
	- tool usati per l'analisi dinamica dell'eseguibile
	- tool per la ricerca di gadgets (ropper)
	- fasi dell'attacco
3. Contromisure applicabili per arginare tali tipologie di attacchi
	- Addresses randomizations (non proprio sicura se si trova l'offset)
	- vedi kBouncer e ROPecker
4. Attacchi che hanno sfruttato effettivamente la tecnica ROP
	- [New Wekby Attacks Use DNS Requests As Command and Control Mechanism](https://unit42.paloaltonetworks.com/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
	- [Evasive Maneuvers by the Wekby Group with Custom ROP-packing and DNS Covert Channels](https://www.anomali.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop)
	- [PowerLoader Injection – Something truly amazing](https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html)
5. ROP in contesti moderni
	- [Gadgets of Gadgets in Industrial Control Systems: Return Oriented Programming Attacks on PLCs | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/document/10132957)

Paper letti e magari citati:
- [The geometry of innocent flesh on the bone | Proceedings of the 14th ACM conference on Computer and communications security](https://dl.acm.org/doi/10.1145/1315245.1315313)
- [Overview of an industrial control system environment contributes to... | Download Scientific Diagram](https://www.researchgate.net/figure/Overview-of-an-industrial-control-system-environment-contributes-to-this-direction-and_fig1_370224876)


---

Estratto dal seguente video: [ROP is DEAD! Kernel Driver Binary Exploitation](https://www.youtube.com/watch?v=mALEQkLegaE)

ROP è un metodo d'attacco di file binari usato per bypassare moderne tecniche di sicurezza, come Data Execution Prevention (DEP: is a security feature that prohibits the application from executing code from non-executable memory area) o NX, ovvero la non eseguibilità dello stack.

A causa di NX non sarebbe possibile sfruttare un buffer overflow per iniettare una shell ed eseguirla, quindi attacchi di questo tipo non funzionerebbero (vedi $W \oplus X$ nel primo paper).

Possiamo però concatenare diversi pezzettini di codice (preesistente nel binario) per eseguire ciò che ci pare attraverso il craft di una ropchain.


---

Source - [[1008.4099] Security Mitigations for Return-Oriented Programming Attacks](https://ar5iv.labs.arxiv.org/html/1008.4099)

>Address Space Layout Randomization (ASLR) as a countermeasure. ASLR renders the layout of an application’s address space less predictable because it relocates the base addresses of executable modules and other memory mappings.

>In order to prevent from effectively using such cases in the ROP attack we propose that every instruction with RET opcode inside of its body will be obfuscated in a special manner. Of course control transfer instructions or any other instructions that use immediate data offsets are an exception to this rule since the immediate displacements are calculated by the linker.





