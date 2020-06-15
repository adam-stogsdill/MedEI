import numpy as np
from typing import List, Dict

letter_to_quantitative_gene_sequence = {
    'a': np.asarray([[1, 0, 0, 0]]),
    't': np.asarray([[0, 1, 0, 0]]),
    'c': np.asarray([[0, 0, 1, 0]]),
    'g': np.asarray([[0, 0, 0, 1]])
}


def convert_to_numpy_object(gene_data: str):
    """
    Method designed to convert gene_data to numpy array.
    """
    # Create empty numpy array and then delete the first row
    result = np.asarray([[0, 0, 0, 0]])
    for nucleotide_base in gene_data:
        result = np.append(result, letter_to_quantitative_gene_sequence.get(nucleotide_base), axis=0)
    return np.delete(result, 0, axis=0)


def grab_n_grams(gene_data: str, n_gram_length=1) -> List[str]:
    return [gene_data[i: i + n_gram_length] for i in range(len(gene_data)) if i + n_gram_length <= len(gene_data)]

def convert_n_gram_to_dict(n_gram_list: List[str]) -> Dict:



def n_gram_gene_similarity(gene1, gene2, n_pair: int):
    """
    n_gram_gene_similarity uses n_grams to create a metric that compares the number of n_grams
    """
    pass
