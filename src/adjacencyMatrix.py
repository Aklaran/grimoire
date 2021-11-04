class AdjacencyMatrix:

  def __init__(self, size):
    if size < 1:
      raise ValueError

    self.matrix = self.__createEmptyMatrix(size)

  def size(self):
    return len(self.matrix)

  def addEdge(self, start, end):
    if start < 0 or end < 0:
      raise ValueError

    self.matrix[start][end] = True

  def addVertex(self):
    for i in range(self.size()):
      self.matrix[i].append(False)

    self.matrix.append([False] * (len(self.matrix) + 1))

  def areConnected(self, start, end):
    return self.matrix[start][end]

  def getEntrances(self, target):
    if target < 0 or target > (self.size() - 1):
      raise ValueError

    res = []

    for i in range(self.size()):
      if self.matrix[i][target]:
        res.append(i)

    return res

  def getExits(self, target):
    if target < 0 or target > (self.size() - 1):
      raise ValueError

    res = []

    for i in range(self.size()):
      if self.matrix[target][i]:
        res.append(i)

    return res

  def __createEmptyMatrix(self, size):
    res = [False] * size

    for i in range(size):
      res[i] = [False] * size

    return res
