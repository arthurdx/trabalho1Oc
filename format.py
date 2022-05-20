#transforma um hexadecimal em formato de string e converte em um binario de 32
#bits em formato de string
def text_to_binary(hexadecimal):
    bin_len = 32
    hex_int = int(hexadecimal, 16)
    hex_bin = bin(hex_int)
    binary = hex_bin[2:].zfill(bin_len) 
    return binary

#recebe uma instrução de 32 bits em numeros binarios e divide em blocos de 
#6, 5, 5, 5, 5, 6 digitos, o formato de instruções do tipo R 
def format_inst_r(inst_bin):
    rs = inst_bin[6:11]
    rt = inst_bin[11:16]
    rd = inst_bin[16:21]
    shamt = inst_bin[21:26]
    func = inst_bin[26:]
    inst = [rs,rt,rd,shamt,func]
    return inst

#recebe uma instrução de 32 bits em numeros binarios e divide em blocos de
#de acordo com o tipo de informação que a função tipo I em especifico tem
def format_inst_i(inst_bin):
    rs = inst_bin[6:11]
    rt = inst_bin[11:16]
    immediate = inst_bin[16:]
    immediate_hexa = hex(int(immediate,2))
    rs_decimal = int(rs,2)
    rt_decimal = int(rt,2)
    inst = [rs_decimal,rt_decimal,immediate_hexa]
    return inst

