import unittest
from Gene_Engine.codon_tree_node import construct_codon_translation_tree, path_traversal


class CodonTreeFunctionality(unittest.TestCase):

    def test_codon_tree_lookup(self):
        node = construct_codon_translation_tree()
        # U Testing
        self.assertEqual(path_traversal(node, 'uuu'), 'F')
        self.assertEqual(path_traversal(node, 'uuc'), 'F')
        self.assertEqual(path_traversal(node, 'uua'), 'L')
        self.assertEqual(path_traversal(node, 'uug'), 'L')
        self.assertEqual(path_traversal(node, 'ucu'), 'S')
        self.assertEqual(path_traversal(node, 'ucc'), 'S')
        self.assertEqual(path_traversal(node, 'uca'), 'S')
        self.assertEqual(path_traversal(node, 'ucg'), 'S')
        self.assertEqual(path_traversal(node, 'uau'), 'Y')
        self.assertEqual(path_traversal(node, 'uac'), 'Y')
        self.assertEqual(path_traversal(node, 'uaa'), '*')
        self.assertEqual(path_traversal(node, 'uag'), '*')
        self.assertEqual(path_traversal(node, 'ugu'), 'C')
        self.assertEqual(path_traversal(node, 'ugc'), 'C')
        self.assertEqual(path_traversal(node, 'uga'), '*')
        self.assertEqual(path_traversal(node, 'ugg'), 'W')
        # C Testing
        self.assertEqual(path_traversal(node, 'cuu'), 'L')
        self.assertEqual(path_traversal(node, 'cuc'), 'L')
        self.assertEqual(path_traversal(node, 'cua'), 'L')
        self.assertEqual(path_traversal(node, 'cug'), 'L')
        self.assertEqual(path_traversal(node, 'ccu'), 'P')
        self.assertEqual(path_traversal(node, 'ccc'), 'P')
        self.assertEqual(path_traversal(node, 'cca'), 'P')
        self.assertEqual(path_traversal(node, 'ccg'), 'P')
        self.assertEqual(path_traversal(node, 'cau'), 'H')
        self.assertEqual(path_traversal(node, 'cac'), 'H')
        self.assertEqual(path_traversal(node, 'caa'), 'Q')
        self.assertEqual(path_traversal(node, 'cag'), 'Q')
        self.assertEqual(path_traversal(node, 'cgu'), 'R')
        self.assertEqual(path_traversal(node, 'cgc'), 'R')
        self.assertEqual(path_traversal(node, 'cga'), 'R')
        self.assertEqual(path_traversal(node, 'cgg'), 'R')
        # A Testing
        self.assertEqual(path_traversal(node, 'auu'), 'I')
        self.assertEqual(path_traversal(node, 'auc'), 'I')
        self.assertEqual(path_traversal(node, 'aua'), 'I')
        self.assertEqual(path_traversal(node, 'aug'), 'M')
        self.assertEqual(path_traversal(node, 'acu'), 'T')
        self.assertEqual(path_traversal(node, 'acc'), 'T')
        self.assertEqual(path_traversal(node, 'aca'), 'T')
        self.assertEqual(path_traversal(node, 'acg'), 'T')
        self.assertEqual(path_traversal(node, 'aau'), 'N')
        self.assertEqual(path_traversal(node, 'aac'), 'N')
        self.assertEqual(path_traversal(node, 'aaa'), 'K')
        self.assertEqual(path_traversal(node, 'aag'), 'K')
        self.assertEqual(path_traversal(node, 'agu'), 'S')
        self.assertEqual(path_traversal(node, 'agc'), 'S')
        self.assertEqual(path_traversal(node, 'aga'), 'R')
        self.assertEqual(path_traversal(node, 'agg'), 'R')
        # G Testing
        self.assertEqual(path_traversal(node, 'guu'), 'V')
        self.assertEqual(path_traversal(node, 'guc'), 'V')
        self.assertEqual(path_traversal(node, 'gua'), 'V')
        self.assertEqual(path_traversal(node, 'gug'), 'V')
        self.assertEqual(path_traversal(node, 'gcu'), 'A')
        self.assertEqual(path_traversal(node, 'gcc'), 'A')
        self.assertEqual(path_traversal(node, 'gca'), 'A')
        self.assertEqual(path_traversal(node, 'gcg'), 'A')
        self.assertEqual(path_traversal(node, 'gau'), 'D')
        self.assertEqual(path_traversal(node, 'gac'), 'D')
        self.assertEqual(path_traversal(node, 'gaa'), 'E')
        self.assertEqual(path_traversal(node, 'gag'), 'E')
        self.assertEqual(path_traversal(node, 'ggu'), 'G')
        self.assertEqual(path_traversal(node, 'ggc'), 'G')
        self.assertEqual(path_traversal(node, 'gga'), 'G')
        self.assertEqual(path_traversal(node, 'ggg'), 'G')

if __name__ == '__main__':
    unittest.main()
