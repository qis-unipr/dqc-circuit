from qiskit.circuit import Instruction

from qiskit.qasm.node.node import Node


class RemoteCxNode(Node):

    def __init__(self, children):
        super().__init__("remoteCx", children, [])

    def qasm(self):
        """Return the corresponding OPENQASM string."""
        return "remoteCx " + self.children[0].qasm() + ";"


class RemoteCxInstr(Instruction):

    # _directive = True

    def __init__(self):
        """Create new remoteCx instruction."""
        super().__init__("remoteCx", 4, 0, [])
        self.label = 'RemoteCx'
