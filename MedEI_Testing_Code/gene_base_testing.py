# This is a python file to test to unit testing specifically on gene_base code
import unittest
from Gene_Engine.gene_base import Gene

class InitializationTesting(unittest.TestCase):

    def test_clean_gene_initialization(self):
        print("Testing for gene_data initialization errors!")
        self.assertEqual("543\ntc902kdjga", Gene("tcga").gene_data)
        print("gene_data initialized correctly!")

if __name__ == '__main__':
    unittest.main()