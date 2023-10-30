#2.1.1
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
           
def remove_duplicados(t):
    # Remove tuplos iguais de dentro de um tuplo 
    result = []
    for item in t:
        if item not in result:
            result.append(item)
    return result

def ordena_intersecoes(t):
    tup = remove_duplicados(t)
    tup_ordenado = sorted(tup, key = lambda x: (x[1], x[0]))
    return tuple(tup_ordenado)   
   
#2.1.2     
def cria_pedra_branca():
    return 0

def cria_pedra_preta():
    return 1

def cria_pedra_neutra():
    return 2

def eh_pedra(arg):
    if arg == 0 or arg == 1 or arg == 2:
        return True
    else:
        return False

def eh_pedra_branca(p):
    if p == 0:
        return True
    else:
        return False
    
def eh_pedra_preta(p):
    if p == 1:
        return True
    else:
        return False    

def pedras_iguais(p1, p2):
    if eh_pedra(p1) and eh_pedra(p2):
        if p1 == p2:
            return True
        else:
            return False

def pedra_para_str(p):
        if p == 0:
            return 'O'
        elif p == 1:
            return 'X'
        else:
            return '.'

def eh_pedra_jogador(p):
    if p == 0 or p == 1:
        return True
    else:
        return False

#2.1.3
def cria_goban_vazio_9(n):

    territorio = '  '
    a = n
    a_2 = a 
    
    i = 0
    # Adiciona letras de coluna ao território, uma ou mais colunas
    if n > 1:
        while i < n:
            territorio += ' ' + ''.join([chr(65+i)])
            i += 1              
        territorio += '\n' + ' ' + ''.join(str(a)) + ' '
    i = 0    
    # Adiciona linhas do meio para uma ou mais colunas
    while a > 1:
        while i < n:
            if n > 1:
                territorio += ''.join('.') + ' '
                i +=1
            else:
                if a_2 == a:
                    territorio += ''.join('.') 
                    i +=1                                         
        territorio += ' ' + ''.join(str(a)) + '\n'
        a = a - 1 
        territorio +=' ' + ''.join(str(a)) + ' '
        i = 0

    while i < n:
        territorio += ' '.join('.') + ' '
        i +=1
    territorio += ' ' + ''.join(str(a)) + '\n' + '   ' 
    
    i = 0
    # Adiciona letras de coluna na parte inferior
    while i < n-1:
        territorio += ' '.join([chr(65+i)]) + ' ' 
        i += 1
    territorio += ' '.join([chr(65+i)]) 

    return territorio    

def cria_goban_vazio_13_19(n):

    territorio = '  '
    b, a = n, n
    a_2 = a 

    i = 0
 
    # Adiciona letras de coluna ao território, uma ou mais colunas
    if n > 1:
        while i < n:
            territorio += ' ' + ''.join([chr(65+i)]) # Adiciona letras das colunas (A, B, C, etc.)
            i += 1  
        if a >= 10:
            territorio += '\n' + '' + ''.join(str(a)) + ' '
        else:    
            territorio += '\n' + ' ' + ''.join(str(a)) + ' '    
    i = 0
   # Adiciona linhas do meio para uma ou mais colunas
    while a > 1:
        while i < n:
                    if n > 1:
                        territorio += ''.join('.') + ' '
                        i +=1                       
                    else:
                        if a_2 == a:
                            territorio += ''.join('.') 
                            i +=1                      
                        else:
                            territorio += ''.join('.') + ' '
                            i +=1     
        if b == a:
            territorio += ' ' + ''.join(str(a)) + '\n'             
        elif a >= 10:
            territorio += ' ' + ''.join(str(a)) + '\n'
        else:    
            territorio += ' ' + ''.join(str(a)) + '\n'
        a = a - 1 # Reduz o número de colunas para a próxima linha
        if a >= 10:
            territorio +='' + ''.join(str(a)) + ' '
        else:
            territorio +=' ' + ''.join(str(a)) + ' '
        i = 0
 
    while i < n:
        territorio += ' '.join('.') + ' '
        i +=1
    territorio += ' ' + ''.join(str(a)) + '\n' + '   ' 
    
    i = 0
    # Adiciona letras de coluna na parte inferior
    while i < n-1:
            territorio += ' '.join([chr(65+i)]) + ' ' 
            i += 1
    territorio += ' '.join([chr(65+i)]) 
    return territorio        

def cria_goban_vazio(n):
    if n != 9 and n != 13 and n != 19:
        raise ValueError('cria_goban_vazio: argumento invalido')
    if n == 9:
        return cria_goban_vazio_9(n)
    else:
        return cria_goban_vazio_13_19(n)        

