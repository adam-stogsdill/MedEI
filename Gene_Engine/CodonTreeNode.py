from typing import List


class Node(object):

    def __init__(self, value: str, nodes=None, leaf_value=""):
        if nodes is None:
            nodes = []
        self.value = value
        self.nodes = nodes
        self.leaf_value = leaf_value

    def append_node(self, node):
        self.nodes.append(node)

    def get(self, nucleotide):
        for x in self.nodes:
            if x.value == nucleotide:
                return True, x
        return False, None

    def get_node(self, nucleotide):
        for x in self.nodes:
            if x.value == nucleotide:
                return x
        return None

    def get_leaf_value(self):
        return self.leaf_value

    def set_leaf_value(self, leaf_value):
        self.leaf_value = leaf_value


def create_traversal_path(initial_node, path, final_value):
    if len(path) == 0:
        initial_node.set_leaf_value(final_value)
    elif type(path[0]) == list:
        for x in path[0]:
            initial_node.append_node(Node(x, leaf_value=final_value))
    else:
        contains_nucl, first_node = initial_node.get(path[0])
        # If our initial node does not contain the node create the node and append it to the initial node.
        if not contains_nucl:
            first_node = Node(path[0], leaf_value='')
            initial_node.append_node(first_node)

        # If the length of the path is zero pass it an empty list to then be caught by the first recursive end condition
        if len(path) == 1:
            create_traversal_path(first_node, [], final_value)
        else:
            create_traversal_path(first_node, path[1:], final_value)
    return


def path_traversal(initial_node, path):
    if initial_node.get_leaf_value() != "":
        return initial_node.get_leaf_value()
    node = initial_node.get_node(path[0])
    return path_traversal(node, path[1:])


def construct_codon_translation_tree():
    initial_node = Node("")
    codon_array = [
        # U's
        [['u', 'u', ['u', 'c']], 'F'],
        [['u', 'u', ['a', 'g']], 'L'],
        [['u', 'c'], 'S'],
        [['u', 'a', ['u', 'c']], 'Y'],
        [['u', 'a', ['a', 'g']], 'STOP'],
        [['u', 'g', ['u', 'c']], 'C'],
        [['u', 'g', 'a'], 'STOP'],
        [['u', 'g', 'g'], 'W'],
        # C's
        [['c', 'u'], 'L'],
        [['c', 'c'], 'P'],
        [['c', 'g'], 'A'],
        [['c', 'a', ['c', 'u']], 'H'],
        [['c', 'a', ['g', 'a']], 'H'],
        # A's
        [['a', 'u', ['a', 'c', 'u']], 'I'],
        [['a', 'u', 'g'], 'M'],
        [['a', 'c'], 'T'],
        [['a', 'a', ['g', 'a']], 'K'],
        [['a', 'a', ['c', 'u']], 'N'],
        [['a', 'g', ['g', 'a']], 'R'],
        [['a', 'g', ['c', 'u']], 'S'],
        # G's
        [['g', 'u'], 'V'],
        [['g', 'c'], 'A'],
        [['g', 'a', ['u', 'c']], 'D'],
        [['g', 'a', ['g', 'a']], 'E'],
        [['g', 'g'], 'G'],
    ]

    for values in codon_array:
        create_traversal_path(initial_node, values[0], values[1])

    return initial_node



