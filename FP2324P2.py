# This is the Python script for your project

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
    return(str(i[0]))

def obtem_lin(i):
    return(int(i[1]))

def eh_intersecao(arg):
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

def intersecoes_iguais(i1, i2): 
    if eh_intersecao(i1) and eh_intersecao(i2) and i1 == i2:      
        return True
    return False

def intersecao_para_str(i):
    return (i[0] + str(i[1]))  

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

def ordena_intersecoes(t):
    def remove_duplicados(t):
        # Remove tuplos iguais de dentro de um tuplo 
        result = []
        for item in t:
            if item not in result:
                result.append(item)
        return result

    if isinstance(t, set):
        t = tuple(t)

    if len(t) == 1:
        t = t[0]

    for x in t:
        if not isinstance(x, tuple):
            return t 

    tup = remove_duplicados(t)
    tup_ordenado = sorted(tup, key = lambda x: (x[1], x[0]))

    return tuple(tup_ordenado)   

def cria_pedra_branca():
    return 0

def cria_pedra_preta():
    return 1

def cria_pedra_neutra():
    return 2

def eh_pedra(arg):
    if arg == 0 or arg == 1 or arg == 2:
        return True
    return False

def eh_pedra_branca(p):
    if p == 0:
        return True
    return False
    
def eh_pedra_preta(p):
    if p == 1:
        return True
    return False    

def pedras_iguais(p1, p2):
    if eh_pedra(p1) and eh_pedra(p2) and p1 == p2:
        return True
    return False

def pedra_para_str(p):
    # Converte uma pedra num caracter
    # Retorna 'O', 'X' ou '.'

    if not isinstance(p, int) or p not in [0, 1, 2]:
        raise ValueError('pedra_para_str: argumento invalido')
    else:
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

def cria_goban_vazio(n):
    #Cria uma lista de listas de tamanho n x n com o caracter '.'9 ou 13 ou 19 vezes dentro de cada lista
    if n == 9 or n == 13 or n == 19:
        goban = []
        for i in range(n):
            goban.append([2] * n)
        return goban 
    else:
        raise ValueError("cria_goban_vazio: argumento invalido")    

def cria_goban(n, ib, ip):
    if n == 9 or n == 13 or n == 19:
        goban = cria_goban_vazio(n)
        if len(ib) > 1 and isinstance(ib[0], tuple):
            for i in range(len(ib)):            
                goban[(n-1) - (ib[i][1] - 1)][ord(ib[i][0])-65] = 0
        else:
            goban[(n-1) - (ib[1] - 1)][ord(ib[0]) - 65] = 0
        if len(ip) > 1 and isinstance(ip[0], tuple):            
            for i in range(len(ip)):    
                goban[(n-1) - (ip[i][1] - 1)][ord(ip[i][0])-65] = 1
        else:
            goban[(n-1) - (ip[1] - 1)][ord(ip[0]) - 65] = 1
        return goban

def cria_copia_goban(t):
    copia_goban = t
    return copia_goban

def obtem_ultima_intersecao(g):

    if not isinstance(g, list) or len(g) == 0:
        raise ValueError('obtem_ultima_intersecao: argumentos invalidos')
    else:
        col = len(g[0])
        lin = len(g)
        return cria_intersecao(chr(col + 64), lin)

def obtem_pedra(g, i):
    if not isinstance(g, list) or not isinstance(i, tuple) or len(g) == 0 or len(i) != 2:
        raise ValueError('obtem_pedra: argumentos invalidos')
    else:
        col = ord(i[0]) - 65
        lin = (len(g) - 1) - (i[1] - 1)
        if g[lin][col] == 2:
            return 2
        elif g[lin][col] == 0:
            return 0
        elif g[lin][col] == 1:
            return 1

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
    # Verifica se os argumentos são válidos
    # Modifica destrutivamente o goban g colocando a pedra do jogador p na intersecao i
    # Retorna o g modificado

    if (
        not isinstance(g, list) or
        not isinstance(i, tuple) or
        not isinstance(p, int) or
        len(g) == 0 or len(i) != 2 or
        p not in [0, 1]
        ):
        raise ValueError('coloca_pedra: argumento invalido')
    else:
        col = ord(i[0]) - 65
        lin = (len(g) - 1) - (i[1] - 1)
        if g[lin][col] == 2:
            g[lin][col] = p
            return g
        else:
            return g

