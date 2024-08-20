import bluequbit
from bluequbit.library import multi_adder
from qiskit import QuantumCircuit
from math import ceil, log2
from coin_toss import qc_qiskit

m = 4 # number of registers
n = 3 # number of qubits in each register

num_sum_qubits = int(ceil(log2(m * (2**n - 1) + 0.5)))  # number of qubits required to store the sum
num_qubits = m * n + num_sum_qubits - n

qc = QuantumCircuit(num_qubits, num_sum_qubits)
qc.h(range(m * n))  # Now each register is in superposition of 0, 1, 2, 3, 4, 5, 6, 7
qc.compose(multi_adder(m, n), inplace=True)
qc.measure(range(num_qubits-num_sum_qubits, num_qubits), range(num_sum_qubits))

bq = bluequbit.init("YOUR_TOKEN_HERE")
# result = bq.run(qc_qiskit)
result = bq.run(qc_qiskit, device='quantum')
print(result.get_counts())