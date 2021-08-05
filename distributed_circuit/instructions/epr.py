from qiskit.circuit import Instruction

from qiskit.qasm.node.node import Node


class EPRNode(Node):

    def __init__(self, children):
        super().__init__("epr", children, [])

    def qasm(self):
        """Return the corresponding OPENQASM string."""
        return "epr " + self.children[0].qasm() + ";"


class EPRInstr(Instruction):

    # _directive = True

    def __init__(self):
        """Create new remoteCx instruction."""
        super().__init__("epr", 2, 0, [])
        self.label = 'EPR'