import unittest
import dirTree

class TestDirTreeMethods(unittest.TestCase):
    test_dict1 = {"a/a": 1}
    test_dict2 = {"b/a": 1, "b/bb": 2}

    def test_combine_dirtree_keys(self):
        self.assertEqual(set([]), dirTree.combine_dirtree_keys([]))
        self.assertEqual(set(["a"]), dirTree.combine_dirtree_keys([self.test_dict1, self.test_dict1]))
        self.assertEqual(set(["a", "b"]), dirTree.combine_dirtree_keys([self.test_dict1, self.test_dict2]))
        self.assertEqual(set(["a", "b"]), dirTree.combine_dirtree_keys([self.test_dict2, self.test_dict1]))

        self.assertEqual(set([]), dirTree.combine_dirtree_keys(["a"]))
        self.assertEqual(set([]), dirTree.combine_dirtree_keys([["a"], ["a"]]))
        with self.assertRaises(TypeError):
            dirTree.combine_dirtree_keys(1)

    def test_all_dictionaries_contains_key(self):
        self.assertEqual(True, dirTree.all_dictionaries_contains_key([self.test_dict1, self.test_dict2], "a"))
        self.assertEqual(False, dirTree.all_dictionaries_contains_key([self.test_dict1, self.test_dict2], "b"))
        self.assertEqual(False, dirTree.all_dictionaries_contains_key([], "b"))

if __name__ == '__main__':
    unittest.main()