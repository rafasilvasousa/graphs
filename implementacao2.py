import matplotlib.pyplot as plt
import networkx as nx

################# FUNÇÃO PARA IMPRIMIR ####################
def imprimir(temp):
    caminho=temp[0]
    componentes = temp[-1]
    for i in range(componentes):
        print('Componente: '+str(i+1))
        for j in caminho[i]:
            print(str(j)+" ", end='')
        print('\n---------------------')

###################### FUNÇÃO DE BUSCA POR PROFUNDIDADE #############
def busca_profundidade(G: nx.Graph):
    visitados=[]
    saida=[]
    vetor_aux=[]
    comp_conexas = 0
    def prof(v):
        for i in G.neighbors(v):
            if i not in visitados:
                visitados.append(i)
                vetor_aux.append(i)
                prof(i)

    for i in G.nodes:
        if i not in visitados:
            if (len(vetor_aux)>0):
                saida.append(vetor_aux.copy())
            vetor_aux.clear()
            comp_conexas+=1
            vetor_aux.append(i)
            visitados.append(i)
            prof(i)
    saida.append(vetor_aux.copy())
    return (saida, comp_conexas)

#####################################################################


###################### FUNÇÃO DE BUSCA POR AMPLITUDE ################
def busca_largura(G:nx.Graph):
    fila=[]
    li_comp=[]
    visitados=[]
    comp_cone=0
    saida=[]
    index=0

    def check_largura(G:nx.Graph):
        for i in fila:
            fila.remove(i)
            for j in G.neighbors(i):
                if j not in visitados:
                    visitados.append(j)
                    fila.append(j)
                    li_comp.append(j)
            check_largura(G)

    
    for i in G.nodes():
        if i not in visitados:
            visitados.append(i)
            fila.append(i)
            li_comp.append(i)
            check_largura(G)
            comp_cone= comp_cone+1
            saida.append([])
            saida[index].extend(li_comp.copy())
            index=index+1
            li_comp.clear()
    
    return(saida, comp_cone)


#####################################################################


######################## FUNÇÃO PRINCIPAL ###########################
arquivo = open('grafo2', 'r')
nvertices =int(arquivo.readline())

vertices = tuple(arquivo.readline().split())

narestas = int(arquivo.readline())

lista_arestas = []

for i in range(narestas):
    lista_arestas.append(arquivo.readline().strip().replace(' ', ''))

grafo = nx.Graph()


grafo.add_nodes_from(vertices)
grafo.add_edges_from(lista_arestas)

profundidade=busca_profundidade(grafo)
print("--> Algoritmo DFS")
imprimir(profundidade)
print()
print()
print('=================================================')
print()
print("--> Algoritmo BFS")
largura=(busca_largura(grafo))
imprimir(largura)


nx.draw_networkx(grafo,with_labels=True, 
    pos=nx.planar_layout(grafo), 
    node_color='r', 
    edge_color='b')
plt.show()