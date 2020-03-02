import nltk
from nltk.corpus import BracketParseCorpusReader

q_bank = nltk.corpus.BracketParseCorpusReader("./", "questionbank.txt")

print q_bank.parsed_sents()[0]
