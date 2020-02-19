import networkx as nx
import matplotlib.pyplot as plt
import math

###########LEITURA E CRIAÇÃO DO GRAFO ###################
arquivo = open('minimum-cicle3', 'r')
nvertices =int(arquivo.readline())
vertices = arquivo.readline().replace("\n","").split(" ")
narestas = int(arquivo.readline())
arestas=[]
G=nx.Graph()

G.add_nodes_from(vertices)

for i in range(narestas):
    arestas.append(arquivo.readline().replace("\n","").split(' '))

G.add_weighted_edges_from(arestas)
###########################################################

lista_de_ciclos=[] #serão armazenados os ciclos encontrados
peso_minimo=math.inf
for i in G.edges():    
    temp=G.get_edge_data(i[0], i[1])#a variavel armazena o peso da aresta
    temp2=(i[0],i[1],temp['weight'])#guardei as configurações vértices pra adicionar no gravo posteriormente
    G.remove_edge(i[0], i[1])#remove a aresta
    try:
        ciclo = nx.shortest_path(G, source=i[0], target=i[1], method='dijkstra') #Usa o algoritmo de Djikstra  para encontrar o menor caminho

        peso=0

        for j in range(len(ciclo)): #esse for percorre o menor caminho e calcula o peso do caminho
            if j!=(len(ciclo)-1):
                data=G.get_edge_data(ciclo[j], ciclo[j+1])
                peso=peso+int(data['weight'])
        peso=peso+int(temp['weight']) #adicionamos o peso da aresta que removemos.
        ciclo.sort() #ordeno o ciclo para facilitar comparação
        if peso<peso_minimo:
            lista_de_ciclos.append([ciclo, peso])
            peso_minimo=peso
        elif peso==peso_minimo:
            if len(lista_de_ciclos)>0:
                if [ciclo, peso] not in lista_de_ciclos: #verifica se o ciclo não foi adicionado anteriormente
                    lista_de_ciclos.append([ciclo, peso])
    except nx.NetworkXNoPath:
        None
    

    G.add_weighted_edges_from([(temp2)]) #poe de volta a resta que foii retirada
        


lista_aux=[]
for l in lista_de_ciclos: #esse for vai extrair todos os ciclos de peso minimo.
    if l[1]==peso_minimo:
        lista_aux.append(l)

####################TRATAMENTO DAS INFORMAÇÕES E DESENHOS DOS CICLOS #################
if len(lista_aux)>0:
    print('Peso minimo: '+str(peso_minimo))
    print("Quantidade de Ciclo de Tamanho Mínimo: "+str(len(lista_aux)))
    print('Ciclos:')
    cont=0
    for i in lista_aux:
        print(i[0])
        g1=nx.subgraph(G, i[0])
        plt.figure(cont)
        cont=cont+1
        pos=nx.shell_layout(g1)
        #vertices
        nx.draw_networkx_nodes(g1,pos, node_size=700)
        #arestas
        nx.draw_networkx_edges(g1, pos, edge_list=g1.edges())

        #titulos
        label=nx.get_edge_attributes(g1, 'weight')
        nx.draw_networkx_edge_labels(g1,pos,edge_labels=label)
        nx.draw_networkx_labels(g1, pos,
            node_color='r', 
            edge_color='b',
            font_size=12)
    ####################DESENHO DO GRAFICO PRINCIPAL#################
    plt.figure(cont)
    pos=nx.shell_layout(G)
    #vertices
    nx.draw_networkx_nodes(G, pos, node_size=700)
    #arestas
    nx.draw_networkx_edges(G, pos, edge_list=G.edges())

    #titulos
    label=nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=label)
    nx.draw_networkx_labels(G, pos,
        node_color='r', 
        edge_color='b',
        font_size=12)
    plt.show()
else:
    print('O grafo não possui ciclos.')    