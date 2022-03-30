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

#Add every node/user in friendship network
G.add_nodes_from(
	node['name']
	for node in data['users'] 
)

#Add edges/relationships between main user and their followers/followees
for node in data['users']:
	if node['follower'] == 'True':
		G.add_edge(node['name'] , '_carsonsharp')
	if node['friend'] == 'True':
		G.add_edge('_carsonsharp' , node['name'])


#Add relationships between the followers and followees
for node in data['users']:
	friend_list = node['mutual_friends'].split(",")
	while("" in friend_list):
		friend_list.remove("")
	for connect_friends in friend_list:
		G.add_edge(node['name'], connect_friends)
	follower_list = node['mutual_followers'].split(",")
	while("" in follower_list):
		follower_list.remove("")
	for connect_followers in follower_list:
		G.add_edge(connect_followers, node['name'])
		



#Draw Direct Graph/Friendship Network
pos = nx.spring_layout(G, k=0.8, iterations=40)
nx.draw(G, pos , with_labels=True)
plt.show()


print(nx.clustering(G))


#Histograph for Pagerank distribution
pr = nx.pagerank(G, alpha = 0.9)
pagerank_values = list(pr.values())
pagerank_values = [round(num,6) for num in pagerank_values]

plt.title("Pagerank Distribution")
plt.xlabel("Pagerank")
plt.ylabel("Number of Nodes")
plt.hist(pagerank_values, ec="k")
plt.show()


#Histogram for In/Out Degree Distribtion
degrees = [G.degree(n) for n in G.nodes()] #creates array of all nodes' degree values

#print(degrees)

plt.title("In/Out Degree Distribution")
plt.xlabel("Degrees")
plt.ylabel("Number of Nodes")
plt.hist(degrees, ec="k")
#plt.tight_layout()
plt.show()



