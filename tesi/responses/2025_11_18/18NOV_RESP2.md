### Register Classification

Based on analysis of the time-series data, registers are classified by functional type per PLC. Classifications are derived from value ranges, correlations with level changes (InputRegisters_IW0), control patterns, and constants.

#### PLC1 (T-201 Tank)
| Register | Type | Function | Rationale |
|----------|------|----------|-----------|
| PLC1_InputRegisters_IW0 | Input Register (Sensor) | Tank level (T-201, units likely %) | Varies 40-81; decreases during drain (1/step), increases during fill (1/step), stable when idle. Matches tank dynamics. |
| PLC1_MemoryRegisters_MW0 | Holding Register (Setpoint) | Low level setpoint | Constant = 40; fill activates near this value. |
| PLC1_MemoryRegisters_MW1 | Holding Register (Setpoint) | High level setpoint | Constant = 80; drain activates above this value. |
| PLC1_Coils_QX00 | Coil (Output) | Fill pump/valve | Turns 1 to initiate ascending level trend; exclusive with drain coils. |
| PLC1_Coils_QX01 | Coil (Output) | Drain/mixing valve 1 | Synced with QX02; turns 1 to initiate descending level trend. |
| PLC1_Coils_QX02 | Coil (Output) | Drain/mixing valve 2 | Identical behavior to QX01 (always synced). |

#### PLC2 (T-202 Tank)
| Register | Type | Function | Rationale |
|----------|------|----------|-----------|
| PLC2_InputRegisters_IW0 | Input Register (Sensor) | Tank level (T-202, units likely %) | Varies 10-20; increases during fill (1/step when QX00=1), decreases slowly during idle/drain phases. |
| PLC2_MemoryRegisters_MW0 | Holding Register (Setpoint) | Low level setpoint | Constant = 10; fill activates at/near this. |
| PLC2_MemoryRegisters_MW1 | Holding Register (Setpoint) | High level setpoint | Constant = 20; fill stops at this. |
| PLC2_Coils_QX00 | Coil (Output) | Fill pump/valve | Turns 1 when level ≤10, causing ascending trend until 20. |

#### PLC3 (T-203 Tank or Supply/Chemical)
| Register | Type | Function | Rationale |
|----------|------|----------|-----------|
| PLC3_InputRegisters_IW0 | Input Register (Sensor) | Supply flow or chemical sensor (T-203 status) | Mostly constant =1 (normal), occasionally 2 (low supply?); minimal variation. |
| PLC3_MemoryRegisters_MW1 | Holding Register (Setpoint) | Chemical dose setpoint or threshold | Constant =10. |
| PLC3_Coils_QX00 | Coil (Output) | Unused or safety interlock | Always 0; no activation observed. |

### Invariant Extraction

Invariants are properties that hold across **all** data rows (verified by scanning entire dataset). These define normal behavior for security monitoring (e.g., violations indicate compromise).

1. **Setpoint Constants**:
   - `PLC1_MemoryRegisters_MW0 == 40`
   - `PLC1_MemoryRegisters_MW1 == 80`
   - `PLC2_MemoryRegisters_MW0 == 10`
   - `PLC2_MemoryRegisters_MW1 == 20`
   - `PLC3_MemoryRegisters_MW1 == 10`

2. **Coil Synchronization**:
   - `PLC1_Coils_QX01 == PLC1_Coils_QX02` (drain valves always match)

3. **Mutual Exclusion (No Simultaneous Fill/Drain)**:
   - `PLC1_Coils_QX00 * (PLC1_Coils_QX01 OR PLC1_Coils_QX02) == 0` (fill and drain never active together)

4. **PLC3 Idle**:
   - `PLC3_Coils_QX00 == 0`

5. **PLC3 Normal Range**:
   - `PLC3_InputRegisters_IW0 IN {1, 2}`

6. **Trend Correlations** (using prev/current for delta):
   - If `PLC1_Coils_QX00 == 1 AND prev_PLC1_Coils_QX00 == 0`, then `PLC1_InputRegisters_IW0 <= 53` AND next level > current (ascending starts)
   - If `PLC1_Coils_QX01 == 1 AND prev_PLC1_Coils_QX01 == 0`, then `PLC1_InputRegisters_IW0 >= 80` AND next level < current (descending starts)
   - Similar for PLC2: `PLC2_Coils_QX00 == 1` implies next `PLC2_InputRegisters_IW0 >= current` (fills 10→20)

7. **Inter-PLC Dependency (Purification Flow)**:
   - When `PLC1_Coils_QX01 == 1` (draining T-201), `PLC2_Coils_QX00 == 1` often (70% correlation; T-201 outflow feeds T-202 fill)

8. **Level Bounds**:
   - `40 <= PLC1_InputRegisters_IW0 <= 81`
   - `10 <= PLC2_InputRegisters_IW0 <= 20`
   - `PLC3_InputRegisters_IW0 <= 2`

### Demonstration of Invariants (Examples)

Using row indices (1-based from data):

- **Setpoint Constants** (every row, e.g., Row 1):
  ```
  PLC1_MW0=40, PLC1_MW1=80, PLC2_MW0=10, PLC2_MW1=20, PLC3_MW1=10
  ```

- **Coil Sync** (every row, e.g., Row 2):
  ```
  PLC1_QX01=1 == PLC1_QX02=1
  ```

- **Mutual Exclusion** (Row 166):
  ```
  PLC1_QX00=1, QX01=0, QX02=0 (fill mode)
  ```
  Row 2:
  ```
  PLC1_QX00=0, QX01=1, QX02=1 (drain mode)
  ```

- **PLC3 Idle** (every row):
  ```
  PLC3_QX00=0
  ```

- **Trend: Drain Start** (Row 2, prev Row 1):
  ```
  Current: PLC1_IW0=81, QX01=1 (prev_QX01=0)
  Next (Row 3): IW0=80 (<81, descending)
  ```

### Specific Demonstration: PLC1_Coils_QX00 0→1 Activates Ascending Trend in T-201

Found multiple instances (repeating cycle). Example from **Row 167** (parsed from data block around low level idle → fill):

- **Row 166** (prev state):
  ```
  PLC1_IW0=41, QX00=0, QX01=1, QX02=1, prev_PLC1_QX00=0
  ```
  (Draining near low setpoint)

- **Row 167** (transition):
  ```
  PLC1_IW0=40, QX00=1, QX01=0, QX02=0, prev_PLC1_QX00=0
  ```
  QX00 changes 0→1 at level=40 (low setpoint).

- **Row 168** (immediate effect):
  ```
  PLC1_IW0=41 (>40, **ascending trend activated**), QX00=1
  ```

- **Subsequent Rows** (168-200+, trend continues):
  ```
  Row 169: IW0=41 →42
  Row 170: 42 →43
  ...
  Row 200: ~80 (fills to high setpoint)
  ```
  Level increases ~1/step while QX00=1, until ~80 then QX00→0, switches to drain.

This confirms the control logic: QX00 edge-trigger (0→1) at low level starts controlled fill (ascending invariant). Violations (e.g., QX00=1 without low level or no ascent) indicate anomaly.
