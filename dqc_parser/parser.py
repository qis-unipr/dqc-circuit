import tempfile

from ply import yacc

from qiskit.qasm.qasmparser import QasmParser

from distributed_circuit.instructions import EPRNode, RemoteCxNode, EntSwapNode
from .lexer import DQCLexer


class DQCParser(QasmParser):

    def __init__(self, filename):
        """Create the dqc_parser."""
        if filename is None:
            filename = ""
        self.lexer = DQCLexer(filename)
        self.tokens = self.lexer.tokens
        self.parse_dir = tempfile.mkdtemp(prefix="qiskit")
        self.precedence = (
            ("left", "+", "-"),
            ("left", "*", "/"),
            ("left", "negative", "positive"),
            ("right", "^"),
        )
        # For yacc, also, write_tables = Bool and optimize = Bool
        self.parser = yacc.yacc(module=self, debug=False, outputdir=self.parse_dir)
        self.qasm = None
        self.parse_deb = False
        self.global_symtab = {}  # global symtab
        self.current_symtab = self.global_symtab  # top of symbol stack
        self.symbols = []  # symbol stack
        self.external_functions = ["sin", "cos", "tan", "exp", "ln", "sqrt", "acos", "atan", "asin"]

    # def p_gate_op_6(self, program):
    #     """
    #     gate_op : REMOTECX id ',' id ',' id ',' id ';'
    #     """
    #     program[0] = RemoteCxNode([program[2], program[4], program[6], program[8]])
    #     self.verify_declared_bit(program[2])
    #     self.verify_declared_bit(program[4])
    #     self.verify_declared_bit(program[6])
    #     self.verify_declared_bit(program[8])
    #     self.verify_distinct([program[2], program[4], program[6], program[8]])

    # def p_gate_op_7(self, program):
    #     """
    #     gate_op : ENTSWAP id_list ';'
    #     """
    #     # gate_op: ENTSWAP id_list ASSIGN id_list ';'
    #     # program[0] = EntSwapNode([program[2], program[4]])
    #     program[0] = EntSwapNode([program[2]])
    #     self.verify_bit_list(program[2])
    #     self.verify_distinct([program[2]])
    #     # self.verify_bit_list(program[4])
    #     # self.verify_distinct([program[4]])
    #
    # def p_gate_op_7e(self, _):
    #     """
    #     gate_op : ENTSWAP error
    #     """
    #     raise QasmError("Invalid entswap inside gate definition.")

    def p_quantum_op(self, program):
        """
        quantum_op : unitary_op
                   | opaque
                   | measure
                   | barrier
                   | epr
                   | remoteCx
                   | entswap
                   | reset
                   | if
        """
        program[0] = program[1]

    def p_epr(self, program):
        """
        epr : EPR primary ',' primary
        """

        program[0] = EPRNode([program[2], program[4]])
        self.verify_reg(program[2], "qreg")
        self.verify_reg(program[4], "qreg")
        self.verify_distinct([program[2], program[4]])

    def p_remoteCx(self, program):
        """
        remoteCx : REMOTECX primary ',' primary ',' primary ',' primary
        """

        program[0] = RemoteCxNode([program[2], program[4], program[6], program[8]])
        self.verify_reg(program[2], "qreg")
        self.verify_reg(program[4], "qreg")
        self.verify_reg(program[6], "qreg")
        self.verify_reg(program[8], "qreg")
        self.verify_distinct([program[2], program[4], program[6], program[8]])

    def p_entswap(self, program):
        """
        entswap : ENTSWAP primary_list
        """
        # entswap: ENTSWAP primary_list ASSIGN primary_list
        # program[0] = EntSwapNode([program[2], program[4]])
        program[0] = EntSwapNode([program[2]])
        # print(program[2].qasm())
        # print(program[4].qasm())
        self.verify_reg_list(program[2], "qreg")
        # self.verify_reg_list(program[4], "creg")
        self.verify_distinct([program[2]])
        # self.verify_distinct([program[4]])
        # if len(program[2]) != len(program[4])+2:
        #     raise QasmError('Error')
