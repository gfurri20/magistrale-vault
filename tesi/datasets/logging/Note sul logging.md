Mappa degli indirizzi OpenPLC e Modbus

| **Variabile OpenPLC** | **Tipo Modbus**               | **Indirizzo Modbus (Offset)** | **Note**              |
| --------------------- | ----------------------------- | ----------------------------- | --------------------- |
| **%QX0.0**            | Coil (Read/Write)             | **0**                         | Uscita digitale bit 0 |
| **%QX0.1**            | Coil (Read/Write)             | **1**                         | Uscita digitale bit 1 |
| **%IW0**              | Input Register (Read Only)    | **0**                         | Ingresso analogico    |
| **%QW0**              | Holding Register (Read/Write) | **0**                         | Uscita analogica      |
| **%MW0**              | Holding Register (Read/Write) | **1024**                      | Memory Register       |
| **%MW1**              | Holding Register (Read/Write) | **1025**                      |                       |
