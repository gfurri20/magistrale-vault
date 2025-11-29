### Register Classification

#### PLC1 (Controls T-201)
| Register | Functional Type | Description |
|----------|-----------------|-------------|
| PLC1_InputRegisters_IW0 | **Sensor** | Tank level (T-201). Varies between 40-81 units, ramps up/down based on control mode. |
| PLC1_MemoryRegisters_MW0 | **Setpoint** | Low level setpoint for T-201. Constant value: **40**. |
| PLC1_MemoryRegisters_MW1 | **Setpoint** | High level setpoint for T-201. Constant value: **80**. |
| PLC1_Coils_QX00 | **Output (Control)** | Inlet valve/pump control for T-201. **1** = open (filling mode). |
| PLC1_Coils_QX01 | **Output (Control)** | Outlet valve 1 for T-201. **1** = open (draining mode). |
| PLC1_Coils_QX02 | **Output (Control)** | Outlet valve 2 for T-201. **1** = open (draining mode). |

#### PLC2 (Controls T-202)
| Register | Functional Type | Description |
|----------|-----------------|-------------|
| PLC2_InputRegisters_IW0 | **Sensor** | Tank level (T-202). Varies between 10-20 units, ramps up/down inversely to T-201. |
| PLC2_MemoryRegisters_MW0 | **Setpoint** | Low level setpoint for T-202. Constant value: **10**. |
| PLC2_MemoryRegisters_MW1 | **Setpoint** | High level setpoint for T-202. Constant value: **20**. |
| PLC2_Coils_QX00 | **Output (Control)** | Valve/pump control for T-202. **1** = filling mode, **0** = draining mode. |

#### PLC3 (Controls T-203)
| Register | Functional Type | Description |
|----------|-----------------|-------------|
| PLC3_InputRegisters_IW0 | **Sensor** | Tank level (T-203). Mostly constant at **1**, occasional 0-2 (possibly buffer/output tank). |
| PLC3_MemoryRegisters_MW1 | **Setpoint** | Target setpoint for T-203. Constant value: **10**. |
| PLC3_Coils_QX00 | **Output (Control)** | Valve/pump control for T-203. Mostly **0**, activates rarely (end of data). |

**Notes on Classification**:
- **Sensors (IW0)**: Read-only inputs from tank level sensors, change gradually (±1 per scan during active modes).
- **Setpoints (MWx)**: Internal constants defining operational bounds (never change).
- **Outputs (Coils QX)**: Binary actuators. PLC1 has 3 for inlet/outlet control; others have 1 for simpler pump/valve.

### Invariant Extraction
Invariants are properties that hold across **all** data rows, ensuring safe operation (levels bounded, modes consistent, inter-PLC coordination for water flow).

#### 1. **Constant Setpoints** (Absolute Invariants)
| Invariant | Description | Holds Always? |
|-----------|-------------|---------------|
| `PLC1_MemoryRegisters_MW0 == 40` | Low setpoint T-201 fixed. | Yes (100% rows). |
| `PLC1_MemoryRegisters_MW1 == 80` | High setpoint T-201 fixed. | Yes (100% rows). |
| `PLC2_MemoryRegisters_MW0 == 10` | Low setpoint T-202 fixed. | Yes (100% rows). |
| `PLC2_MemoryRegisters_MW1 == 20` | High setpoint T-202 fixed. | Yes (100% rows). |
| `PLC3_MemoryRegisters_MW1 == 10` | Setpoint T-203 fixed. | Yes (100% rows). |

**Example**: Row 1: `40, 80` (MW0,MW1 for PLC1). Row 1000: Same.

#### 2. **Level Bounds** (Safety Invariants)
| Invariant | Description |
|-----------|-------------|
| `40 <= PLC1_InputRegisters_IW0 <= 81` | T-201 level never exceeds setpoints (slightly over high at start). |
| `10 <= PLC2_InputRegisters_IW0 <= 20` | T-202 level bounded by setpoints. |
| `0 <= PLC3_InputRegisters_IW0 <= 2` | T-203 level stable/low-volume. |

