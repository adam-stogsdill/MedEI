import pandas as pd
from enum import Enum


class CorpusType(Enum):
    CSV = 0
    SINGLE_FILE = 1
    DIRECTORY = 2


def corpus_loader(corpus_type, corpus):
    if corpus_type == CorpusType.CSV:
        df = pd.read_csv(corpus, )
