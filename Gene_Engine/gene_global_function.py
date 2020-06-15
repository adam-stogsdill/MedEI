import numpy as np
from typing import List, Dict
from math import sqrt

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
    """
    Basically a method that runs a count of the number of times a n_gram occurs in the gene
    """
    result_dictionary = dict()
    for n_gram_set in n_gram_list:
        if n_gram_set in result_dictionary.keys():
            result_dictionary[n_gram_set] += 1
        else:
            result_dictionary[n_gram_set] = 1
    return result_dictionary


def n_gram_gene_similarity(gene1, gene2, n_gram: int):
    """
    n_gram_gene_similarity uses n_grams to create a metric that compares the number of n_grams. While this
    metric does not contain any information such as the order of the n_gram comparison model, it can still
    be useful to see initially how close the gene makeup is.
    """
    vector_sum = 0
    # Find if we should operate on gene1 or gene2
    gene1_n_gram_dict = convert_n_gram_to_dict(grab_n_grams(gene1.gene_data, n_gram))
    gene2_n_gram_dict = convert_n_gram_to_dict(grab_n_grams(gene2.gene_data, n_gram))

    # Equalize size and n-grams
    for key in gene1_n_gram_dict.keys():
        if key not in gene2_n_gram_dict.keys():
            gene2_n_gram_dict[key] = 0

    for key in gene2_n_gram_dict.keys():
        if key not in gene1_n_gram_dict.keys():
            gene1_n_gram_dict[key] = 0

    # At this point both n_grams should have equal size in length assert true. Throw error if not true
    # otherwise the other part of this method will not work.
    try:
        assert(len(gene1_n_gram_dict) == len(gene2_n_gram_dict))
    except AssertionError:
        print("Length of the N_Grams dictionaries are unequal and causing an error in the n_gram_gene_similarity "
              "method!")

    for key in gene1_n_gram_dict.keys():
        vector_sum += (gene1_n_gram_dict[key] - gene2_n_gram_dict[key]) ** 2

    return sqrt(vector_sum)

