# This is a python file to test to unit testing specifically on gene_base code
import unittest
from Gene_Engine.gene_base import Gene
from Gene_Engine.gene_global_function import convert_to_numpy_object, n_gram_gene_similarity, gene_match
import numpy as np


class InitializationTesting(unittest.TestCase):

    def test_clean_gene_initialization(self):
        print("Testing for gene_data initialization errors!")
        self.assertEqual("tcga", Gene("Name", "543\ntc90!][2kdjga").gene_data)
        print("gene_data initialized correctly!")

    def test_file_reading(self):
        gene = open('F:/MedEI/gene_samples/testing_sample', 'r')
        self.assertEqual(Gene("Name", "".join([line for line in gene])).gene_data,
                         "GTGCTCTAAAATGTCAATTTGCATCTCAAAGACTGCAAACTTGTATGCCTTAAAATGGTGCCATTACCGT".lower())
        gene.close()

    def test_vectorization_of_gene(self):
        print("Testing the vectorization of TCGA")
        vectorization = convert_to_numpy_object(Gene("Name", "543\ntc90!][2kdjga").gene_data)
        vectorization_check = np.asarray([[0, 1, 0, 0],
                                          [0, 0, 1, 0],
                                          [0, 0, 0, 1],
                                          [1, 0, 0, 0]])
        comparison_data = vectorization == vectorization_check
        self.assertTrue(comparison_data.all())
        print("Gene Vectorization works correctly!")


class GeneGlobalFunctionTesting(unittest.TestCase):

    def test_n_gram_similarity(self):
        print("Testing Similarity Metric")
        gene1 = Gene("None", "543\ntc90!][2kdjga")
        gene2 = Gene("None", "543\ntc90!][2kdjga")
        self.assertTrue(n_gram_gene_similarity(gene1, gene2, 1) == 0)
        print("Similarity Metric check passed")

    def test_match_method(self):
        print("Testing if genes are a match!")
        gene1 = Gene("None", "543\ntc90!][2kdjga")
        gene2 = Gene("None", "543\ntc90!][2kdjga")
        gene3 = Gene("None", "543\ntc90!][2kdjgaa")
        self.assertTrue(gene_match(gene1, gene2))
        self.assertFalse(gene_match(gene1, gene3))
        print("Genes match properly!")


if __name__ == '__main__':
    unittest.main()