def cria_goban_9(n, ib, ip):
    #Cria um tabuleiro de Go de dimensões nxn em que ib representa um tuplo com as cooredenadas das pessas brancas que devem ser representadas por "O" e ip representa um tuplo com as cooredenadas das pessas pretas que devem ser representadas por "X", as outras coordenadas devem ser representadas por ".". 
    
    territorio = '  '
    a = n
    i = 0

    while i < n:
        territorio += ' ' + ''.join([chr(65+i)])
        i += 1              
    territorio += '\n' + ' ' + ''.join(str(a)) + ' '
    i = 0

    while a > 1:
        while i < n:
            if (chr(65+i), a) in ib:
                territorio += ''.join('O') + ' '
                i +=1
            elif (chr(65+i), a) in ip:
                territorio += ''.join('X') + ' '
                i +=1
            else:        
                territorio += ''.join('.') + ' '
                i +=1
        territorio += ' ' + ''.join(str(a)) + '\n'
        a = a - 1 
        territorio +=' ' + ''.join(str(a)) + ' '
        i = 0  
    while i < n:
        if (chr(65+i), a) in ib:
            territorio += ''.join('O') + ' '
            i +=1
        elif (chr(65+i), a) in ip:
            territorio += ''.join('X') + ' '
            i +=1
        else:        
            territorio += ''.join('.') + ' '
            i +=1
    territorio += ' ' + ''.join(str(a)) + '\n' + '   '

    i = 0                  
    # Adiciona letras de coluna na parte inferior
    while i < n-1:
        territorio += ' '.join([chr(65+i)]) + ' ' 
        i += 1
    territorio += ' '.join([chr(65+i)]) 

    return territorio    

def cria_goban_13_19(n,ib,ip):
    territorio = '  '
    b, a = n, n

    i = 0
    while i < n:
        territorio += ' ' + ''.join([chr(65+i)]) # Adiciona letras das colunas (A, B, C, etc.)
        i += 1  
    if a >= 10:
        territorio += '\n' + '' + ''.join(str(a)) + ' '
    else:    
        territorio += '\n' + ' ' + ''.join(str(a)) + ' '

    i = 0
    while a > 1:
        while i < n:
            if (chr(65+i), a) in ib:
                territorio += ''.join('O') + ' '
                i +=1
            elif (chr(65+i), a) in ip:
                territorio += ''.join('X') + ' '
                i +=1    
            else:
                territorio += ''.join('.') + ' '
                i +=1
        if b == a:
            territorio += ' ' + ''.join(str(a)) + '\n'             
        elif a >= 10:
            territorio += ' ' + ''.join(str(a)) + '\n'
        else:    
            territorio += ' ' + ''.join(str(a)) + '\n'
        a = a - 1 # Reduz o número de colunas para a próxima linha
        if a >= 10:
            territorio +='' + ''.join(str(a)) + ' '
        else:
            territorio +=' ' + ''.join(str(a)) + ' '
        i = 0 

    while i < n:
        if (chr(65+i), a) in ib:
            territorio += ''.join('O') + ' '
            i +=1
        elif (chr(65+i), a) in ip:
            territorio += ''.join('X') + ' '
            i +=1    
        else:
            territorio += ''.join('.') + ' '
            i +=1
    territorio += ' ' + ''.join(str(a)) + '\n' + '   ' 

    i=0
    while i < n-1:
        territorio += ' '.join([chr(65+i)]) + ' ' 
        i += 1
    territorio += ' '.join([chr(65+i)]) 

    return territorio        

def cria_goban(n, ib, ip):
    if n != 9 and n != 13 and n != 19:
        raise ValueError('cria_goban: argumento invalido')
    # Verificar se algum dos membros de ib ou ip não é um tuplo
    if not all(isinstance(x, tuple) for x in ib) or not all(isinstance(x, tuple) for x in ip):
        raise ValueError('cria_goban: argumento invalido')

    if n == 9:
        return cria_goban_9(n, ib, ip)
    else:
        return cria_goban_13_19(n, ib, ip)

def cria_copia_goban(t):
    copia_goban = t
    return copia_goban

def obtem_ultima_intersecao(g):
    # Devolve a interseção que corresponde ao canto superior direito do goban g
    if '19' in g:
        return ('S', 19)
    elif '13' in g:
        return ('M', 13)
    else:
        return ('I', 9)

def obtem_pedra(g, i):
    # Divide o tabuleiro em linhas com uma lista
    linhas = g.split('\n')[1:-1] 

    # Remove espaços em branco e números no início e no final das linhas
    linhas_limpas = [linha[3:-3].replace(' ', '') for linha in linhas] 

    # Cria uma lista de listas a partir das linhas
    tabuleiro = [list(linha) for linha in linhas_limpas]

    # Converte a coordenada para números de acordo com a lista: tabuleiro
    numero_linha = len(tabuleiro) - (int(i[1]) - 1) - 1  
    numero_coluna = ord(i[0]) - 65

    # Verifica se a coordenada está dentro do tabuleiro
    if 0 <= numero_linha < len(tabuleiro) and 0 <= numero_coluna < len(tabuleiro[0]):
        intersecao = tabuleiro[numero_linha][numero_coluna]

        if intersecao == '.':
            return 2  # Interseção vazia
        elif intersecao == 'X':
            return 1  # Pedra preta
        elif intersecao == 'O':
            return 0  # Pedra branca
        else:
            raise ValueError('obtem_pedra: argumento invalido')
    else:
        raise ValueError('obtem_pedra: argumento invalido')

