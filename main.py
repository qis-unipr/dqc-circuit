from distributed_circuit import DistQuantumCircuit

qc = DistQuantumCircuit.from_qasm_file('tests/test.qasm')

print(qc.qasm())
print(qc)
qc = qc.decompose()
print(qc.qasm())
print(qc.draw(output='text'))
