
La prima funzione alloca 192 bytes e sembra inserirci 23 indirizzi (ind. `0x5555556032a0`).

In realtà ad ogni iterazione (ci sono 23 iterazioni) alloca 16 byte.
$$\frac{192}{16} = 12$$
Ogni indirizzo sembra puntare ad una istruzione assembly (sempre quelle per ogni avvio).

|    Indirizzo     | Istruzione |       Hex        |
| :--------------: | :--------: | :--------------: |
| `0x555555603370` |            | `0x7ffff7fc2000` |
| `0x555555603390` |            | `0x7ffff7fc2011` |
| `0x5555556033b0` |            | `0x7ffff7fc2022` |
| `0x5555556033d0` |            | `0x7ffff7fc2033` |
| `0x5555556033f0` |            | `0x7ffff7fc2044` |
| `0x555555603410` |            | `0x7ffff7fc2055` |
| `0x555555603430` |            | `0x7ffff7fc2066` |
| `0x555555603450` |            | `0x7ffff7fc2077` |
| `0x555555603470` |            | `0x7ffff7fc2088` |
| `0x555555603490` |            | `0x7ffff7fc2099` |
| `0x5555556034b0` |            | `0x7ffff7fc20aa` |
| `0x5555556034d0` |            | `0x7ffff7fc20bb` |
| `0x5555556034f0` |            | `0x7ffff7fc20cc` |
| `0x555555603510` |            | `0x7ffff7fc20dd` |
| `0x555555603530` |            | `0x7ffff7fc20ee` |
| `0x555555603550` |            | `0x7ffff7fc20ff` |
| `0x555555603570` |            | `0x7ffff7fc2110` |
| `0x555555603590` |            | `0x7ffff7fc2121` |
| `0x5555556035b0` |            | `0x7ffff7fc2132` |
| `0x5555556035d0` |            | `0x7ffff7fc2143` |
| `0x5555556035f0` |            | `0x7ffff7fc2154` |
| `0x555555603610` |            | `0x7ffff7fc2165` |
| `0x555555603630` |            | `0x7ffff7fc2176` |

Una volta eseguita la copia del codice in memoria, ognuno di questi indirizzi andrà a puntare ad una sezione di codice.

In questo modo il codice inserito in memoria sarà sezionato in base ai 23 indirizzi sopra riportati.

Dopo vari sbrodolamenti nel codice ho provato a patchare l'eseguibile in modo da eliminare la funzione che utilizza il random.
Grazie alla patch il controllo fatto nel codice che viene caricato in memoria controlla l'input in modo sequenziale rispetto alla flag.

Ad ogni chiamata del codice caricato in memoria l'istruzione `0x7ffff7fc2004`, sotto-riportata, veniva modificata con il successivo carattere.

Quindi basta completare la flag chiamando tante volte il file patchato aggiungendo di volta in volta il carattere corretto.

Flag:
$$\texttt{CCIT\{itz\_m0rph\_34C3!!!\}}$$

e.g.:
```asm
**0x7ffff7fc2000**:      push   rsi
0x7ffff7fc2001:          push   rdx
0x7ffff7fc2002:          mov    al,BYTE PTR [rdi]
0x7ffff7fc2004:          cmp    al,0x43
0x7ffff7fc2006:          jne    0x7ffff7fc22e7
0x7ffff7fc200c:          jmp    0x7ffff7fc22c9
**0x7ffff7fc2011**:      rex.RXB
0x7ffff7fc2012:          rex.XB
0x7ffff7fc2013:          fwait
0x7ffff7fc2014:          (bad)
0x7ffff7fc2015:          sub    eax,0xdb941e52
0x7ffff7fc201a:          adc    edx,DWORD PTR [rcx]
0x7ffff7fc201c:          adc    eax,edi
0x7ffff7fc201e:          mov    dh,0x13
0x7ffff7fc2020:          adc    DWORD PTR [rcx],edx
**0x7ffff7fc2022**:      je     0x7ffff7fc2094
0x7ffff7fc2024:          test   al,0x25
```

Il codice sezionato si ferma a `0x7ffff7fc2176`, prima del muro di `nop`.

