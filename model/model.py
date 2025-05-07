import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._county = DAO.getAllNodes()
        self._grafo = nx.Graph()
        self._idMapCounty = {}
        for a in self._county:
            self._idMapCounty[a.CCode] = a

    def getAllCountry(self):
        return DAO.getAllNodes()

    def buildGraph(self, anno):
        # Aggiungo i nodi
        anno = int(anno)
        self._grafo.clear()
        self._county = DAO.getNodes(anno)
        self._grafo.add_nodes_from(self._county)  # aggiungo un nodo per ogni fermata
        self.getAllEdges(anno)

    def getAllEdges(self, anno):
        """
        Faccio una query che prende tutti gli arghi
        e poi mi arrangio su python
        """
        allEdges = DAO.getAllEdges(anno)
        for e in allEdges:
            self._grafo.add_edge(self._idMapCounty[e.state1no], self._idMapCounty[e.state2no])



    def getWeightNodes(self,anno):
        anno = int(anno)
        nodiPesati = DAO.getWeightNodes(anno)
        return nodiPesati


    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def getNumConnessa(self):
        return nx.number_connected_components(self._grafo)

    def getComponenteConnessa(self, stato):
        print(f"hai selezionato: {self._idMapCounty[int(stato)]}")
        conn = nx.node_connected_component(self._grafo, self._idMapCounty[int(stato)])
        return conn