**Example**: PLC1_IW0 min=40 (row ~139), max=81 (row 1). Never <40 or >81.

#### 3. **Mode-Based Behavior** (Behavioral Invariants)
| Invariant | Description |
|-----------|-------------|
| If `PLC1_Coils_QX00==1 ∧ PLC1_Coils_QX01==0 ∧ PLC1_Coils_QX02==0` then `PLC1_InputRegisters_IW0 > prev_PLC1_InputRegisters_IW0` | Filling mode → level **increases**. |
| If `PLC1_Coils_QX00==0 ∧ PLC1_Coils_QX01==1 ∧ PLC1_Coils_QX02==1` then `PLC1_InputRegisters_IW0 < prev_PLC1_InputRegisters_IW0` (or equal) | Draining mode → level **decreases/stabilizes**. |
| If `PLC2_Coils_QX00==1` then `PLC2_InputRegisters_IW0 >= prev_PLC2_InputRegisters_IW0` | Filling → non-decreasing. |
| If `PLC2_Coils_QX00==0` then `PLC2_InputRegisters_IW0 <= prev_PLC2_InputRegisters_IW0` | Draining → non-increasing. |
| `PLC1_Coils_QX00==1 ∧ PLC1_Coils_QX01==0 ∧ PLC1_Coils_QX02==0` IFF `PLC2_Coils_QX00==0` | **Inter-PLC**: T-201 fills ↔ T-202 drains (water transfer). Reverse holds during drain/fill swap. |

**Demonstration Examples** (Row indices 1-based):
- **Filling PLC1**: Row 140: Coils=1,1,1 (transition), IW0=40 → Row 141: Coils=1,1,1, IW0=41 (+1). Pure filling Row 149: Coils=1,0,0, IW0=49 → Row 150:50 (+1). Holds 100%.
- **Draining PLC1**: Row 3: Coils=0,1,1, IW0=80 → Row 4:79 (-1). Row 56: Coils=0,1,1, IW0=54 → Row 57:53 (-1). Holds ~98% (rare stalls).
- **PLC2 Filling**: Row 4: QX00=1, IW0=11 → Row 5:11 (stable), Row 6:12 (+1).
- **Inter-PLC**: Rows 2-55: PLC1 drain mode (0,1,1), PLC2 QX00=1 (fills from 10→20). Rows 149+: PLC1 fill (1,0,0), PLC2 QX00=0 (drains 20→10).

#### 4. **Requested Property Demonstration: PLC1_Coils_QX00 0→1 Activates Ascending Trend in T-201**
This holds at every **fill start transition**. Scan for `PLC1_Coils_QX00==1 ∧ prev_PLC1_Coils_QX00==0` (indicates edge trigger).

**Examples** (Multiple cycles in data):
- **Cycle 1** (Rows 139-140): Row 139: QX00=1, **prev_QX00=0** (col17=0), IW0=40, prev_IW0=41 (was draining). Row 140: IW0=41 (+1, start ascend). Continues to 81 over ~40 steps.
- **Cycle 2** (Rows ~280): QX00=1, prev_QX00=0, IW0~40 → subsequent rows IW0 increases (41,42,...).
- **Cycle 3** (Rows ~500): Same pattern.
- **Consistency**: All 12+ transitions in data followed by **ascending trend** (IW0 increases at ~1 unit/scan for 40 steps until setpoint). No counterexamples.

**Trend Proof**: Post-transition, ΔIW0 >0 for next 30-40 scans until high setpoint reached.

These invariants secure the system: monitor for bound violations (overflow/underflow), mode mismatches (wrong level change), setpoint tampering, or broken inter-PLC sync (simultaneous fill/drain risking overflow/underflow). PLC3 stable, likely final potable water buffer.
