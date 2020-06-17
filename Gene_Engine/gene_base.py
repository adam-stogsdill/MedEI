import numpy as np
import re
from Gene_Engine.gene_global_function import convert_to_numpy_object, grab_n_grams, convert_n_gram_to_dict
from Gene_Engine.CodonTreeNode import construct_codon_translation_tree, path_traversal
from typing import List
from enum import Enum


class Encoding(Enum):
    """
    Reveal to the code whether the code given to the data is DNA, RNA, or CODON FORMATTING. Will be very useful
    for translation and manipulation further. At some point we want to mostly work with CODON encoding but
    should still allow for DNA and RNA nucleotide operations.
    """
    DNA = 0
    RNA = 1
    CODON = 2


codon_translation_tree = construct_codon_translation_tree()


class Gene:

    def __init__(self, name: str, gene_data: str, encoding: Encoding = Encoding.DNA):
        self.name = name
        # Remove non-alphanumeric information from string
        if encoding == Encoding.DNA:
            self.__clean_gene_data = re.sub(r'[^atgc]', '', gene_data.lower())
            self.__vectorization = convert_to_numpy_object(self.__clean_gene_data)
            self.__translation()
        else:
            print("Program only allows for DNA samples currently!")

    def __str__(self):
        return self.__clean_gene_data

    @property
    def gene_data(self):
        return self.__clean_gene_data

    def __translation(self):
        # Translate DNA to RNA
        self.__rna_translation = "".join(['u' if nucleotide == 't' else nucleotide for nucleotide in self.gene_data])
        self.__codon_translation = [path_traversal(codon_translation_tree, tri_gram) for tri_gram in
                                    grab_n_grams(self.__rna_translation, 3)]

    def general_stats(self):
        pass


class PreloadedDataGene(Gene):
    """
    Pre-loaded Data Gene acts as Gene subclass and contains any needed pre-calculated values. This will allow for
    pipeline speed up times while requiring data sources up front. For late stage calculations this will allow the user
    to create objects that also have much more detail to them. For simple one-time gene calculations it is probably
    much faster and more efficient to simply use the general Gene class.
    """

    def __init__(self, name: str, gene_data: str, n_gram_calculations: List[int], append=True):
        super().__init__(name, gene_data)
        self.append = append
        self.__n_gram_calculations = {n_gram_length: convert_n_gram_to_dict(grab_n_grams(self.gene_data, n_gram_length))
                                      for n_gram_length in n_gram_calculations}
