<small>ID chlg: CR_1.08</small>

Subito si nota come alla key manchino due caratteri e questo fa subito pensare che bisognerà fare del minimo brute-forcing su di essa, sembra composta solo da caratteri alfanumerici.

Manca l'intero IV e un pezzo del ciphertext.

Definiamo:
- `p1 = "AES with CBC is"`
- `p2 = "very unbreakable"`
- `c1 = "c5??????????????????????????d49e"`
- `c2 = "78c670cb67a9e5773d696dc96b78c4e0"`
- `key = "yn9RB3Lr43xJK2??"`
- `iv = "?????????????????"`

Prima di tutto bisogna trovare la chiave `key`, e questo è possibile farlo osservando che:
$$p2 = Decrypt_{key}(c2) \oplus c1$$
ma allora, grazie alle proprietà dello XOR:
$$c1 = Decrypt_{key}(c2) \oplus p2$$
Per trovare `c1` quindi bisogna eseguire un brute-force su `key` cercando i caratteri rimanenti che permettono di ottenere un risultato caratterizzato da:
- i primi due caratteri in hex sono `"c5"`
- gli ultimi quattro caratteri in hex sono `"d49e"`

Di seguito il codice della funzione in python:
```python
def find_c1(c2, p2):
    alph = string.ascii_letters + string.digits
    baseKEY = "yn9RB3Lr43xJK2"

    # brute force sugli ultimi due caratteri della chiave
    for char1 in alph:
        for char2 in alph:
            KEY = baseKEY + char1 + char2
            res = bytearray()

            # algoritmo di decifratura a blocchi con sola chiave
            aes = AES.new(KEY.encode(), AES.MODE_ECB)
            dec = aes.decrypt(c2)

            # facciamo lo xor tra dec e p2
            res = xor(dec, p2)

            hex_res = ''.join(format(byte, '02x') for byte in res)

            # cerca la corrispondenza con i pezzi che abbiamo
            if hex_res[0:2] == "c5" and hex_res[len(hex_res) - 4:] == "d49e":
                return KEY, res
```

Se si ottiene riscontro allora abbiamo trovato `key` e `c1`.

Infatti:
- `key = "yn9RB3Lr43xJK2tp"`
- `c1 = "c5dc598a00e6e31272bcb2ed502ad49e"`

Infine, per trovare `iv`, basterà seguire la seguente formula:
$$p1 = Decrypt_{key}(c1) \oplus iv \implies iv = Decrypt_{key}(c1) \oplus p1$$
Codice:
```python
def find_IV(p1, c1, KEY):
    aes = AES.new(KEY.encode(), AES.MODE_ECB)
    dec = aes.decrypt(c1)

    iv = xor(p1, dec)

    return iv.decode()
```

In questo modo si ottiene `iv = "P4rt14l_1nf0_b4d"`, che unito alla sintassi della flag ci permette di ottenere: `CCIT{P4rt14l_1nf0_b4d}`.

P.S.: la funzione $Decrypt_{key}(x)$ non è altro che l'applicazione di AES in modalità ECB.