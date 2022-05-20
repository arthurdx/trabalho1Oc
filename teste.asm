loop:
addi $t2,$zero, 0x1
bne $t2, $zero, pula
pula:
addi $t0,$t1, 0x2
ori $t0,$zero, 0x1
ori $t1,$zero, 0x1
j loop