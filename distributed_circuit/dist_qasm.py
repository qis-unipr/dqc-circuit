from qiskit.qasm.qasm import Qasm

from dqc_parser.parser import DQCParser


class DistQasm(Qasm):

    def __init__(self, filename=None, data=None):
        super().__init__(filename=filename, data=data)

    def parse(self):
        """Parse the data."""
        if self._filename:
            with open(self._filename) as ifile:
                self._data = ifile.read()

        with DQCParser(self._filename) as qasm_p:
            qasm_p.parse_debug(False)
            return qasm_p.parse(self._data)
