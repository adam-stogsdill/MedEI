import numpy as np
import re

from Gene_Engine import gene_global_function


class Gene:

    def __init__(self, gene_data: str):
        # Remove non-alphanumeric information from string
        self.__clean_gene_data = re.sub(r'[^atgc]', '', gene_data.lower())
        self.__vectorization = gene_global_function.convert_to_numpy_object(self.__clean_gene_data)
        print(gene_global_function.grab_n_grams(self.__clean_gene_data, 4))

    def __str__(self):
        return self.__clean_gene_data

    @property
    def gene_data(self):
        return self.__clean_gene_data

