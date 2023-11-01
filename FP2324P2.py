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
    def is_valid(x, y):
        return 0 <= x < len(g) and 0 <= y < len(g[0])

    def get_neighbors(x, y):
        return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    def flood_fill(x, y, visited, color):
        visited[x][y] = True
        chain = [(chr(x + 65), y)]
        
        for nx, ny in get_neighbors(x, y):
            if is_valid(nx, ny) and not visited[nx][ny] and g[nx][ny] == color:
                chain.extend(flood_fill(nx, ny, visited, color))
        
        return chain

    x, y = ord(i[0]) - ord('A'), i[1] - 1
    if not is_valid(x, y):
        return []

    visited = [[False] * len(g[0]) for _ in range(len(g))]
    color = g[x][y]

    if color == 0:
        return []

    return ordena_intersecoes(flood_fill(x, y, visited, color))

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
            raise ValueError('coloca_pedra: argumento invalido')

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
    else:
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


def obtem_territorios_vazios(g):
    global estado_goban

    if estado_goban is None:
        estado_goban = g

    dimensoes = obtem_ultima_intersecao(estado_goban)

    # Divide o tabuleiro em linhas com uma lista
    linhas = estado_goban.strip().split('\n')[1:-1]

    # Remova espaços em branco e números no início e no final das linhas
    linhas_limpas = [linha[3:-3].replace(' ', '') for linha in linhas]

    # Crie uma lista de listas a partir das linhas
    tabuleiro = [list(linha) for linha in linhas_limpas]

    visitados = set()  # Conjunto para rastrear interseções já visitadas
    territorios = []

    def todas_adjacentes_vazias(coordenada):
        for adjacente in obtem_intersecoes_adjacentes(coordenada, dimensoes):
            if obtem_pedra(estado_goban, adjacente) != 2:  # Verifica se não é uma pedra de jogador
                return False
        return True

    for linha_num, linha in enumerate(tabuleiro):
        for coluna_num, intersecao in enumerate(linha):
            coordenada = (chr(coluna_num + 65), dimensoes[1] - linha_num)

            if intersecao == '.' and coordenada not in visitados and todas_adjacentes_vazias(coordenada):
                territorio = set()
                fila = [coordenada]

                while fila:
                    atual = fila.pop()
                    visitados.add(atual)
                    territorio.add(atual)

                    for adjacente in obtem_intersecoes_adjacentes(atual, dimensoes):
                        if obtem_pedra(estado_goban, adjacente) == 2 and adjacente not in visitados:
                            fila.append(adjacente)

                territorios.append(tuple(sorted(territorio)))

    return tuple(sorted(territorios))

def obtem_territorios(g):
    global estado_goban

    if estado_goban is None:
        estado_goban = g

    possiveis_territorios = obtem_territorios_vazios(estado_goban)
    dimensoes = obtem_ultima_intersecao(estado_goban)
    caixa_1 = set()
    caixa_2 = ()
    caixa_pedras= set()
    caixa_pedras_2 = ()
    caixa_final = ()
    i = 0
    ii = -1

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
            caixa_pedras.add(obtem_pedra(estado_goban, elementos))
        caixa_pedras_2 += (caixa_pedras,)
        caixa_pedras = set()    

    for tuplos in caixa_pedras_2:
        ii += 1
        if all(x in [0,2] for x in tuplos) or all(x in [0,1] for x in tuplos):
            caixa_final += ((possiveis_territorios[ii]),)

    resultado = ((ordena_intersecoes(caixa_final)),)  

    return resultado

def obtem_adjacentes_diferentes(g, t):
    global estado_goban

    if estado_goban is None:
        estado_goban = g

    resultado = set()

    for intersecoes in t:
        if obtem_pedra(estado_goban, intersecoes) != 2:
            intersecoes_pedras = obtem_intersecoes_adjacentes(intersecoes, obtem_ultima_intersecao(estado_goban))
            for intersecao in intersecoes_pedras:
                if obtem_pedra(estado_goban, intersecao) == 2:
                    resultado.add(intersecao)
        else:
            intersecoes_livres = obtem_intersecoes_adjacentes(intersecoes, obtem_ultima_intersecao(estado_goban))
            for intersecao in intersecoes_livres:
                if obtem_pedra(estado_goban, intersecao) != 2:
                    resultado.add(intersecao)

    return ordena_intersecoes(resultado) 

