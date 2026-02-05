Mappa degli indirizzi OpenPLC e Modbus

| **Variabile OpenPLC** | **Tipo Modbus**               | **Indirizzo Modbus (Offset)** | **Note**              |
| --------------------- | ----------------------------- | ----------------------------- | --------------------- |
| **%QX0.0**            | Coil (Read/Write)             | **0**                         | Uscita digitale bit 0 |
| **%QX0.1**            | Coil (Read/Write)             | **1**                         | Uscita digitale bit 1 |
| **%IW0**              | Input Register (Read Only)    | **0**                         | Ingresso analogico    |
| **%QW0**              | Holding Register (Read/Write) | **0**                         | Uscita analogica      |
| **%MW0**              | Holding Register (Read/Write) | **1024**                      | Memory Register       |
| **%MW1**              | Holding Register (Read/Write) | **1025**                      |                       |
Codice per leggere i sopracitati registri di una singola PLC:

```python
2502: {
	"input_registers": [(0, 1)], # %IW0
	"coils": [(0, 2)], # %QX0.0 e %QX0.1
	"holding_registers": [(0, 1), (1025, 1)], # %QW0 e %MW1
}
```

