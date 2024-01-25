from sorting import insertionSort
import unittest

class TestInsertionSort(unittest.TestCase):
    def test_asc_num(self):
        arr1 = [64, 34, 25, 12, 22, 11, 90]
        print("\nExpected Output: [11, 12, 22, 25, 34, 64, 90]")
        print("Actual Output: ",insertionSort(arr1))
        self.assertEqual(insertionSort(arr1), [11, 12, 22, 25, 34, 64, 90])
    def test_desc_num(self):
        arr2 = [64, 34, 25, 12, 22, 11, 90]
        print("\nExpected Output: [90, 64, 34, 25, 22, 12, 11]")
        print("Actual Output:",insertionSort(arr2, ascending=False))
        self.assertEqual(insertionSort(arr2, ascending=False), [90, 64, 34, 25, 22, 12, 11])
    def test_asc_str(self):
        arr3 = ['banana', 'date', 'apple', 'plum', 'cherry', 'apricot', 'blueberry']
        print("\nExpected Output: ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'date', 'plum']")
        print("Actual Output:",insertionSort(arr3))
        self.assertEqual(insertionSort(arr3), ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'date', 'plum'])
    def test_desc_str(self):
        arr4 = ['banana', 'date', 'apple', 'plum', 'cherry', 'apricot', 'blueberry']
        print("\nExpected Output: ['plum', 'date', 'cherry', 'blueberry', 'banana', 'apricot', 'apple']")
        print("Actual Output:",insertionSort(arr4, ascending=False))
        self.assertEqual(insertionSort(arr4, ascending=False), ['plum', 'date', 'cherry', 'blueberry', 'banana', 'apricot', 'apple'])
    def test_heterogenous(self):
        arr3 = [1, 'string', 23]
        print("\nExpected Output: Exception: Heterogeneous array")
        print("Actual Output:",insertionSort(arr3))
        self.assertEqual(insertionSort(arr3), "Exception: Heterogeneous array")

if __name__ == '__main__':
    unittest.main()