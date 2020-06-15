# This is a python file to test to unit testing specifically on gene_base code
import unittest
from Gene_Engine.gene_base import Gene
from Gene_Engine.gene_global_function import convert_to_numpy_object
import numpy as np


class InitializationTesting(unittest.TestCase):

    def test_clean_gene_initialization(self):
        print("Testing for gene_data initialization errors!")
        self.assertEqual("tcga", Gene("543\ntc90!][2kdjga").gene_data)
        print("gene_data initialized correctly!")

    def test_vectorization_of_gene(self):
        print("Testing the vectorization of TCGA")
        vectorization = convert_to_numpy_object(Gene("543\ntc90!][2kdjga").gene_data)
        vectorization_check = np.asarray([[0, 1, 0, 0],
                                          [0, 0, 1, 0],
                                          [0, 0, 0, 1],
                                          [1, 0, 0, 0]])
        comparison_data = vectorization == vectorization_check
        self.assertTrue(comparison_data.all())
        print("Gene Vectorization works correctly!")


class GeneGlobalFunctionTesting(unittest.TestCase):

    def n_gram_testing(self):
        pass


if __name__ == '__main__':
    unittest.main()
