// RAM[2] = RAM[0] + RAM[1]

@0
D = M

@1
D = D + M

@2
M = D

D = D+A
@17
M = M+1

@100
D = D-1;JNE
A = D

D; JEQ
0;JMP