def obtem_cadeia(g, i):
    # Devolve a tupla formada pelas interseções da cadeia que passa pela interseção i
    tipo_pedra = obtem_pedra(g, i)
    dimensoes = obtem_ultima_intersecao(g)

    visitados = set()
    cadeia = set()
    pilha = [i]

    while pilha:
        intersecao = pilha.pop() # Retira a interseção do topo da pilha
        if intersecao not in visitados:
            visitados.add(intersecao) # Marca a interseção como visitada
            if obtem_pedra(g, intersecao) == tipo_pedra:
                cadeia.add(intersecao)
                # Adiciona as interseções adjacentes à pilha para continuar a busca
                adjacentes = obtem_intersecoes_adjacentes(intersecao, dimensoes)
                pilha.extend(adjacentes)

    return tuple(ordena_intersecoes(cadeia))

def coloca_pedra(g, i, p):
    # Divide o tabuleiro em linhas com uma lista
    linhas = g.split('\n')[1:-1] 

    # Remove espaços em branco e números no início e no final das linhas
    linhas_limpas = [linha[3:-3].replace(' ', '') for linha in linhas] 

    # Cria uma lista de listas a partir das linhas
    tabuleiro = [list(linha) for linha in linhas_limpas]

    # Converte a coordenada para números de acordo com a lista: tabuleiro
    numero_linha = len(tabuleiro) - (int(i[1]) - 1) - 1  
    numero_coluna = ord(i[0]) - 65

    if eh_intersecao(i) and eh_pedra(p) and 0 <= numero_linha < len(tabuleiro) and 0 <= numero_coluna < len(tabuleiro[0]):
        if p == 0:
            tabuleiro[numero_linha][numero_coluna] = 'O'
        elif p == 1:
            tabuleiro[numero_linha][numero_coluna] = 'X'
        else:
            tabuleiro[numero_linha][numero_coluna] = '.'

    n = len(tabuleiro)
    ib = []
    ip = []
    for linha in range(n):
        for coluna in range(n):
            if tabuleiro[linha][coluna] == 'O':
                ib.append((chr(65 + coluna), n - linha))
            elif tabuleiro[linha][coluna] == 'X':
                ip.append((chr(65 + coluna), n - linha))

    return cria_goban(n, ib, ip)

def remove_pedra(g, i):
    pedra_i = obtem_pedra(g, i)
    if pedra_i == 2:
        return g
    else:
        return coloca_pedra(g, i, 2)

def remove_cadeia(g, t):
    pecas_a_remover = list(t)
    for i in pecas_a_remover:
        g = remove_pedra(g, i)
    return g

def eh_goban(arg):
    #devolve True caso o seu argumento seja um TAD goban e False caso contrario.
    linhas = [linha.split() for linha in arg.strip().split('\n')]
    num_colunas = len(linhas[0])
    tamanho_valido = [9, 13, 19]

    if (
        not isinstance(arg, str) or
        len(linhas) < 3 or
        len(linhas) > 21 or
        num_colunas not in tamanho_valido
        ):
        return False

    for linha in linhas[1:-1]:
        if len(linha) - 2 != num_colunas:
            return False
        for char in linha[1:-1]:
            if char not in 'XO.':
                return False

    return True                

def eh_intersecao_valida(g, i):
    pedra_i = obtem_pedra(g, i)
    if pedra_i == 2:
        return True
    else:
        return False
    
def gobans_iguais(g1, g2):
    if eh_goban(g1) and eh_goban(g2) and g1 == g2:
        return True
    else:
        return False
    
def goban_para_str(g):
    return g

def obtem_territorios(g):
    territorios = []  # Alterei para uma lista em vez de uma tupla
    dimensoes = obtem_ultima_intersecao(g)  # Obtenha as dimensões do tabuleiro

    # Divide o tabuleiro em linhas com uma lista
    linhas = g.strip().split('\n')[1:-1]

    # Remova espaços em branco e números no início e no final das linhas
    linhas_limpas = [linha[3:-3].replace(' ', '') for linha in linhas]

    # Crie uma lista de listas a partir das linhas
    tabuleiro = [list(linha) for linha in linhas_limpas]

    visitados = set()  # Crie um conjunto para rastrear interseções já visitadas

    for linha_num, linha in enumerate(tabuleiro):
        for coluna_num, intersecao in enumerate(linha):
            coordenada = (chr(coluna_num + 65), dimensoes[1] - linha_num)

            if intersecao != '.' and coordenada not in visitados:
                cadeia = obtem_cadeia(g, coordenada)
                territorios.append(cadeia)
                visitados.update(cadeia)

    return ordena_intersecoes(territorios)



 

    