def remove_pedra(g, i):
    # Verifica se os argumentos são válidos
    # Modifica destrutivamente o goban g removendo a pedra da intersecao i
    # Retorna o g modificado

    if (
        not isinstance(g, list) or
        not isinstance(i, tuple) or
        len(g) == 0 or len(i) != 2
        ):
        raise ValueError('remove_pedra: argumento invalido')
    else:
        col = ord(i[0]) - 65
        lin = (len(g) - 1) - (i[1] - 1)
        if g[lin][col] == 0 or g[lin][col] == 1:
            g[lin][col] = 2
            return g
        else:
            raise ValueError('remove_pedra: argumento invalido')

def remove_cadeia(g, t):
    if (
        not isinstance(g, list) or
        not isinstance(t, tuple) or
        not all(isinstance(coord, tuple) and len(coord) == 2 for coord in t)
    ):
        raise ValueError('remove_cadeia: argumento invalido')

    rows = len(g)
    cols = len(g[0])

    for coord in t:
        col = ord(coord[0]) - ord('A')
        row = rows - coord[1]

        if col < 0 or col >= cols or row < 0 or row >= rows:
            raise ValueError('remove_cadeia: argumento invalido')

        if g[row][col] not in (0, 1):
            raise ValueError('remove_cadeia: argumento invalido')

    for coord in t:
        col = ord(coord[0]) - ord('A')
        row = rows - coord[1]
        g[row][col] = 2

    return g

def eh_goban(arg):
    # Verifica se o argumento é um goban válido
    # Retorna True ou False

    if not isinstance(arg, list) or len(arg) == 0:
        return False
    return True                

def eh_intersecao_valida(g, i):
    # Verifica se a intersecao i é válida no goban g
    # Retorna True ou False

    if (
        not isinstance(g, list) or
        not isinstance(i, tuple) or
        len(g) == 0 or len(i) != 2
        ):
        return False
    else:
        col = ord(i[0]) - 65
        lin = (len(g) - 1) - (i[1] - 1)
        if col < 0 or col >= len(g[0]) or lin < 0 or lin >= len(g):
            return False
        else:
            return True

def gobans_iguais(g1, g2):
    # Verifica se os gobans g1 e g2 são iguais
    # Retorna True ou False

    if (
        not isinstance(g1, list) or
        not isinstance(g2, list) or
        len(g1) != len(g2) or
        len(g1) == 0  # Também verificamos se ambos têm pelo menos uma linha
    ):
        return False
    else:
        for i in range(len(g1)):
            if len(g1[i]) != len(g2[i]):
                return False  # Verifica se o número de colunas é o mesmo em cada linha
            for j in range(len(g1[i])):
                if g1[i][j] != g2[i][j]:
                    return False
        return True

def goban_para_str(g):
    # Converte um goban em uma string no formato especificado

    if not isinstance(g, list) or len(g) == 0:
        raise ValueError('goban_para_str: argumento inválido')
    elif len(g) == 9:
        str_goban = '   ' + ' '.join([chr(i + 65) for i in range(len(g[0]))]) + '\n'
        for i in range(len(g)):
            str_goban += ' ' + str(len(g) - i) + ' '
            for j in range(len(g[i])):
                if g[i][j] == 0:
                    str_goban += 'O '
                elif g[i][j] == 1:
                    str_goban += 'X '
                elif g[i][j] == 2:
                    str_goban += '. '
            str_goban += ' ' + str(len(g) - i) + '\n'  # Remova o espaço extra aqui
        str_goban += '   ' + ' '.join([chr(i + 65) for i in range(len(g[0]))])
        return str_goban
    
    else:
        territorio = '  '
        n = len(g)
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
                if obtem_pedra(g, (chr(65+i), a)) == 0:
                    territorio += ''.join('O') + ' '
                    i +=1
                elif obtem_pedra(g, (chr(65+i), a)) == 1:
                    territorio += ''.join('X') + ' '
                    i +=1    
                else:
                    territorio += ''.join('.') + ' '
                    i +=1
            if b == a:
                territorio += ''.join(str(a)) + '\n'             
            elif a >= 10:
                territorio += ''.join(str(a)) + '\n'
            else:    
                territorio += ' ' + ''.join(str(a)) + '\n'
            a = a - 1 # Reduz o número de colunas para a próxima linha
            if a >= 10:
                territorio +='' + ''.join(str(a)) + ' '
            else:
                territorio +=' ' + ''.join(str(a)) + ' '
            i = 0 
        while i < n:
            if obtem_pedra(g, (chr(65+i), a)) == 0:
                territorio += ''.join('O') + ' '
                i +=1
            elif obtem_pedra(g, (chr(65+i), a)) == 1:
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

def vizinhas(i, j):
    # Esta função retorna as coordenadas das interseções vizinhas
    # a partir das coordenadas (i, j).
    return [
        (i - 1, j),  # Interseção acima
        (i + 1, j),  # Interseção abaixo
        (i, j - 1),  # Interseção à esquerda
        (i, j + 1),  # Interseção à direita
    ]

