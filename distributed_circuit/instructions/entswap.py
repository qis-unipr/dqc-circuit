from qiskit.circuit import Instruction, Measure, Gate

from qiskit.qasm.node.node import Node


class EntSwapNode(Node):

    def __init__(self, children):
        super().__init__("entswap", children, [])

    def qasm(self):
        """Return the corresponding OPENQASM string."""
        # return "entswap " + self.children[0].qasm() + "->" + self.children[1].qasm() + ";"
        return "entswap " + self.children[0].qasm() + ";"


class EntSwapInstr(Instruction):

    # _directive = True

    def __init__(self, num_qubits):
        """Create new entswaè instruction."""
        # super().__init__("entswap", num_qubits, num_qubits-2, [])
        super().__init__("entswap", num_qubits, 0, [])
        self.label = 'EntSwap'

    # def broadcast_arguments(self, qargs, cargs):
    #     for i in range(1, self.num_qubits - 1, 2):
    #         yield qargs[i][0], qargs[i+1][0]
    #     # for i in range(self.num_clbits):
    #     #     yield qargs[i+1][0], cargs[i][0]
    #     for i in range(1, self.num_clbits, 2):
    #         yield qargs[i+1], cargs[i]
    #         yield qargs[-1][0], [cargs[i]]
    #     # for i in range(0, self.num_clbits, 2):
    #     #     yield qargs[0], cargs[i]

    # def c_if(self, classical, val):
    #     raise QiskitError("Barriers are compiler directives and cannot be conditional.")

    # def _define(self):
    #     # pylint: disable=cyclic-import
    #     from qiskit.circuit.quantumcircuit import QuantumCircuit, QuantumRegister, ClassicalRegister
    #     from qiskit.circuit.library import SGate, HGate, CXGate, XGate
    #
    #     q = QuantumRegister(self.num_qubits, "q")
    #     # print(self.num_qubits)
    #     # print(self.num_clbits)
    #     cregs = []
    #     for i in range(self.num_clbits):
    #         cregs.append(ClassicalRegister(1))
    #     # c = ClassicalRegister(self.num_clbits, "c")
    #     qc = QuantumCircuit(q, name=self.name)
    #     for creg in cregs:
    #         qc.add_register(creg)
    #     # rules = []
    #     for i in range(1, self.num_qubits-1, 2):
    #         qc.cx(q[i], q[i+1])
    #         # rules.append((CXGate(), [q[i], q[i+1]], []))
    #     for i in range(1, self.num_clbits, 2):
    #         qc.measure(q[i+1], cregs[i][0])
    #         # qc.measure(q[i+1], cregs[i][0])
    #         qc.x(q[-1]).c_if(cregs[i], 1)
    #         # rules.append((Measure(), [q[i+1]], [cregs[i][0]]))
    #
    #     # for rule in rules:
    #     #     qc._append(*rule)
    #
    #     # print(qc)
    #
    #     self.definition = qc
