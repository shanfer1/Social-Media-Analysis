import matplotlib.pyplot as plt
import networkx as nx

def degree_histogram_directed(G, in_degree=False, out_degree=False):
    nodes = G.nodes()
    if in_degree:
        in_degree = dict(G.in_degree())
        degseq=[in_degree.get(k,0) for k in nodes]
    elif out_degree:
        out_degree = dict(G.out_degree())
        degseq=[out_degree.get(k,0) for k in nodes]
    else:
        degseq=[v for k, v in G.degree()]
    dmax=max(degseq)+1
    freq= [ 0 for d in range(dmax) ]
    for d in degseq:
        freq[d] += 1
    return freq

def plotDegreeHistogram(DGs):
    g1=DGs[0]
    g2=DGs[1]
    in_degree_freq = degree_histogram_directed(g1, in_degree=True)
    out_degree_freq = degree_histogram_directed(g1, out_degree=True)
    plt.figure(figsize=(12, 8)) 
    plt.plot(range(len(in_degree_freq)), in_degree_freq, "go-", label='in_degree') 
    plt.plot(range(len(out_degree_freq)), out_degree_freq, "bo-", label='out_degree')
    plt.legend(loc="upper right")
    y_max=max(max(in_degree_freq),max(out_degree_freq))
    plt.axis([0,len(in_degree_freq),0,y_max])
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title('Pro Vaccine degree distribution')
    plt.show()

    
    in_degree_freq = degree_histogram_directed(g2, in_degree=True)
    out_degree_freq = degree_histogram_directed(g2, out_degree=True)
    plt.figure(figsize=(12, 8)) 
    y_max=max(max(in_degree_freq),max(out_degree_freq))
    plt.plot(range(len(in_degree_freq)), in_degree_freq, 'go-', label='in-degree') 
    plt.plot(range(len(out_degree_freq)), out_degree_freq, 'bo-', label='out-degree')
    plt.legend(loc="upper right")
    plt.axis([0,len(in_degree_freq),0,y_max])
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title('Anti Vaccine Degree Distribution')
    plt.show()


    nodes=g1.nodes()
    clusterDict=nx.clustering(g1)
    coeffients=[clusterDict.get(k,0) for k in nodes]
    y_max=1
    plt.figure(figsize=(12, 8)) 
    plt.plot(list(nodes), coeffients, 'go-', label='local-clustering-coefficient for pro vaccine') 
    plt.legend(loc="upper right")
    plt.axis([0,len(nodes),0,y_max])
    plt.xlabel('Nodes')
    plt.ylabel('Clustering Coeficient')
    plt.title('Local clustering Coeffient for pro vaccine')
    plt.show()

    nodes=g2.nodes()
    clusterDict=nx.clustering(g2)
    coeffients=[clusterDict.get(k,0) for k in nodes]
    y_max=1
    plt.figure(figsize=(12, 8)) 
    plt.plot(list(nodes), coeffients, 'go-', label='local-clustering-coefficient for anti vaccine') 
    plt.legend(loc="upper right")
    plt.axis([0,len(nodes),0,y_max])
    plt.xlabel('Nodes')
    plt.ylabel('Clustering Coeficient')
    plt.title('Local clustering Coeffient for anti vaccine')
    plt.show()


    nodes=g1.nodes()
    closenessDict=nx.closeness_centrality(g1)
    closeness=[closenessDict.get(k,0) for k in nodes]
    y_max=1
    plt.figure(figsize=(12, 8)) 
    plt.plot(list(nodes), closeness, 'go-', label='Closeness centrality for pro vaccine') 
    plt.legend(loc="upper right")
    plt.axis([0,len(nodes),0,y_max])
    plt.xlabel('Nodes')
    plt.ylabel('Closeness Centrality')
    plt.title('Closeness Centrality for pro vaccine')
    plt.show()

    nodes=g2.nodes()
    closenessDict=nx.closeness_centrality(g2)
    closeness=[closenessDict.get(k,0) for k in nodes]
    y_max=1
    plt.figure(figsize=(12, 8)) 
    plt.plot(list(nodes), closeness, 'go-', label='Closeness centrality for anti vaccine') 
    plt.legend(loc="upper right")
    plt.axis([0,len(nodes),0,y_max])
    plt.xlabel('Nodes')
    plt.ylabel('Closeness Centrality')
    plt.title('Closeness Centrality for anti vaccine')
    plt.show()