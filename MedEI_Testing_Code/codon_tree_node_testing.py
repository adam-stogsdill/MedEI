import unittest
from Gene_Engine.CodonTreeNode import construct_codon_translation_tree, path_traversal


class CodonTreeFunctionality(unittest.TestCase):

    def test_codon_tree_lookup(self):
        node = construct_codon_translation_tree()
        self.assertEqual(path_traversal(node, 'uuu'), 'F')
        self.assertEqual(path_traversal(node, 'uuc'), 'F')
        self.assertEqual(path_traversal(node, 'uua'), 'L')
        self.assertEqual(path_traversal(node, 'uug'), 'L')
        self.assertEqual(path_traversal(node, 'ucu'), 'S')
        self.assertEqual(path_traversal(node, 'ucc'), 'S')
        self.assertEqual(path_traversal(node, 'uca'), 'S')
        self.assertEqual(path_traversal(node, 'ucg'), 'S')


if __name__ == '__main__':
    unittest.main()
