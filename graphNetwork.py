import json
import networkx as nx
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#had to install "scipy" aswell as matplotlib

G = nx.DiGraph()
#G.add_node('_carsonsharp')

from networkx.readwrite import json_graph
with open('network_data.json') as f:
	data = json.load(f)

#for p in data['users']:
#	print('Name: ' + p['name'])

G.add_nodes_from(
	elem['name']
	for elem in data['users'] 
)

#Add nodes and edges to G
for elem in data['users']:
	if elem['followers'] == 'True':
		G.add_edge(elem['name'] , 'Ryleeg99')
	if elem['friends'] == 'True':
		G.add_edge('Ryleeg99' , elem['name'])


#Draw Direct Graph/Friendship Network
pos = nx.spring_layout(G, k=0.15, iterations=20)
nx.draw(G, pos , with_labels=True)
plt.show()


#Histograph for pagerank distribution
pr = nx.pagerank(G, alpha = 0.9)
pagerank_values = list(pr.values())
pagerank_values = [round(num,6) for num in pagerank_values]

val,count = np.unique(pagerank_values, return_counts=True)

fig, ax = plt.subplots()
plt.xlabel("Pagerank")
plt.ylabel("Number of Nodes")
ax.bar(x=range(len(val)), height=count)
ax.set_xticks(range(len(val)))
ax.set_xticklabels(val)
plt.title("Pagerank Distribution")
plt.show()


#Histogram for Degree Distribtion
degrees = [G.degree(n) for n in G.nodes()] #creates array of all nodes' degree values
"""
plt.hist(degrees,range=[1,2], ec="k")
plt.tight_layout()
plt.show()
"""

val,count = np.unique(degrees, return_counts=True)

fig, ax = plt.subplots()
plt.xlabel("Degrees")
plt.ylabel("Number of Nodes")
ax.bar(x=range(len(val)), height=count)
ax.set_xticks(range(len(val)))
ax.set_xticklabels(val)
plt.title("Degree Distribution")
plt.show()



