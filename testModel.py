from model.model import Model

m = Model()

m.buildGraph(1895)
print(m.getWeightNodes(1895))