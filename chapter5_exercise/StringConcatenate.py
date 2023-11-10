def string_concatenate(word: str):
    length_of_word = len(word)
    if length_of_word == 3:
        return word + "ing"


def string_concatenate2(word: str):
    if word.endswith('ing'):
        return word + 'ly'


def String_concatenate3(word: str):
    if len(word) < 3:
        return word
