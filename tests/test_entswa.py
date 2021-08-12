from distributed_circuit import DistQuantumCircuit

qc = DistQuantumCircuit.from_qasm_file('test_entswap.qasm')

print(qc.qasm())
print(qc)
qc = qc.decompose()
print(qc.qasm())
print(qc.draw(output='text'))
