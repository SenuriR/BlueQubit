import bluequbit
from qiskit import QuantumCircuit

qc_qiskit = QuantumCircuit(4)
qc_qiskit.h(0)
qc_qiskit.h(1)
qc_qiskit.h(2)
qc_qiskit.h(3)
qc_qiskit.measure_all()

bq = bluequbit.init("YOUR_TOKEN_HERE")
result = bq.run(qc_qiskit, device='quantum') # <-- Quantum Magic
print(result.get_counts())