Byte copiati in memoria:
```bytes
56 52 8a 07 3c 43 0f 85 db 02 00 00 e9 b8 02 00 00 47 43 9b 16 2d 52 1e 94 db 13 11 11 f8 b6 13 11 11 74 70 a8 25 1e 6b 2d a7 9b 20 22 22 cb b4 20 22 22 65 61 b9 34 0f 67 3c b6 9b 31 33 33 da b6 31 33 33 12 16 ce 43 78 3f 4b c1 d3 46 44 44 ad 30 46 44 44 03 07 df 52 69 3c 5a d0 d3 57 55 55 bc 36 57 55 55 30 34 ec 61 5a 12 69 e3 13 64 66 66 8f 34 64 66 66 21 25 fd 70 4b 0d 78 f2 13 75 77 77 9e 36 75 77 77 de da 02 8f b4 d7 87 0d db 8a 88 88 61 b8 8a 88 88 cf cb 13 9e a5 f4 96 1c db 9b 99 99 70 86 9b 99 99 fc f8 20 ad 96 9a a5 2f 9b a8 aa aa 43 a4 a8 aa aa ed e9 31 bc 87 c9 b4 3e 9b b9 bb bb 52 46 ba bb bb 9a 9e 46 cb f0 bc c3 49 c3 ce cc cc 25 20 cd cc cc 8b 8f 57 da e1 b5 d2 58 23 dc dd dd 34 06 dc dd dd b8 bc 64 e9 d2 b1 e1 6b 03 ef ee ee 07 24 ef ee ee a9 ad 75 f8 c3 cc f0 7a 23 fe ff ff 16 46 fe ff ff 46 42 9a 17 2c 24 1f 95 db 11 10 10 f9 b8 11 10 10 77 73 ab 26 1d 62 2e a4 9b 20 21 21 c8 b6 20 21 21 64 60 b8 35 0e 01 3d b7 9b 33 32 32 db b4 33 32 32 15 11 c9 44 7f 62 4c c6 db 42 43 43 aa 36 42 43 43 02 06 de 53 68 75 5b d1 d3 55 54 54 bd 30 55 54 54 33 37 ef 62 59 44 6a e0 13 64 65 65 8c 36 64 65 65 20 24 fc 71 4a 0b 79 f3 13 77 76 76 9f 34 77 76 76 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 58 5f 41 b8 00 00 00 00 49 83 f8 11 74 1c 8a 1f 88 c1 30 cb 88 1f 49 ff c0 48 ff c7 eb ea b8 3c 00 00 00 bf 01 00 00 00 0f 05 c3 00
```

