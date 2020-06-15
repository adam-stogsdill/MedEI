import numpy as np
import re

from Gene_Engine import gene_global_function
from typing import List


class Gene:

    def __init__(self, gene_data: str):
        # Remove non-alphanumeric information from string
        self.__clean_gene_data = re.sub(r'[^atgc]', '', gene_data.lower())
        self.__vectorization = gene_global_function.convert_to_numpy_object(self.__clean_gene_data)

    def __str__(self):
        return self.__clean_gene_data

    @property
    def gene_data(self):
        return self.__clean_gene_data


class PreloadedDataGene(Gene):
    """
    Pre-loaded Data Gene acts as Gene subclass and contains any needed pre-calculated values. This will allow for
    pipeline speed up times while requiring data sources up front. For late stage calculations this will allow the user
    to create objects that also have much more detail to them. For simple one-time gene calculations it is probably
    much faster and more efficient to simply use the general Gene class.
    """

    def __init__(self, gene_data: str, n_gram_calculations: List[int], append = True):
        super().__init__(gene_data)
        self.__n_gram_calculations = None

