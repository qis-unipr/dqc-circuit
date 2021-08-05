OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
creg c1[1];
creg c2[1];
creg c3[1];
creg c4[1];

epr q[0], q[5];
epr q[2], q[1];
entswap q[0],q[5],q[2],q[1];
remoteCx q[0],q[3],q[2],q[1];

