from mathutils import Vector
from unittest import TestCase
from . complex_lists import Vector3DList

class TestInitialisation(TestCase):
    def testEmpty(self):
        v = Vector3DList()
        self.assertEqual(len(v), 0)

    def testWithLength(self):
        v = Vector3DList(10)
        self.assertEqual(len(v), 10)

    def testWithBoth(self):
        v = Vector3DList(10, 30)
        self.assertEqual(len(v), 10)

class TestAppend(TestCase):
    def setUp(self):
        self.list = Vector3DList()

    def testFirst(self):
        self.list.append((1, 2, 3))
        self.assertEqual(len(self.list), 1)

    def testWrongInputLength(self):
        with self.assertRaises(TypeError):
            self.list.append((2, 4))
        with self.assertRaises(TypeError):
            self.list.append((2, 4, 7, 9))

    def testWrongInputType(self):
        with self.assertRaises(TypeError):
            self.list.append("abc")

    def testVector(self):
        self.list.append(Vector((1, 2, 3)))
        self.assertEqual(self.list[0], Vector((1, 2, 3)))

class TestGetSingleItem(TestCase):
    def testEmptyList(self):
        v = Vector3DList()
        with self.assertRaises(IndexError):
            a = v[0]

    def testNormal(self):
        v = Vector3DList()
        for i in range(5):
            v.append((i, i, i))
        self.assertEqual(v[0], Vector((0, 0, 0)))
        self.assertEqual(v[1], Vector((1, 1, 1)))
        self.assertEqual(v[4], Vector((4, 4, 4)))

    def testNegativeIndex(self):
        v = Vector3DList()
        for i in range(5):
            v.append((i, i, i))
        self.assertEqual(v[-1], Vector((4, 4, 4)))
        self.assertEqual(v[-3], Vector((2, 2, 2)))
        with self.assertRaises(IndexError):
            a = v[-10]

    def testReturnType(self):
        v = Vector3DList()
        v.append((0, 0, 0))
        self.assertIsInstance(v[0], Vector)

class TestJoin(TestCase):
    def testNormal(self):
        v1 = Vector3DList()
        v1.append((0, 0, 0))
        v1.append((1, 1, 1))
        v2 = Vector3DList()
        v2.append((2, 2, 2))
        v2.append((3, 3, 3))
        v3 = Vector3DList()
        v3.append((4, 4, 4))
        v3.append((5, 5, 5))

        result = Vector3DList.join(v1, v2, v3)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[4], Vector((4, 4, 4)))

class TestAdd(TestCase):
    def testNormal(self):
        v1 = Vector3DList()
        v1.append((0, 0, 0))
        v1.append((1, 1, 1))
        v2 = Vector3DList()
        v2.append((2, 2, 2))
        v2.append((3, 3, 3))

        result = v1 + v2
        self.assertEqual(len(result), 4)
        self.assertEqual(result[2], Vector((2, 2, 2)))

class TestMultiply(TestCase):
    def testNormal(self):
        v = Vector3DList()
        v.append((0, 0, 0))
        v.append((1, 1, 1))
        r = v * 3
        self.assertEqual(len(r), 6)
        self.assertEqual(r[4], Vector((0, 0, 0)))

class TestInplaceAdd(TestCase):
    def testNormal(self):
        v1 = Vector3DList()
        v1.append((0, 0, 0))
        v1.append((1, 1, 1))
        v2 = Vector3DList()
        v2.append((2, 2, 2))
        v2.append((3, 3, 3))

        v1 += v2
        self.assertEqual(len(v1), 4)
        self.assertEqual(v1[2], Vector((2, 2, 2)))

class TestReversed(TestCase):
    def testNormal(self):
        v = Vector3DList()
        for i in range(4):
            v.append((i, i, i))
        r = v.reversed()
        self.assertEqual(r[0], Vector((3, 3, 3)))
        self.assertEqual(r[1], Vector((2, 2, 2)))
        self.assertEqual(r[2], Vector((1, 1, 1)))
        self.assertEqual(r[3], Vector((0, 0, 0)))

