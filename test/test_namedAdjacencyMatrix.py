import unittest
from src.namedAdjacencyMatrix import NamedAdjacencyMatrix


class TestAdjacencyMatrix(unittest.TestCase):

  def test_init_length1(self):
    names = ["540"]
    sut = NamedAdjacencyMatrix(names)

    self.assertEqual(len(sut.matrix), 1)
    self.assertEqual(sut.names["540"], 0)

  def test_init_length3(self):
    names = ["540", "touchdown raiz", "cork"]
    sut = NamedAdjacencyMatrix(names)
    self.assertEqual(len(sut.matrix), 3)
    self.assertEqual(sut.names["540"], 0)
    self.assertEqual(sut.names["cork"], 2)

  def test_init_length0(self):
    names = []
    self.assertRaises(ValueError, lambda: NamedAdjacencyMatrix(names))

  def test_addNamedEdge(self):
    names = ["540", "touchdown raiz", "cork"]
    sut = NamedAdjacencyMatrix(names)

    self.assertFalse(sut.areNamesConnected("touchdown raiz", "cork"))

    sut.addNamedEdge("touchdown raiz", "cork")

    self.assertTrue(sut.areNamesConnected("touchdown raiz", "cork"))

  def test_getNamedEntrances(self):
    names = ["540", "touchdown raiz", "cork"]
    sut = NamedAdjacencyMatrix(names)

    self.assertEqual([], sut.getNamedEntrances("cork"))

    sut.addNamedEdge("touchdown raiz", "cork")

    self.asser
