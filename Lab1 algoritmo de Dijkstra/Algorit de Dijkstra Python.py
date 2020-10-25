def dijkstra(graf,src,dest,visit=[],distan={},prede={}):
    if src == dest:
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=prede.get(pred,None)
        readable=path[0]
        for i in range(1,len(path)): readable = path[i]+'--->'+readable
        print('Camino mas corto: '+str(path))
        print("Valor Total="+str(distan[dest]))
    else :     
        if not visit: 
            distan[src]=0
        for vecino in graph[src] :
            if vecino not in visit:
                n_distan = distan[src] + graph[src][vecino]
                if n_distan < distan.get(vecino,float('inf')):
                    distan[vecino] = n_distan
                    prede[vecino] = src
        visit.append(src)
        s_visited={}
        for k in graph:
            if k not in visit:
                s_visited[k] = distan.get(k,float('inf'))        
        x=min(s_visited, key=s_visited.get)
        dijkstra(graph,x,dest,visit,distan,prede)
        
if True:
    graph = {'a': {'b': 5, 'c': 9},
            'b': {'a': 5, 'e': 10, 'f': 7},
            'c': {'a': 9, 'd': 3, 'e': 5},
            'd': {'c': 3, 'e': 1, 'g': 4},
            'e': {'d': 1, 'b': 10, 'c': 5, 'h': 2, 'g': 4},
            'f': {'b': 7, 'h': 8},
            'g': {'d': 4, 'e': 4, 'i': 12},
            'h': {'f': 8, 'e': 2, 'i': 6},
            'i': {'h': 6, 'g': 12}
            }
    dijkstra(graph,'a','e')