class TestExtend(TestCase):
    def setUp(self):
        self.list = Vector3DList()

    def testEmptyInput(self):
        self.list.extend([])
        self.assertEqual(len(self.list), 0)

    def testListInput(self):
        self.list.extend([(0, 0, 0), (1, 1, 1), (2, 2, 2)])
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[1], Vector((1, 1, 1)))

    def testTupleInput(self):
        self.list.extend(([0, 0, 0], [1, 1, 1], [2, 2, 2]))
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[1], Vector((1, 1, 1)))

    def testVectorListInput(self):
        self.list.extend([Vector((0, 0, 0)), Vector((1, 1, 1)), Vector((2, 2, 2))])
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[1], Vector((1, 1, 1)))

    def testOtherBaseListInput(self):
        tmp = Vector3DList()
        tmp.extend([(0, 0, 0), (1, 1, 1), (2, 2, 2)])
        self.list.extend(tmp)
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[1], Vector((1, 1, 1)))

    def testWrongInputType(self):
        with self.assertRaises(TypeError):
            self.list.extend("abc")

class TestFromValues(TestCase):
    def testEmptyInput(self):
        v = Vector3DList.fromValues([])
        self.assertEqual(len(v), 0)

    def testWrongInputType(self):
        with self.assertRaises(TypeError):
            v = Vector3DList.fromValues("abc")
        with self.assertRaises(TypeError):
            v = Vector3DList.fromValues([(0, 0, 0), (1, 1, 1, 1)])

    def testListInput(self):
        v = Vector3DList.fromValues([(0, 0, 0), (1, 1, 1), (2, 2, 2)])
        self.assertEqual(len(v), 3)
        self.assertEqual(v[1], Vector((1, 1, 1)))

    def testOtherComplexListInput(self):
        tmp = Vector3DList.fromValues([(0, 0, 0), (1, 1, 1), (2, 2, 2)])
        v = Vector3DList.fromValues(tmp)
        self.assertEqual(len(v), 3)
        self.assertEqual(v[1], Vector((1, 1, 1)))

class TestGetValuesInSlice(TestCase):
    def setUp(self):
        self.list = Vector3DList()
        for i in range(10):
            self.list.append((i, i, i))

    def testStart(self):
        v = self.list[:3]
        self.assertEqual(len(v), 3)
        self.assertEqual(v[0].x, 0)
        self.assertEqual(v[1].y, 1)
        self.assertEqual(v[2].z, 2)

    def testMiddle(self):
        v = self.list[3:6]
        self.assertEqual(len(v), 3)

    def testReverse(self):
        v = self.list[::-1]
        self.assertEqual(len(v), 10)
        self.assertEqual(v[0], Vector((9, 9, 9)))
        self.assertEqual(v[9], Vector((0, 0, 0)))

    def testStep(self):
        v = self.list[::2]
        self.assertEqual(len(v), 5)
        self.assertEqual(v[2], Vector((4, 4, 4)))

class TestContains(TestCase):
    def setUp(self):
        self.list = Vector3DList.fromValues(
            [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3)])

    def testInside(self):
        self.assertTrue((2, 2, 2) in self.list)
        self.assertTrue([1, 1, 1] in self.list)
        self.assertTrue(Vector((3, 3, 3)) in self.list)

    def testNotInside(self):
        self.assertFalse((4, 4, 4) in self.list)
        self.assertFalse([-1, -1, -1] in self.list)
        self.assertFalse(Vector((4, 5, 6)) in self.list)

    def testWrongInputType(self):
        with self.assertRaises(TypeError):
            a = "abc" in self.list
        with self.assertRaises(TypeError):
            a = (0, 0, 0, 0) in self.list

class TestIndex(TestCase):
    def setUp(self):
        self.list = Vector3DList.fromValues(
            [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3)])

    def testInside(self):
        self.assertEqual(self.list.index((0, 0, 0)), 0)
        self.assertEqual(self.list.index((1, 1, 1)), 1)
        self.assertEqual(self.list.index((2, 2, 2)), 2)
        self.assertEqual(self.list.index((3, 3, 3)), 3)

    def testNotInside(self):
        with self.assertRaises(ValueError):
            self.list.index((0, 1, 2))

    def testWrongType(self):
        with self.assertRaises(TypeError):
            self.list.index("abc")

    def testTooLongInput(self):
        with self.assertRaises(TypeError):
            self.list.index((0, 0, 0, 0))

    def testTooShortInput(self):
        with self.assertRaises(TypeError):
            self.list.index((0, 0))

    def testList(self):
        self.assertEqual(self.list.index([2, 2, 2]), 2)

    def testTuple(self):
        self.assertEqual(self.list.index((2, 2, 2)), 2)

    def testVector(self):
        self.assertEqual(self.list.index(Vector((2, 2, 2))), 2)

