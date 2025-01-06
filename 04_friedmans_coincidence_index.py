alphabet = 'abcdefghijklmnopqrstuvwxyz'

english_ci = 0.0656
random_ci = 0.0385


def coincidence_index(text: str) -> float:
    """
    The coincidence index measures the probability that two randomly
    chosen letters in a text are the same.
    """
    length = len(text)
    number_of_pairs = length * (length - 1)
    number_of_matches = 0
    for x in alphabet:
        number_of_matches += text.count(x) * (text.count(x) - 1)
    ci = number_of_matches / number_of_pairs
    return ci


def key_length_guess(text: str) -> float:
    """
    In encryption with poly-alphabetic ciphers, keys repeat periodically.
    Hence, congruent letters and none congruent letters have different
    coincidence indexes. From which the key length may be deduced upon
    comparison with the coincidence index of the entire text.
    """
    text_ci = coincidence_index(text)
    return (english_ci - random_ci) / (text_ci - random_ci)
