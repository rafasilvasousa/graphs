import matplotlib.pyplot as plt
import networkx as nx

################# FUNÇÃO PARA IMPRIMIR BUSCA PROF####################
def imprimir_profundidade(G:nx.Graph):
    print('Busca por profundidade')
    temp = busca_profundidade(G)
    caminho=temp[0]
    componentes = temp[-1]
    print('Componentes Conexos: '+str(componentes))
    if(componentes==1):
        print('Caminho: ', end='')
        for i in caminho[0]:
            print(str(i)+" ", end='')
        print()

    else:
        for i in range(componentes):
            print('Caminho do comp '+str(i+1)+': ', end='')
            for j in caminho[i]:
                print(str(j)+" ", end='')
            print()

#####################################################################

###################### FUNÇÃO DE BUSCA POR PROFUNDIDADE #############
def busca_profundidade(G: nx.Graph):
    visitados=[]
    saida=[]
    vetor_aux=[]
    comp_conexas = 0
    def prof(v):
        # print(v)
        #visitados.append(v)
        for i in G.neighbors(v):
            if i not in visitados:
                visitados.append(i)
                vetor_aux.append(i)
                #saida.append(i)
                prof(i)

    for i in G.nodes:
        if i not in visitados:
            if (len(vetor_aux)>0):
                saida.append(vetor_aux.copy())
            vetor_aux.clear()
            comp_conexas+=1
            vetor_aux.append(i)
            visitados.append(i)
            # saida.append(i)
            prof(i)
    saida.append(vetor_aux.copy())
    return (saida, comp_conexas)

#####################################################################

################# FUNÇÃO PARA IMPRIMIR BUSCA AMPL####################
def imprimir_amplitude(G:nx.Graph):
    print('Busca por amplitude')
    temp = busca_largura(G)
    caminho=temp[0]
    componentes = temp[-1]
    print('Componentes Conexos: '+str(componentes))
    if(componentes==1):
        print('Caminho: ', end='')
        for i in caminho:
            print(str(i)+" ", end='')
        print()

    # else:
        # for i in range(componentes):
        #     print('Caminho do comp '+str(i+1)+': ', end='')
        #     for j in caminho[i]:
        #         print(str(j)+" ", end='')
        #     print()

#####################################################################

###################### FUNÇÃO DE BUSCA POR AMPLITUDE ################
def busca_largura(G:nx.Graph):
    visitados=[]
    fila_aux=[]
    lista_aux=[]
    saida=[]
    comp_conexos=0
    for i in G.nodes:
        if i not in visitados:
            visitados.append(i)
            lista_aux.append(i)
            fila_aux.append(i)
        # if (len(fila_aux)>0):
        #     fila_aux.remove(i)
        #     if(len(fila_aux)==0):
        #         comp_conexos+=1
        #         if(len(lista_aux)>1):
        #             saida.append(lista_aux.copy)
        #             lista_aux.clear()
        for j in G.neighbors(i):
            if j not in visitados:
                visitados.append(j)
                fila_aux.append(j)
                lista_aux.append(j)

        if (len(fila_aux)>0):
            fila_aux.remove(i)
            if(len(fila_aux)==0):
                comp_conexos+=1
                if(len(lista_aux)>1):
                    saida.append(lista_aux.copy)
                    lista_aux.clear()
            
    return (saida, comp_conexos)



#####################################################################


######################## FUNÇÃO PRINCIPAL ###########################
arquivo = open('grafo1', 'r')
nvertices =int(arquivo.readline())

vertices = tuple(arquivo.readline().split())

narestas = int(arquivo.readline())

lista_arestas = []
for i in range(narestas):
    lista_arestas.append(arquivo.readline().strip().replace(' ', ''))

grafo = nx.Graph()


grafo.add_nodes_from(vertices)
grafo.add_edges_from(lista_arestas)

# imprimir_profundidade(grafo)
imprimir_amplitude(grafo)


nx.draw_networkx(grafo,with_labels=True, 
    pos=nx.planar_layout(grafo), 
    node_color='r', 
    edge_color='b')
plt.show()