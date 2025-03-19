Diario che descrive la risoluzione della challenge, passo per passo, idea per idea.

## Analisi Statica del sorgente
Ci viene dato sia il binario che il codice sorgente, quindi analizziamo velocemente il codice sorgente per capire subito dove sta la vulnerabilità che probabilmente permette di fare buffer overflow.

Il codice contiene delle funzioni mai chiamate dal `main` che eseguono codice assembly, cattura la mia curiosità la seguente funzione:

```c
void angelo_della_morte() {
    asm("int $0x80");
}
```

Essa invoca un interrupt 80 utile per le chiamate a sistema, inoltre è presente una variabile globale di tipo stringa contenente `/bin/sh`.

Deduco quindi che, attraverso la concatenazione di return sia **necessario invocare una chiamata di sistema** (e.g. `execv`) **per aprire la shell**.

Dov'è la vulnerabilità?

```c
char soldi[4];
read(STDIN_FILENO, soldi, soldi);
```

Qua il programma legge da `stdin` ed inserisce nel buffer `soldi` un numero di caratteri grande tanto quanto lo stesso contenuto di `soldi`, permettendoci quindi di scrivere tutto quello ce vogliamo nello stack.

## Esecuzione del binario


