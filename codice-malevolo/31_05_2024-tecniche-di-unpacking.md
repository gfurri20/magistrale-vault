Primo file: `.../Chapter18/Lab18-02.exe`.

Dobbiamo capire il tipo di packing:
1. apriamo con pestudio per capire il tipo di spacchettamento -> `fsg 1.0`, ma non abbiamo lo spacchettatore
Ci sono varie metodologie per trovare l'original entry point in base alle situazione dette nella scorsa lezione a cui io non ho partecipato perché stavo fallendo la cc.
(probabilmente è scritto sulle slide)

Non abbiamo indicazioni tramite IDA, allora usiamo x32dbg...

Possiamo sfruttare la funzione di `tracing` delle varie istruzioni, essa permette di eseguire determinate istruzione e creare un log fino a quando non accade un evento/situazione specificata.

In questo caso eseguiamo fino a quando non arriviamo ad un indirizzo che è fuori dalla sezione in cui stiamo eseguendo.

`Tracing > trace over`

Inseriamo in `Break Condition` il seguente filtro: `mem.base(cip)!=405000`.

Eseguito il comando di tracing, il debugger si ferma su `push ebp` e quindi su una probabile chiamata di funzione.

Si può usare Scylla (plugin) che riconosce immediatamente l'entry point (se abbiamo correttamente fatto il tracing), ed eseguiamo queste operazioni:

`dump` -> `IAT autosearch` -> `GET imports` -> `fix dump` sul file dumpato in precedenza.

---

Ora analizziamo il file `Lab18-03.exe`, in questo caso è impacchettato con `PECompact v1.4`.

Qua il codice è ridotto e si notano subito due istruzioni:
- `pushf` -> pusha il registro delle flag sullo stack
- `pusha` -> pusha gli 8 registri general purpose (16 bit) nello stacckozzo
Probabilmente salva tali info per poi riavercele per l'esecuzione del malware.

Successivamente chiama una funzione, che presumibilmente chiamerà delle pop per recuperare tali info.

==Quindi possiamo cercare delle pop su x32dbg==

Quindi eseguiamo entrambe le push e settiamo un hardware bp sull'indirizzo in memoria puntato dall'esp:
`follow in dump` -> `breakpoint` -> `hw access` -> `dword`

In questo modo quando tale indirizzo sarà acceduto (con una pop probabilmente, ma non per forza), l'esecuzione si fermerà.

Dopo il `run` eseguiamo `step in` e dopo una `ret` arriviamo al main. A questo punto Scylliamo.

---

Lo stesso procedimento visto con il `Lab18-03` lo si può applicare a `Lab18-04`:
- il file è impacchettato con una codifica `AZ`
- con ida si nota che viene fatta una pusha, quindi da qualche parte ci sarà una pop relativa che ripristina i valori nella CPU
- con x32dbg è possibile inserire un hw breakpoints per fermarsi sulla pop che cerchiamo
- scorrendo fino alla prima `ret` ed eseguendola raggiungiamo l'entry point
- a questo punto lo scylliamo
- done

---

`Lab18-05`

Subito con pestudio si capisce il tipo di packaging -> Upack V0.36

In questo caso non vediamo imports quindi il malware dovrà caricare le API in memoria attraverso la `get_proc_address`.

Possiamo usare il comando nella command line `setBPX GetProcAddress`, in questo modo mettiamo un breakpoint sulla prima istruzione all'interno della funzione breakpointata.

Ad ogni esecuzione del comando `run` si nota che in `eax` viene caricata il nome di una funzione che verrà importata.

L'ultima funzione caricata è `InternetOpenA`.

Il main sembra stare all'indirizzo `401190`.




