"""Hamming Distance from Exercism"""


def distance(strand_a, strand_b):
    """Determine the hamming distance between two RNA strings
    param: str strand_a
    param: str strand_b
    return: int calculation of the hamming distance between strand_a and strand_b
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    distance = 0

    for i, _ in enumerate(strand_a):
        if strand_a[i] != strand_b[i]:
            distance += 1

    return distance
