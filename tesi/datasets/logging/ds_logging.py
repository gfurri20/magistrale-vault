import time
import signal
import sys
import atexit
import easymodbus.modbusClient
from tqdm import trange
# import matplotlib.pyplot as plt

TARGET_IP = "localhost"

LOG_FILE = f"plc_data_log_{time.strftime('%Y%m%d_%H%M%S')}.csv"
TIME_BETWEEN_SAMPLES = 0.1  # in seconds; but keep in mind that reading multiple registers takes time
CAPTURE_LEN = 10  # in seconds
LEN_GATHER_SAMPLES = int(CAPTURE_LEN / TIME_BETWEEN_SAMPLES)

plc_ports_and_registers = {
    # PLC1
    2502: {
        "input_registers": [(0, 1)],
        "coils": [(0, 2)],
        "holding_registers": [(0, 1), (1025, 1)],
        #"discrete_input_registers": [(0, 0)],
    },
    # PLC2
    3502: {
        "input_registers": [(0, 1)],
        "coils": [(0, 3)],
        "holding_registers": [(0, 1), (1025, 1)],
        #"discrete_input_registers": [(0, 0)],
    },
    # PLC3
    4502: {
        "input_registers": [(0, 1)],
        "coils": [(0, 2)],
        "holding_registers": [(0, 1), (1025, 1)],
        #"discrete_input_registers": [(0, 0)],
    },
    # PLC4
    5502: {
        "input_registers": [(0, 1)],
        "coils": [(0, 3)],
        "holding_registers": [(0, 1), (1025, 1)],
        #"discrete_input_registers": [(0, 0)],
    }
}

# create the header for my log file
with open(LOG_FILE, "w") as f:
    header = "timestamp"
    for port, regs in plc_ports_and_registers.items():
        for start, count in regs["input_registers"]:
            for i in range(count):
                header += f",PLC{port}_IR{start + i}"
        for start, count in regs["coils"]:
            for i in range(count):
                header += f",PLC{port}_C{start + i}"
        for start, count in regs["holding_registers"]:
           for i in range(count):
               header += f",PLC{port}_HW{start + i}"
        # for start, count in regs["discrete_input_registers"]:
        #     for i in range(count):
        #         header += f",PLC{port}_DR{start + i}"

    # use this to replace the name of the PLCs in the header if needed
    header = header.replace("2502", "1").replace("3502", "2").replace("4502", "3").replace("5502", "4")

    f.write(header + "\n")

# connect to plcs
plcs = [
    easymodbus.modbusClient.ModbusClient(TARGET_IP, port) for port in list(plc_ports_and_registers.keys())
]
for plc in plcs:
    plc.connect()

print("Reading from PLCs...")

input_registers_histories = [[] for _ in plcs]
coil_histories = [[] for _ in plcs]

for _ in trange(LEN_GATHER_SAMPLES, desc="Gathering samples"):
    
    #start_time = time.time()
    log_line = f"{time.time()}"
    for idx, plc in enumerate(plcs):
        regs = plc_ports_and_registers[list(plc_ports_and_registers.keys())[idx]]
        for start, count in regs["input_registers"]:
            inputRegisters = plc.read_inputregisters(start, count)
            input_registers_histories[idx].append(inputRegisters)
            for val in inputRegisters:
                log_line += f",{val}"
        for start, count in regs["coils"]:
            coils = plc.read_coils(start, count)
            coil_histories[idx].append(coils)
            for val in coils:
                log_line += f",{val}"
        for start, count in regs["holding_registers"]:
           holdingRegisters = plc.read_holdingregisters(start, count)
           for val in holdingRegisters:
               log_line += f",{val}"
        # for start, count in regs["discrete_input_registers"]:
        #     discreteInputs = plc.read_discreteinputs(start, count)
        #     for val in discreteInputs:
        #         log_line += f",{val}"
    #print(f"Sampled in {time.time() - start_time} seconds")

    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")

    time.sleep(TIME_BETWEEN_SAMPLES)

# # Convert to lists for plotting
# input_registers_histories = [list(zip(*hist)) for hist in input_registers_histories]

# plt.figure(figsize=(14, 7))
# colors = ['b', 'g', 'r']
# for plc_idx, (reg_hist, coil_hist) in enumerate(zip(input_registers_histories, coil_histories)):
#     for idx, reg_values in enumerate(reg_hist):
#         plt.plot(reg_values, label=f'PLC{plc_idx+1} Input Register {idx}', color=colors[plc_idx], alpha=0.7)
#     plt.plot(coil_hist, label=f'PLC{plc_idx+1} Coil 0', linestyle='--', color=colors[plc_idx], alpha=0.7)
# plt.legend()
# plt.title('PLC Input Registers and Coil 0 over Time (All PLCs)')
# plt.xlabel('Sample')
# plt.ylabel('Value')
# plt.show()

def _close_all_plcs():
    for plc in plcs:
        try:
            plc.close()
        except Exception:
            pass

# Ensure PLCs are closed on normal exit
atexit.register(_close_all_plcs)

# Ensure PLCs are closed on SIGINT / SIGTERM (Ctrl+C)
def _signal_handler(signum, frame):
    _close_all_plcs()
    sys.exit(0)

signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# Close on normal end of script
_close_all_plcs()
