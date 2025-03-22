
| LV           | Password     |
| ------------ | ------------ |
| `leviathan1` | `3QJ3TgzHDq` |
| `leviathan2` | `NsN1HwFoyN` |
| `leviathan3` | `f0n8h2iWLP` |
| `leviathan4` | `WG1egElCvO` |
| `leviathan5` | `0dyxT7F4QD` |
| `leviathan6` | `szo7HDB88w` |

## leviathan0
Cerca nel file html in `.backup` la parola `leviathan1`

# leviathan1
`ltrace` risolve i problemi, esagerato usare ghidra

# leviathan2
Qua avevo capito la vulnerabilità, ovvero la possibile command injection su
`snprintf(cmd, 511, "/bin/cat %s", argv[1]);`

Ma non capivo dove potevo creare un file con nome corrotto, cercando su internet ho visto che era possibile creare cartelle in `/tmp`

Allora basta creare `"/tmp/foo;sh"` ed eseguire `./printfile .....` per avere una shell

# leviathan3
`ltrace` risolve i problemi, esagerato usare ghidra

# leviathan4
No comment ahaha

# leviathan5
Link simbolico `-s` sul file letto
