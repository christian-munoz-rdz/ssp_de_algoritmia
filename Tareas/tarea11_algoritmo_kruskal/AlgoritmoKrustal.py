# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:01:04 2022

@author: goten
"""

from networkx.algorithms import tree
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_edge("A","B", weight = 1)
g.add_edge("A","E", weight = 2)
g.add_edge("A","C", weight = 3)
g.add_edge("A","D", weight = 4)
g.add_edge("B","D", weight = 5)
g.add_edge("B","H", weight = 6)
g.add_edge("B","C", weight = 7)
g.add_edge("C","D", weight = 8)
g.add_edge("C","E", weight = 9)
g.add_edge("C","H", weight = 10)
g.add_edge("C","J", weight = 11)
g.add_edge("C","G", weight = 12)
g.add_edge("D","F", weight = 13)
g.add_edge("D","H", weight = 14)
g.add_edge("E","G", weight = 15)
g.add_edge("E","F", weight = 16)
g.add_edge("F","C", weight = 17)
g.add_edge("F","G", weight = 18)
g.add_edge("F","J", weight = 19)
g.add_edge("F","I", weight = 20)
g.add_edge("G","I", weight = 21)
g.add_edge("G","H", weight = 23)
g.add_edge("G","J", weight = 24)
g.add_edge("H","J", weight = 25)
g.add_edge("I","J", weight = 26)

pos=nx.spring_layout(g)

plt.subplot(121)

edge_labels = dict([((u,v,), d['weight'])
                   for u,v,d in g.edges(data = True)])
nx.draw_networkx_edge_labels(g, pos, edge_labels = edge_labels)
nx.draw(g,pos,with_labels=True, node_color = "green")


plt.subplot(122)

h = tree.minimum_spanning_tree(g, algorithm='kruskal')
edge_labels = dict([((u,v,), d['weight'])
                   for u,v,d in h.edges(data = True)])
nx.draw_networkx_edge_labels(h, pos, edge_labels = edge_labels)
nx.draw(h,pos,with_labels=True, node_color = 'red')


plt.show()
print("Nodos")
print(g.nodes)
print("Aristas")
print(g.edges)