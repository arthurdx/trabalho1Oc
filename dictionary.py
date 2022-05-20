#definindo os dicionarios contendo as instruções, e os registros relacionados a seus codigos em binário

instruct_r = ({'100000': 'add',
            '100100': 'and',
            '100101':'or',
            '100010':'slt',
            '000000':'sll',
            '000010':'slr',
            '100110':'xor',
            '100010':'sub'})

instruct_j = ({
            '000010': 'j'}) 

instruct_i = ({'001000':  'addi' ,
            '001100': 'andi' ,
            '000100': 'beq' ,
            '000101':  'bne' ,
            '100011':   'lw' ,
            '001101':   'ori' ,
            '001010':   'slti' ,
            '101011':    'sw' ,
            '001110':   'xori'})

reg = ({0:'$zero',
    1:'$at', 2:'$v0',3:'$v1',
    4:'$a0', 5:'$a1', 6:'$a2',
    7:'$a3', 8:'$t0', 9:'$t1', 
    10:'$t2', 11:'$t3', 12:'$t4',
    13:'$t5', 14:'$t6', 15:'$t7',
    16:'$s0', 17:'$s1', 18:'$s2',
    19:'$s3', 20:'$s4', 21:'$s5',
    22:'$s6', 23:'$s7', 24:'$t8',
    25:'$t9', 26:'$k0', 27:'$k1',
    28:'$gp', 29:'$sp', 30:'$fp',
    31:'$ra'})