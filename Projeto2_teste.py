def cria_intersecao(col, lin):
    col = col.strip()

    if (
        not isinstance(col, str) or 
        not isinstance(lin, int) or 
        not col.isupper() or 
        col not in 'ABCDEFGHIJKLMNOPGRS' or
        lin not in range(1, 20)
        ):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return(col,lin)
    
def obtem_col(i):
    return(i[0])

def obtem_lin(i):
    return(i[1])

def intersecao(arg):
    if (
        arg is None or
        not isinstance(arg, tuple) or
        len(arg) != 2 or
        not isinstance(arg[1], int) or
        not isinstance(arg[0], str) or
        isinstance(arg[1], bool) or
        isinstance(arg[0], bool) or
        not arg[0].strip().isalpha() or 
        not arg[0].strip().isupper() or
        len(arg[0]) != 1 or
        arg[1] > 19 or
        arg[1] < 1 
        ):
        return False
    else:
        return True
    
def eh_intersecao(arg):
    return intersecao(arg)

def intersecoes_iguais(i1, i2): 
    if intersecao(i1) and intersecao(i2):
        if i1 == i2:
            return True
        else:
            return False
    
def intersecao_para_str(i):
    return(i[0] + str(i[1]))  
 
def str_para_intersecao(s):
    col = s[0]
    lin = int(s[1:])
    return cria_intersecao(col, lin)

def obtem_intersecoes_adjacentes(i, l):
    max_col = l[0]
    max_lin = l[1]
    resultado = ()
    #Vê se há interseções adjacentes em baixo
    if i[1] > 1:
        resultado += ((i[0], i[1]-1),)
    #Vê se há interseções adjacentes à esquerda
    if i[0] != 'A':
        resultado += ((chr(ord(i[0])-1), i[1]),) 
    #Vê se há interseções adjacentes à direita
    if i[0] != max_col:
        resultado += ((chr(ord(i[0])+1), i[1]),)
     #Vê se há interseções adjacentes em cima
    if i[1] < max_lin: 
        resultado += ((i[0], i[1]+1),)  
         
    return resultado              