def busca_territorio(i, j, terr, g):
            if (
                i < 0 or i >= len(g) or
                j < 0 or j >= len(g[0]) or
                g[i][j] != 2
            ):
             return
            

            terr.add((chr(j + 65), len(g) - i))
            g[i][j] = 3  # Marca a interseção como visitada

            for ni, nj in vizinhas(i, j):
                busca_territorio(ni, nj, terr, g)

def obtem_territorios(g):
    def obtem_territorios_vazios(g):
        
        territorios = []
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j] == 2:
                    terr = set()
                    busca_territorio(i, j, terr, g)
                    if terr:
                        territorios.append(tuple(sorted(terr)))
    
        # Restaura o estado original das interseções
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j] == 3:
                    g[i][j] = 2

        return tuple(sorted(territorios, key=lambda terr: (terr[0][1], terr[0][0])))

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


    possiveis_territorios = obtem_territorios_vazios(g)
    dimensoes = obtem_ultima_intersecao(g)
    caixa_1 = set()
    caixa_2 = ()
    caixa_pedras= set()
    caixa_pedras_2 = ()
    caixa_final = ()
    ii = -1
    i=0

    for territorios in possiveis_territorios:
        i += 1
        for intersecao in territorios:
            if obtem_intersecoes_adjacentes(intersecao, dimensoes) not in caixa_1:
                adjacente = obtem_intersecoes_adjacentes(intersecao, dimensoes)
                for x in adjacente:
                    if x not in caixa_1:
                        caixa_1.add(x)
        caixa_2 +=(caixa_1,)
        caixa_1 = set()
        

    # Converter os elementos dentro da caixa para as suas respetivas pedras, 2, 0 ou 1
    for tuplos in caixa_2:
        for elementos in tuplos:
            caixa_pedras.add(obtem_pedra(g, elementos))
        caixa_pedras_2 += (caixa_pedras,)
        caixa_pedras = set()    

    for tuplos in caixa_pedras_2:
        ii += 1
        if all(x in [0,2] for x in tuplos) or all(x in [0,1] for x in tuplos):
            caixa_final += ((possiveis_territorios[ii]),)

    resultado = ((ordena_intersecoes(caixa_final)),)  

    return resultado

def obtem_adjacentes_diferentes(g, t):
    # Verifica se os argumentos são válidos
    #devolve o tuplo ordenado formado pelas interseoes adjacentes as intersecoes do tuplo t:
    #(a) livres, se as intersecoes do tuplo t estao ocupadas por pedras de jogador
    #(b) ocupadas por pedras de jogador, se as intersecoes do tuplo t estao livres
    #(a) corresponde as liberdades de uma cadeia de pedras,enquanto que (b) corresponde a fronteira de um territorio.

    if (
        not isinstance(g, list) or
        not isinstance(t, tuple) 
    ):
        raise ValueError('obtem_adjacentes_diferentes: argumento invalido')
    elif isinstance(t[0], tuple): 
        if not all(isinstance(coord, tuple) and len(coord) == 2 for coord in t):
            raise ValueError('obtem_adjacentes_diferentes: argumento invalido')

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

    resultado = set()

    for intersecoes in t:
        if obtem_pedra(g, intersecoes) != 2:
            intersecoes_pedras = obtem_intersecoes_adjacentes(intersecoes, obtem_ultima_intersecao(g))
            for intersecao in intersecoes_pedras:
                if obtem_pedra(g, intersecao) == 2:
                    resultado.add(intersecao)
        else:
            intersecoes_livres = obtem_intersecoes_adjacentes(intersecoes, obtem_ultima_intersecao(g))
            for intersecao in intersecoes_livres:
                if obtem_pedra(g, intersecao) != 2:
                    resultado.add(intersecao)

    return ordena_intersecoes(resultado) 