Se si prova a disassemblare tali bytes si ottiene il seguente codice assembly:
```asm
0:  56                      push   rsi  
1:  52                      push   rdx  
2:  8a 07                   mov    al,BYTE PTR [rdi]  
4:  3c 43                   cmp    al,0x43  
6:  0f 85 db 02 00 00       jne    0x2e7  
c:  e9 b8 02 00 00          jmp    0x2c9  
11: 47                      rex.RXB  
12: 43                      rex.XB  
13: 9b                      fwait  
14: 16                      (bad)  
15: 2d 52 1e 94 db          sub    eax,0xdb941e52  
1a: 13 11                   adc    edx,DWORD PTR [rcx]  
1c: 11 f8                   adc    eax,edi  
1e: b6 13                   mov    dh,0x13  
20: 11 11                   adc    DWORD PTR [rcx],edx  
22: 74 70                   je     0x94  
24: a8 25                   test   al,0x25  
26: 1e                      (bad)  
27: 6b 2d a7 9b 20 22 22    imul   ebp,DWORD PTR [rip+0x22209ba7],0x22        # 0x22209bd5  
2e: cb                      retf  
2f: b4 20                   mov    ah,0x20  
31: 22 22                   and    ah,BYTE PTR [rdx]  
33: 65 61                   gs (bad)  
35: b9 34 0f 67 3c          mov    ecx,0x3c670f34  
3a: b6 9b                   mov    dh,0x9b  
3c: 31 33                   xor    DWORD PTR [rbx],esi  
3e: 33 da                   xor    ebx,edx  
40: b6 31                   mov    dh,0x31  
42: 33 33                   xor    esi,DWORD PTR [rbx]  
44: 12 16                   adc    dl,BYTE PTR [rsi]  
46: ce                      (bad)  
47: 43 78 3f                rex.XB js 0x89  
4a: 4b c1 d3 46             rex.WXB rcl r11,0x46  
4e: 44                      rex.R  
4f: 44 ad                   rex.R lods eax,DWORD PTR ds:[rsi]  
51: 30 46 44                xor    BYTE PTR [rsi+0x44],al  
54: 44 03 07                add    r8d,DWORD PTR [rdi]  
57: df 52 69                fist   WORD PTR [rdx+0x69]  
5a: 3c 5a                   cmp    al,0x5a  
5c: d0 d3                   rcl    bl,1  
5e: 57                      push   rdi  
5f: 55                      push   rbp  
60: 55                      push   rbp  
61: bc 36 57 55 55          mov    esp,0x55555736  
66: 30 34 ec                xor    BYTE PTR [rsp+rbp*8],dh  
69: 61                      (bad)  
6a: 5a                      pop    rdx  
6b: 12 69 e3                adc    ch,BYTE PTR [rcx-0x1d]  
6e: 13 64 66 66             adc    esp,DWORD PTR [rsi+riz*2+0x66]  
72: 8f                      (bad)  
73: 34 64                   xor    al,0x64  
75: 66 66 21 25 fd 70 4b    data16 and WORD PTR [rip+0xd4b70fd],sp        # 0xd4b717a  
7c: 0d  
7d: 78 f2                   js     0x71  
7f: 13 75 77                adc    esi,DWORD PTR [rbp+0x77]  
82: 77 9e                   ja     0x22  
84: 36 75 77                ss jne 0xfe  
87: 77 de                   ja     0x67  
89: da 02                   fiadd  DWORD PTR [rdx]  
8b: 8f                      (bad)  
8c: b4 d7                   mov    ah,0xd7  
8e: 87 0d db 8a 88 88       xchg   DWORD PTR [rip+0xffffffff88888adb],ecx        # 0xffffffff88888b6f  
94: 61                      (bad)  
95: b8 8a 88 88 cf          mov    eax,0xcf88888a  
9a: cb                      retf  
9b: 13 9e a5 f4 96 1c       adc    ebx,DWORD PTR [rsi+0x1c96f4a5]  
a1: db 9b 99 99 70 86       fistp  DWORD PTR [rbx-0x798f6667]  
a7: 9b                      fwait  
a8: 99                      cdq  
a9: 99                      cdq  
aa: fc                      cld  
ab: f8                      clc  
ac: 20 ad 96 9a a5 2f       and    BYTE PTR [rbp+0x2fa59a96],ch  
b2: 9b                      fwait  
b3: a8 aa                   test   al,0xaa  
b5: aa                      stos   BYTE PTR es:[rdi],al  
b6: 43 a4                   rex.XB movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]  
b8: a8 aa                   test   al,0xaa  
ba: aa                      stos   BYTE PTR es:[rdi],al  
bb: ed                      in     eax,dx  
bc: e9 31 bc 87 c9          jmp    0xffffffffc987bcf2  
c1: b4 3e                   mov    ah,0x3e  
c3: 9b                      fwait  
c4: b9 bb bb 52 46          mov    ecx,0x4652bbbb  
c9: ba bb bb 9a 9e          mov    edx,0x9e9abbbb  
ce: 46 cb                   rex.RX retf  
d0: f0 bc c3 49 c3 ce       lock mov esp,0xcec349c3  
d6: cc                      int3  
d7: cc                      int3  
d8: 25 20 cd cc cc          and    eax,0xcccccd20  
dd: 8b 8f 57 da e1 b5       mov    ecx,DWORD PTR [rdi-0x4a1e25a9]  
e3: d2 58 23                rcr    BYTE PTR [rax+0x23],cl  
e6: dc dd                   (bad)  
e8: dd 34 06                fnsave [rsi+rax*1]  
eb: dc dd                   (bad)  
ed: dd b8 bc 64 e9 d2       fnstsw WORD PTR [rax-0x2d169b44]  
f3: b1 e1                   mov    cl,0xe1  
f5: 6b 03 ef                imul   eax,DWORD PTR [rbx],0xffffffef  
f8: ee                      out    dx,al  
f9: ee                      out    dx,al  
fa: 07                      (bad)  
fb: 24 ef                   and    al,0xef  
fd: ee                      out    dx,al  
fe: ee                      out    dx,al  
ff: a9 ad 75 f8 c3          test   eax,0xc3f875ad  
104:    cc                      int3  
105:    f0 7a 23                lock jp 0x12b  
108:    fe                      (bad)  
109:    ff                      (bad)  
10a:    ff 16                   call   QWORD PTR [rsi]  
10c:    46 fe                   rex.RX (bad)  
10e:    ff                      (bad)  
10f:    ff 46 42                inc    DWORD PTR [rsi+0x42]  
112:    9a                      (bad)  
113:    17                      (bad)  
114:    2c 24                   sub    al,0x24  
116:    1f                      (bad)  
117:    95                      xchg   ebp,eax  
118:    db 11                   fist   DWORD PTR [rcx]  
11a:    10 10                   adc    BYTE PTR [rax],dl  
11c:    f9                      stc  
11d:    b8 11 10 10 77          mov    eax,0x77101011  
122:    73 ab                   jae    0xcf  
124:    26 1d 62 2e a4 9b       es sbb eax,0x9ba42e62  
12a:    20 21                   and    BYTE PTR [rcx],ah  
12c:    21 c8                   and    eax,ecx  
12e:    b6 20                   mov    dh,0x20  
130:    21 21                   and    DWORD PTR [rcx],esp  
132:    64 60                   fs (bad)  
134:    b8 35 0e 01 3d          mov    eax,0x3d010e35  
139:    b7 9b                   mov    bh,0x9b  
13b:    33 32                   xor    esi,DWORD PTR [rdx]  
13d:    32 db                   xor    bl,bl  
13f:    b4 33                   mov    ah,0x33  
141:    32 32                   xor    dh,BYTE PTR [rdx]  
143:    15 11 c9 44 7f          adc    eax,0x7f44c911  
148:    62                      (bad)  
149:    4c c6                   rex.WR (bad)  
14b:    db 42 43                fild   DWORD PTR [rdx+0x43]  
14e:    43 aa                   rex.XB stos BYTE PTR es:[rdi],al  
150:    36 42                   ss rex.X  
152:    43                      rex.XB  
153:    43 02 06                rex.XB add al,BYTE PTR [r14]  
156:    de 53 68                ficom  WORD PTR [rbx+0x68]  
159:    75 5b                   jne    0x1b6  
15b:    d1 d3                   rcl    ebx,1  
15d:    55                      push   rbp  
15e:    54                      push   rsp  
15f:    54                      push   rsp  
160:    bd 30 55 54 54          mov    ebp,0x54545530  
165:    33 37                   xor    esi,DWORD PTR [rdi]  
167:    ef                      out    dx,eax  
168:    62                      (bad)  
169:    59                      pop    rcx  
16a:    44 6a e0                rex.R push 0xffffffffffffffe0  
16d:    13 64 65 65             adc    esp,DWORD PTR [rbp+riz*2+0x65]  
171:    8c 36                   mov    WORD PTR [rsi],?  
173:    64 65 65 20 24 fc       fs gs and BYTE PTR gs:[rsp+rdi*8],ah  
179:    71 4a                   jno    0x1c5  
17b:    0b 79 f3                or     edi,DWORD PTR [rcx-0xd]  
17e:    13 77 76                adc    esi,DWORD PTR [rdi+0x76]  
181:    76 9f                   jbe    0x122  
183:    34 77                   xor    al,0x77  
185:    76 76                   jbe    0x1fd  
187:    90                      nop  
188:    90                      nop  
189:    90                      nop  
18a:    90                      nop  
18b:    90                      nop  
18c:    90                      nop  
18d:    90                      nop  
18e:    90                      nop  
18f:    90                      nop  
190:    90                      nop  
191:    90                      nop  
192:    90                      nop  
193:    90                      nop  
194:    90                      nop  
195:    90                      nop  
196:    90                      nop  
197:    90                      nop  
198:    90                      nop  
199:    90                      nop  
19a:    90                      nop  
19b:    90                      nop  
19c:    90                      nop  
19d:    90                      nop  
19e:    90                      nop  
19f:    90                      nop  
1a0:    90                      nop  
1a1:    90                      nop  
1a2:    90                      nop  
1a3:    90                      nop  
1a4:    90                      nop  
1a5:    90                      nop  
1a6:    90                      nop  
1a7:    90                      nop  
1a8:    90                      nop  
1a9:    90                      nop  
1aa:    90                      nop  
1ab:    90                      nop  
1ac:    90                      nop  
1ad:    90                      nop  
1ae:    90                      nop  
1af:    90                      nop  
1b0:    90                      nop  
1b1:    90                      nop  
1b2:    90                      nop  
1b3:    90                      nop  
1b4:    90                      nop  
1b5:    90                      nop  
1b6:    90                      nop  
1b7:    90                      nop  
1b8:    90                      nop  
1b9:    90                      nop  
1ba:    90                      nop  
1bb:    90                      nop  
1bc:    90                      nop  
1bd:    90                      nop  
1be:    90                      nop  
1bf:    90                      nop  
1c0:    90                      nop  
1c1:    90                      nop  
1c2:    90                      nop  
1c3:    90                      nop  
1c4:    90                      nop  
1c5:    90                      nop  
1c6:    90                      nop  
1c7:    90                      nop  
1c8:    90                      nop  
1c9:    90                      nop  
1ca:    90                      nop  
1cb:    90                      nop  
1cc:    90                      nop  
1cd:    90                      nop  
1ce:    90                      nop  
1cf:    90                      nop  
1d0:    90                      nop  
1d1:    90                      nop  
1d2:    90                      nop  
1d3:    90                      nop  
1d4:    90                      nop  
1d5:    90                      nop  
1d6:    90                      nop  
1d7:    90                      nop  
1d8:    90                      nop  
1d9:    90                      nop  
1da:    90                      nop  
1db:    90                      nop  
1dc:    90                      nop  
1dd:    90                      nop  
1de:    90                      nop  
1df:    90                      nop  
1e0:    90                      nop  
1e1:    90                      nop  
1e2:    90                      nop  
1e3:    90                      nop  
1e4:    90                      nop  
1e5:    90                      nop  
1e6:    90                      nop  
1e7:    90                      nop  
1e8:    90                      nop  
1e9:    90                      nop  
1ea:    90                      nop  
1eb:    90                      nop  
1ec:    90                      nop  
1ed:    90                      nop  
1ee:    90                      nop  
1ef:    90                      nop  
1f0:    90                      nop  
1f1:    90                      nop  
1f2:    90                      nop  
1f3:    90                      nop  
1f4:    90                      nop  
1f5:    90                      nop  
1f6:    90                      nop  
1f7:    90                      nop  
1f8:    90                      nop  
1f9:    90                      nop  
1fa:    90                      nop  
1fb:    90                      nop  
1fc:    90                      nop  
1fd:    90                      nop  
1fe:    90                      nop  
1ff:    90                      nop  
200:    90                      nop  
201:    90                      nop  
202:    90                      nop  
203:    90                      nop  
204:    90                      nop  
205:    90                      nop  
206:    90                      nop  
207:    90                      nop  
208:    90                      nop  
209:    90                      nop  
20a:    90                      nop  
20b:    90                      nop  
20c:    90                      nop  
20d:    90                      nop  
20e:    90                      nop  
20f:    90                      nop  
210:    90                      nop  
211:    90                      nop  
212:    90                      nop  
213:    90                      nop  
214:    90                      nop  
215:    90                      nop  
216:    90                      nop  
217:    90                      nop  
218:    90                      nop  
219:    90                      nop  
21a:    90                      nop  
21b:    90                      nop  
21c:    90                      nop  
21d:    90                      nop  
21e:    90                      nop  
21f:    90                      nop  
220:    90                      nop  
221:    90                      nop  
222:    90                      nop  
223:    90                      nop  
224:    90                      nop  
225:    90                      nop  
226:    90                      nop  
227:    90                      nop  
228:    90                      nop  
229:    90                      nop  
22a:    90                      nop  
22b:    90                      nop  
22c:    90                      nop  
22d:    90                      nop  
22e:    90                      nop  
22f:    90                      nop  
230:    90                      nop  
231:    90                      nop  
232:    90                      nop  
233:    90                      nop  
234:    90                      nop  
235:    90                      nop  
236:    90                      nop  
237:    90                      nop  
238:    90                      nop  
239:    90                      nop  
23a:    90                      nop  
23b:    90                      nop  
23c:    90                      nop  
23d:    90                      nop  
23e:    90                      nop  
23f:    90                      nop  
240:    90                      nop  
241:    90                      nop  
242:    90                      nop  
243:    90                      nop  
244:    90                      nop  
245:    90                      nop  
246:    90                      nop  
247:    90                      nop  
248:    90                      nop  
249:    90                      nop  
24a:    90                      nop  
24b:    90                      nop  
24c:    90                      nop  
24d:    90                      nop  
24e:    90                      nop  
24f:    90                      nop  
250:    90                      nop  
251:    90                      nop  
252:    90                      nop  
253:    90                      nop  
254:    90                      nop  
255:    90                      nop  
256:    90                      nop  
257:    90                      nop  
258:    90                      nop  
259:    90                      nop  
25a:    90                      nop  
25b:    90                      nop  
25c:    90                      nop  
25d:    90                      nop  
25e:    90                      nop  
25f:    90                      nop  
260:    90                      nop  
261:    90                      nop  
262:    90                      nop  
263:    90                      nop  
264:    90                      nop  
265:    90                      nop  
266:    90                      nop  
267:    90                      nop  
268:    90                      nop  
269:    90                      nop  
26a:    90                      nop  
26b:    90                      nop  
26c:    90                      nop  
26d:    90                      nop  
26e:    90                      nop  
26f:    90                      nop  
270:    90                      nop  
271:    90                      nop  
272:    90                      nop  
273:    90                      nop  
274:    90                      nop  
275:    90                      nop  
276:    90                      nop  
277:    90                      nop  
278:    90                      nop  
279:    90                      nop  
27a:    90                      nop  
27b:    90                      nop  
27c:    90                      nop  
27d:    90                      nop  
27e:    90                      nop  
27f:    90                      nop  
280:    90                      nop  
281:    90                      nop  
282:    90                      nop  
283:    90                      nop  
284:    90                      nop  
285:    90                      nop  
286:    90                      nop  
287:    90                      nop  
288:    90                      nop  
289:    90                      nop  
28a:    90                      nop  
28b:    90                      nop  
28c:    90                      nop  
28d:    90                      nop  
28e:    90                      nop  
28f:    90                      nop  
290:    90                      nop  
291:    90                      nop  
292:    90                      nop  
293:    90                      nop  
294:    90                      nop  
295:    90                      nop  
296:    90                      nop  
297:    90                      nop  
298:    90                      nop  
299:    90                      nop  
29a:    90                      nop  
29b:    90                      nop  
29c:    90                      nop  
29d:    90                      nop  
29e:    90                      nop  
29f:    90                      nop  
2a0:    90                      nop  
2a1:    90                      nop  
2a2:    90                      nop  
2a3:    90                      nop  
2a4:    90                      nop  
2a5:    90                      nop  
2a6:    90                      nop  
2a7:    90                      nop  
2a8:    90                      nop  
2a9:    90                      nop  
2aa:    90                      nop  
2ab:    90                      nop  
2ac:    90                      nop  
2ad:    90                      nop  
2ae:    90                      nop  
2af:    90                      nop  
2b0:    90                      nop  
2b1:    90                      nop  
2b2:    90                      nop  
2b3:    90                      nop  
2b4:    90                      nop  
2b5:    90                      nop  
2b6:    90                      nop  
2b7:    90                      nop  
2b8:    90                      nop  
2b9:    90                      nop  
2ba:    90                      nop  
2bb:    90                      nop  
2bc:    90                      nop  
2bd:    90                      nop  
2be:    90                      nop  
2bf:    90                      nop  
2c0:    90                      nop  
2c1:    90                      nop  
2c2:    90                      nop  
2c3:    90                      nop  
2c4:    90                      nop  
2c5:    90                      nop  
2c6:    90                      nop  
2c7:    90                      nop  
2c8:    90                      nop  
2c9:    58                      pop    rax  
2ca:    5f                      pop    rdi  
2cb:    41 b8 00 00 00 00       mov    r8d,0x0  
2d1:    49 83 f8 11             cmp    r8,0x11  
2d5:    74 1c                   je     0x2f3  
2d7:    8a 1f                   mov    bl,BYTE PTR [rdi]  
2d9:    88 c1                   mov    cl,al  
2db:    30 cb                   xor    bl,cl  
2dd:    88 1f                   mov    BYTE PTR [rdi],bl  
2df:    49 ff c0                inc    r8  
2e2:    48 ff c7                inc    rdi  
2e5:    eb ea                   jmp    0x2d1  
2e7:    b8 3c 00 00 00          mov    eax,0x3c  
2ec:    bf 01 00 00 00          mov    edi,0x1  
2f1:    0f 05                   syscall  
2f3:    c3                      ret
```