def jogada(g, i, p):
    global estado_goban

    if estado_goban is None:
        estado_goban = g

    cadeia = set()
    caixa_pedras= set()
    caixa_pedras_2 = ()  
    cadeia_remover = () 
    
    if eh_intersecao_valida(estado_goban, i):
        estado_goban = coloca_pedra(estado_goban, i, p)
    else:
        raise ValueError('jogada: argumentos invalidos')
    
    cadeias_adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(estado_goban))
    
    for tuplos in cadeias_adjacentes:
        caixa_pedras.add(obtem_pedra(estado_goban, tuplos))
        caixa_pedras_2 += (caixa_pedras,)
        caixa_pedras = set()
    for x in caixa_pedras_2:
        if all(set([0]) == i for i in caixa_pedras_2) or all(set([1]) == i for i in caixa_pedras_2):
            return estado_goban

    caixa_pedras_2 = ()

    for x in cadeias_adjacentes:
        pedra = obtem_pedra(estado_goban, x)
        if obtem_pedra(estado_goban, x) != 2:
            cadeia_remover = obtem_cadeia(estado_goban, x)
            for ts in cadeia_remover:
                if not isinstance(ts, tuple):
                    cadeia_remover = (cadeia_remover,)
                    break
            elementos = obtem_cadeia(estado_goban, x)
            for t in elementos:
                if not isinstance(t, tuple):
                    elementos = (elementos,)
                    break
            for ele in elementos:
                triagem = obtem_intersecoes_adjacentes(ele, obtem_ultima_intersecao(estado_goban))
                for tuplos in triagem:
                    if obtem_pedra(estado_goban, tuplos) != 2 and obtem_pedra(estado_goban, tuplos) != pedra:
                        cadeia.add(tuplos)
                
            for elemento in cadeia:
                pedra = obtem_pedra(estado_goban, x)

                for tuplos in cadeia:
                    caixa_pedras.add(obtem_pedra(estado_goban, tuplos))
                    caixa_pedras_2 += (caixa_pedras,)
                    caixa_pedras = set()  

                if pedra == 1:
                    if all(set([0]) == i for i in caixa_pedras_2):
                        if len(cadeia_remover) == 1:
                            estado_goban = remove_pedra(estado_goban, x)
                            return estado_goban
                        elif len(cadeia_remover) > 1:    
                            estado_goban = remove_cadeia(estado_goban, cadeia_remover)
                            return estado_goban 
                elif pedra == 0:
                    #Vê se todos os elementos em caixa_pedras_2 são 1
                    if all(set([1]) == i for i in caixa_pedras_2):
                        if len(cadeia_remover) == 1:
                            estado_goban = remove_pedra(estado_goban, x)
                            return estado_goban
                        elif len(cadeia_remover) > 1:    
                            estado_goban = remove_cadeia(estado_goban, cadeia_remover)
                            return estado_goban    
    return estado_goban        
            
def obtem_pedras_jogadores(g):
    global estado_goban

    if estado_goban is None:
        estado_goban = g

    pedras_brancas = 0
    pedras_pretas = 0

    for linha in estado_goban.split('\n')[1:-1]:
        for intersecao in linha:
            if intersecao == 'O':  #  0 represente uma pedra branca
                pedras_brancas += 1
            elif intersecao == 'X':  #  1 represente uma pedra preta
                pedras_pretas += 1

    return (pedras_brancas, pedras_pretas)

def calcula_pontos(g):
    global estado_goban

    if estado_goban is None:
        estado_goban = g

    pontos_j_b = obtem_pedras_jogadores(estado_goban)[0]
    pontos_j_p = obtem_pedras_jogadores(estado_goban)[1]
    
    territorios = obtem_territorios(estado_goban)
    territorio_pertence = territorio_de_quem(estado_goban, territorios)
    
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
 
