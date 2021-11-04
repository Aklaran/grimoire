import unittest
from src.adjacencyMatrix import AdjacencyMatrix


class TestAdjacencyMatrix(unittest.TestCase):

  def test_init_length1(self):
    sut = AdjacencyMatrix(1)

    self.assertEqual(sut.size(), 1, "size should be 1")
    self.assertEqual(len(sut.matrix), 1, "length should be 1")
    self.assertEqual(len(sut.matrix[0]), 1,
                     "length of first element should be 1")
    self.assertEqual(sut.matrix[0][0], False, "all elements should be False")

  def test_init_invalidLengths(self):
    self.assertRaises(ValueError, lambda: AdjacencyMatrix(0))
    self.assertRaises(ValueError, lambda: AdjacencyMatrix(-5))

  def test_init_length5(self):
    sut = AdjacencyMatrix(5)

    self.assertEqual(sut.size(), 5, "size should be 5")
    self.assertEqual(len(sut.matrix), 5, "length should be 5")
    self.assertEqual(len(sut.matrix[0]), 5,
                     "length of first element should be 5")

  def test_addEdge_inBounds(self):
    sut = AdjacencyMatrix(5)

    sut.addEdge(0, 0)

    self.assertEqual(sut.matrix[0][0], True,
                     "first element should be set to True")

  def test_addEdge_outOfBounds(self):
    sut = AdjacencyMatrix(5)

    self.assertRaises(ValueError, lambda: sut.addEdge(-1, 0))
    self.assertRaises(ValueError, lambda: sut.addEdge(0, -6))

  def test_addVertex(self):
    sut = AdjacencyMatrix(5)

    sut.addVertex()

    self.assertEqual(sut.size(), 6, "size should be 6")
    self.assertEqual(len(sut.matrix), 6, "length should be 6")
    self.assertEqual(len(sut.matrix[0]), 6,
                     "length of first element should be 6")

  def test_areConnected(self):
    sut = AdjacencyMatrix(2)

    self.assertFalse(sut.areConnected(0, 1))

    sut.addEdge(0, 1)

    self.assertTrue(sut.areConnected(0, 1))
    self.assertFalse(sut.areConnected(1, 0))

  def test_getEntrances(self):
    sut = AdjacencyMatrix(3)

    self.assertEqual([], sut.getEntrances(2))

    sut.addEdge(0, 2)
    sut.addEdge(2, 2)

    self.assertEqual([0, 2], sut.getEntrances(2))

  def test_getExits(self):
    sut = AdjacencyMatrix(3)

    self.assertEqual([], sut.getExits(2))

    sut.addEdge(2, 0)
    sut.addEdge(2, 2)

    self.assertEqual([0, 2], sut.getExits(2))


if __name__ == '__main__':
  unittest.main()
