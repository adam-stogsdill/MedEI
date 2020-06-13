import numpy as np
import re

class Gene():

    def __init__(self, gene_data : str):
        # Remove non-alphanumeric information from string
        self.__clean_gene_data = re.sub(r'[^atgc]', '', gene_data)

    def __str__(self):
        return self.__clean_gene_data

    @property
    def gene_data(self):
        return self.__clean_gene_data