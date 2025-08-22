import string


def is_pangram(sentence):
    sentence_set = set(sentence.lower())  
    return sentence_set.issuperset(set(string.ascii_lowercase))