def jogada(g, i, p):
    if eh_intersecao_valida(g, i) and p in [0, 1]:
        g = coloca_pedra(g, i, p)
    else:
        raise ValueError('jogada: argumentos inválidos')

    cadeia = set()
    caixa_pedras= set()
    caixa_pedras_2 = ()  
    cadeia_remover = () 

    cadeias_adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))

    for tuplos in cadeias_adjacentes:
        caixa_pedras.add(obtem_pedra(g, tuplos))
        caixa_pedras_2 += (caixa_pedras,)
        caixa_pedras = set()
    for x in caixa_pedras_2:
        if all(set([0]) == i for i in caixa_pedras_2) or all(set([1]) == i for i in caixa_pedras_2):
            return g

    caixa_pedras_2 = ()

    for x in cadeias_adjacentes:
        pedra = obtem_pedra(g, x)
        if obtem_pedra(g, x) != 2:
            cadeia_remover = obtem_cadeia(g, x)
            for ts in cadeia_remover:
                if not isinstance(ts, tuple):
                    cadeia_remover = (cadeia_remover,)
                    break
            elementos = obtem_cadeia(g, x)
            for t in elementos:
                if not isinstance(t, tuple):
                    elementos = (elementos,)
                    break
            for ele in elementos:
                triagem = obtem_intersecoes_adjacentes(ele, obtem_ultima_intersecao(g))
                for tuplos in triagem:
                    if obtem_pedra(g, tuplos) != 2 and obtem_pedra(g, tuplos) != pedra:
                        cadeia.add(tuplos)
                
            for elemento in cadeia:
                pedra = obtem_pedra(g, x)

                for tuplos in cadeia:
                    caixa_pedras.add(obtem_pedra(g, tuplos))
                    caixa_pedras_2 += (caixa_pedras,)
                    caixa_pedras = set()  

                if pedra == 1:
                    if all(set([0]) == i for i in caixa_pedras_2):
                        if len(cadeia_remover) == 1:
                            g = remove_pedra(g, x)
                            return g
                        elif len(cadeia_remover) > 1:    
                            g = remove_cadeia(g, cadeia_remover)
                            return g 
                elif pedra == 0:
                    #Vê se todos os elementos em caixa_pedras_2 são 1
                    if all(set([1]) == i for i in caixa_pedras_2):
                        if len(cadeia_remover) == 1:
                            g = remove_pedra(gn, x)
                            return g
                        elif len(cadeia_remover) > 1:    
                            g = remove_cadeia(g, cadeia_remover)
                            return g    
    return g        
                              
def obtem_pedras_jogadores(g):
    
    pedras_brancas = 0
    pedras_pretas = 0

    for linha in g:
        for intersecao in linha:
            if intersecao == 0:  #  0 represente uma pedra branca
                pedras_brancas += 1
            elif intersecao == 1:  #  1 represente uma pedra preta
                pedras_pretas += 1

    return (pedras_brancas, pedras_pretas)

def calcula_pontos(g):

    pontos_j_b = obtem_pedras_jogadores(g)[0]
    pontos_j_p = obtem_pedras_jogadores(g)[1]
    
    territorios = obtem_territorios(g)
    territorio_pertence = territorio_de_quem(g, territorios)
    
    tamanho_territorio = len(territorios[0])
    if territorio_pertence == 0:
        pontos_j_b += tamanho_territorio
    elif territorio_pertence == 1:  
        pontos_j_p += tamanho_territorio    
    return (pontos_j_b, pontos_j_p) 

def territorio_de_quem(g, territorio):
    #Descobre a quem pertence o território
    for territorios in territorio:
        for intersecao in territorios:
            adjacentes = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(g))
            for tuplos in adjacentes:
                if obtem_pedra(g, tuplos) == 0:
                    return 0
                elif obtem_pedra(g, tuplos) == 1:
                    return 1
 
def eh_jogada_legal(g, i, p, l):
    if  (
        not isinstance(g, list) or
        not isinstance(i, tuple) or
        not isinstance(p, int) or
        not isinstance(l, list) or
        len(g) == 0 or len(i) != 2 or
        p not in [0, 1]
        ):
         raise ValueError('eh_jogada_legal: argumento invalido')
    print(goban_para_str(l))
    goban_dep_jogada = coloca_pedra(cria_copia_goban(g), i, p)
    

    if not gobans_iguais(goban_dep_jogada, l):
        tipo_pedra = obtem_pedra(goban_dep_jogada, i)
        cadeia = obtem_cadeia(goban_dep_jogada, i)
        if not isinstance(cadeia[0], tuple):
            cadeia = (cadeia,)
        adjacentes = obtem_adjacentes_diferentes(goban_dep_jogada, cadeia)
        caixa_pedras = set()
        caixa_pedras_2 = ()

        for tuplos in adjacentes:
            caixa_pedras.add(obtem_pedra(goban_dep_jogada, tuplos))
            caixa_pedras_2 += (caixa_pedras,)
            caixa_pedras = set()
        if all(set([tipo_pedra]) == i for i in caixa_pedras_2):
            goban_dep_jogada = remove_pedra(goban_dep_jogada, i)
            return False    
        else:
            goban_dep_jogada = remove_pedra(goban_dep_jogada, i)
            return True
    else:
        return True 

def cria_copia_goban(g):
    import copy
    copia = copy.deepcopy(g)
    return copia