class TestCount(TestCase):
    def setUp(self):
        self.list = Vector3DList.fromValues(
            [(0, 0, 0), (1, 1, 1), (0, 0, 0), (3, 3, 3),
             (0, 0, 0), (1, 2, 3), (3, 2, 1), (1, 2, 3)])

    def testWrongType(self):
        with self.assertRaises(TypeError):
            self.list.count("abc")

    def testWrongLength(self):
        with self.assertRaises(TypeError):
            self.list.count((0, 0))
        with self.assertRaises(TypeError):
            self.list.count((0, 0, 0, 0))

    def testNormal(self):
        self.assertEqual(self.list.count((0, 0, 0)), 3)
        self.assertEqual(self.list.count((1, 1, 1)), 1)
        self.assertEqual(self.list.count((3, 3, 3)), 1)
        self.assertEqual(self.list.count((1, 2, 3)), 2)
        self.assertEqual(self.list.count((3, 2, 1)), 1)

    def testNotInside(self):
        self.assertEqual(self.list.count((2, 6, 4)), 0)

class TestSetSingleElement(TestCase):
    def setUp(self):
        self.list = Vector3DList.fromValues([(0, 0, 0), (1, 1, 1), (2, 2, 2)])

    def testWrongType(self):
        with self.assertRaises(TypeError):
            self.list[1] = "abc"

    def testWrongLength(self):
        with self.assertRaises(TypeError):
            self.list[1] = (1, 1, 1, 1)
        with self.assertRaises(TypeError):
            self.list[1] = (1, 1)

    def testTuple(self):
        self.list[1] = (4, 5, 6)
        self.assertEqual(self.list[1], Vector((4, 5, 6)))

    def testList(self):
        self.list[1] = [6, 7, 8]
        self.assertEqual(self.list[1], Vector((6, 7, 8)))

    def testVector(self):
        self.list[1] = Vector((3, 4, 5))
        self.assertEqual(self.list[1], Vector((3, 4, 5)))

    def testNegativeIndex(self):
        self.list[-1] = (7, 7, 7)
        self.assertEqual(self.list[2], Vector((7, 7, 7)))

    def testInvalidIndex(self):
        with self.assertRaises(IndexError):
            self.list[5] = (1, 1, 1)
        with self.assertRaises(IndexError):
            self.list[-5] = (1, 1, 1)

class TestDeleteSingleElement(TestCase):
    def setUp(self):
        self.list = Vector3DList.fromValues(
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)])

    def testLength(self):
        del self.list[0]
        self.assertEqual(len(self.list), 2)

    def testPositiveIndex(self):
        del self.list[1]
        self.assertEqual(self.list[1], Vector((6, 7, 8)))

    def testNegativeIndex(self):
        del self.list[-3]
        self.assertEqual(self.list[0], Vector((3, 4, 5)))

    def testInvalidIndex(self):
        with self.assertRaises(IndexError):
            del self.list[6]
        with self.assertRaises(IndexError):
            del self.list[-6]

class TestSetElementsInSlice(TestCase):
    def setUp(self):
        self.list = Vector3DList.fromValues(
            [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3)])

    def testWrongLength(self):
        with self.assertRaises(ValueError):
            self.list[:3] = [(1, 2, 3), (5, 6, 7)]

    def testWrongType(self):
        with self.assertRaises(Exception):
            self.lists[:3] = "abc"

    def testInvalidElement(self):
        with self.assertRaises(TypeError):
            self.list[:3] = [(1, 2, 3), (4, 5, 6, 7), (0, 0, 0)]

    def testStart(self):
        self.list[:2] = (1, 2, 3), (4, 5, 6)
        self.assertEqual(self.list[0], Vector((1, 2, 3)))
        self.assertEqual(self.list[1], Vector((4, 5, 6)))
        self.assertEqual(self.list[2], Vector((2, 2, 2)))

    def testEnd(self):
        self.list[2:] = (5, 6, 7), (1, 2, 3)
        self.assertEqual(self.list[2], Vector((5, 6, 7)))
        self.assertEqual(self.list[3], Vector((1, 2, 3)))

    def testNegativeStep(self):
        self.list[::-2] = (1, 2, 3), (4, 5, 6)
        self.assertEqual(self.list[1], Vector((4, 5, 6)))
        self.assertEqual(self.list[3], Vector((1, 2, 3)))
