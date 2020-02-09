import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def gera_lista(G, n):
    m=[]
    m.extend(G.neighbors(n))
    return m
'''
def gera_matriz(G, n):
''' 
    
###################PARA TESTES HABILITAR ESSE TREECHO DE CODIGO #################################################################
# print("Escreva a lista dos nós separados por vírgula: ")
# nodes = input().split(",")
# print(type(nodes))
# print("Escreva a lista das arestas no formato ab separados por vírgula: ")
# edges = input().split(",")
# print(type(edges))
# print(edges)
##############################################################################################

# lista de nós para testes: [a, b, c, d, e, f] -> entrada a,b,c,d,e,f
# exemplo de arestas para teste (a,b),(d,e),(c,e),(b,c),(e,f)
# entrada ab,de,ce,bc,ef

########################PARA TESTES DESABILITAR ESSE TRECHO DE CODIGO##################
nodes='a', 'b', 'c', 'd', 'e', 'f'
edges='ab','de','ce','bc','ef'
#####################################################################################

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# for i in G.nodes:
#     print("Lista de adjacencias de "+i+": "+ str(gera_lista(G,i)))

m=nx.adjacency_matrix(G)
print(m.toarray())


nx.draw_networkx(G,with_labels=True, pos=nx.circular_layout(G), node_color='r', edge_color='b')

plt.show()




