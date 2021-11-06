from src.adjacencyMatrix import AdjacencyMatrix


class NamedAdjacencyMatrix(AdjacencyMatrix):

  def __init__(self, names):
    if len(names) == 0:
      raise ValueError

    self.names = {}
    for i in range(len(names)):
      self.names[names[i]] = i

    super().__init__(len(names))

  def addNamedEdge(self, start, end):
    startIndex = self.names[start]
    endIndex = self.names[end]

    self.addEdge(startIndex, endIndex)

  def addNamedVertex(self, name):
    index = self.size()

    self.names[name] = index

    self.addVertex()

  def areNamesConnected(self, start, end):
    startIndex = self.names[start]
    endIndex = self.names[end]

    return self.areConnected(startIndex, endIndex)

  def getNamedEntrances(self, target):
    index = self.names[target]

    entranceIndices = self.getEntrances(index)

    return map()

  def getNamedExits(self, target):
    index = self.names[target]

    return self.getExits(index)
