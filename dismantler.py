#importando funções que formatam as instruções nos formatos de instruções r e i, e uma função
#que transforma o texto em hexadecimal em uma instrução binaria de 32 bits e dicionario
#que contem a relação de uma função em hexadecimal com seu nome em assembly

#importing functions to format hexadecimal like text in binary 32 bits instructions and 
#a dictionary whit each function code related to their name


from dictionary import instruct_r, instruct_j, instruct_i, reg
from format import format_inst_r, format_inst_i, text_to_binary


#lendo o arquivo texto e salvando suas linhas em uma lista de strings

#reading text file and filling a list whit his lines
with open('hex.txt', 'r') as f:
    lines = f.readlines()


#criando uma lista para armazenar cada binario convertido do
#arquivo texto

#list to store text file lines as binary 


final_txt = ''
label_counter = 0


#lendo linha a linha do texto

#reading each line
for line in lines:
    first2_chars = line[0:2]


#verificando se a string line está vazia e se os dois primeiros
#caracteres são '0x' indicando que é uma linha de codigo hexadecimal




    if line and first2_chars == '0x':


#convertendo o numero para decimal e armazenando na lista usando uma
#substring da linha que começa após o 0x

#converting decimal number and storing in a list


        inst_hex = line[2:].replace('\n' ,'')
        binary = text_to_binary(inst_hex)
    op = binary[:6] 
    if op == '000000':
#formatando os binarios para uma instrução do tipo r e
#relacionando aos valores no dicionario

#formating binarys as type r instruction and searching his key 
#in the dictionary

        inst_r = format_inst_r(binary)
        rs_decimal = int(inst_r[0],2)
        rt_decimal = int(inst_r[1],2)
        rd_decimal = int(inst_r[2],2)
        shamt = inst_r[3]
        func = inst_r[4]
        rs_txt = reg.get(rs_decimal)
        rt_txt = reg.get(rt_decimal)
        rd_txt = reg.get(rd_decimal)
        func_txt = instruct_r.get(func)
        final_txt += (func_txt + ' ' + rd_txt + ', ' + rs_txt + ', ' + rt_txt)
    
#instrução do tipo J

#type j instruction

    elif op =='000010':
        address = binary[6:]
        func = op
        func_txt = instruct_j.get(func)
        address_hex = hex(int(address,2))
        final_txt += (func_txt + ' label_' + str(label_counter))
        label_counter +=1

#se a instrução não se encaixa no tipo R nem no tipo J ela é uma
#instrução de tipo I onde o OP difere para cada uma

#type i where op code is different for every instruction
    else:
        inst_i = format_inst_i(binary)
        rs_decimal = inst_i[0]
        rt_decimal = inst_i[1]
        immediate_hexa = inst_i[2]
        rs_txt = (reg.get(rs_decimal))
        rt_txt = (reg.get(rt_decimal))
        func = op
        func_txt = (instruct_i.get(func))
        if func == '000100' or func == '000101':
            final_txt += (func_txt + ' ' + rs_txt + ', ' + rt_txt + ', label_' + str(label_counter))
            label_counter +=1
        else:
            final_txt += (func_txt + ' ' + rt_txt + ', ' + rs_txt + ', ' + immediate_hexa)
    final_txt +='\n'

#criando um contador para o numero de labels que existem no codigo
#para cima soma 1 pra baixo subtrai 1

#label counter - going up add 1 - going down subtract 1
label_counter = 0
for line in lines:
    first2_chars = line[0:2]
#verificando se a string line está vazia e se os dois primeiros
#caracteres são '0x' indicando que é uma linha de codigo hexadecimal
    if line and first2_chars == '0x':
#convertendo o numero para decimal e armazenando na lista usando uma
#substring da linha que começa após o 0x
        inst_hex = line[2:].replace('\n' ,'')
        binary = text_to_binary(inst_hex)
#if para contar os jumps

#couting jumps
    op = binary[:6]
    if op =='000010':
        address = binary[6:]
        line_index = int(address,2)
        line_index = line_index - 1048576 
#valor decimal para posição 0 em binario
        line_list = final_txt.split('\n')
        for i in range(0, len(line_list)):
            if i == line_index:
                line_list[i] = 'label_' + str(label_counter) + ':\n' + line_list[i]
                label_counter += 1 
                break
        final_txt = ''
        for l in line_list:
            final_txt += l + '\n'
    elif op == '000100' or op == '000101':
       branch_counter = inst_hex[3:]
       line_list = final_txt.split('\n')
       j_lines = 0
       if inst_hex[5:7] != 'ff': 
#verificando se é um numero hexadeximal negativo

#looking for hexadeximals < 0
            j_lines = j_lines + int(inst_hex[7:],16) + 1 
            for l in line_list:
                if 'beq' in l or 'bne' in l:
                    line_list[line_list.index(l) + j_lines] = 'label_' + str(label_counter) + ':\n' + line_list[line_list.index(l) + j_lines]
                    label_counter += 1
                    break
            final_txt = ''
            for l in line_list:
                final_txt += l + '\n'
#caso esteja pulando para baixo

#if going down
       else:
            j_lines = 15 - (int(inst_hex[7:],16)) + 1
            for l in line_list:
                if 'beq' in l:
                    line_list[line_list.index(l) - j_lines] = 'label_' + str(label_counter) + ':\n' + line_list[line_list.index(l) - j_lines]
                    label_counter += 1
                    break
            final_txt = ''
            for l in line_list:
                final_txt += l + '\n'
#caso esteja pulando para cima

#if going up


#escrevendo o algoritmo em assembly em um novo arquivo

#writing assembly algorithm in a new file
with open('assembly.txt', 'w') as f2:
    f2.write(final_txt)
