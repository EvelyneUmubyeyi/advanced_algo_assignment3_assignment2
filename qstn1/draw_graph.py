import networkx as nx
import matplotlib.pyplot as plt

def draw_graph (mst) :
    # Create a networkx graph for the MST
    G_mst = nx.Graph()

    # Add nodes and MST edges to the graph
    for edge in mst:
        G_mst.add_edge(edge[0], edge[1], weight=edge[2])

    # Create a figure for the plot
    plt.figure(figsize=(8, 6))

    # Draw the MST edges
    pos = nx.spring_layout(G_mst)
    nx.draw(G_mst, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', edge_color='r', width=2, edge_cmap=plt.cm.Blues, font_size=8)

    # Display edge weights
    edge_labels = nx.get_edge_attributes(G_mst, 'weight')
    nx.draw_networkx_edge_labels(G_mst, pos, edge_labels=edge_labels, font_color='black')

    # Display vertices
    nx.draw_networkx_nodes(G_mst, pos, node_color='skyblue', node_size=700)
    nx.draw_networkx_labels(G_mst, pos, font_color='black')

    plt.title('Minimum Spanning Tree')
    plt.show()

