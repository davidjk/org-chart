""" Import an org chart in CSV format
Create a quick plot of directed graph and export as GML

Kelsey Jordahl
David Kim
Enthought, Inc.
Time-stamp: <Thu Jan 10 15:50:55 EST 2013>
"""

import csv
import networkx as nx
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    csv_file_name = sys.argv[1]
    gml_file_name = sys.argv[2]
    G = nx.DiGraph()
    labels = {}
    with open(csv_file_name, 'rU') as csvfile:
        csvreader = csv.reader(csvfile)
        header = csvreader.next()
        for row in csvreader:
            node = {}
            for key, value in zip(header, row):
                node[key] = value
            G.add_node(node['name'],
                       title=node['title'],
                       group1=node['group1'],
                       group2=node['group2'],
                       group3=node['group3'],)
            labels[node['name']] = '%s\n%s\n%s\n%s\n%s' % (
                node['name'],
                node['title'],
                node['group1'],
                node['group2'],
                node['group3'])
            if node.get('reports_to', None):
                print node['name'], node['reports_to']
                G.add_edge(node['name'], node['reports_to'])
    try:
        pos = nx.graphviz_layout(G)
    except:
        pos = nx.spring_layout(G, iterations=20)
    plt.figure()
    nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color='m', arrow=True)
    nx.draw_networkx_nodes(G, pos, node_size=50, node_color='w', alpha=0.4)
    nx.draw_networkx_labels(G, pos, labels, fontsize=14)
    nx.write_gml(G, gml_file_name)
    plt.show()
