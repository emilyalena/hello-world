def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid and contains no characters other than 'A', 'T', 'C', and 'G'.

    >>> is_valid_sequence('ATCGCC')
    True
    >>> is_valid_sequence('ATBC')
    False
    >>> is_valid_sequence('BCC')
    False
    """
    valid = True
    for char in dna:
        if char not in 'ATCG':
            valid = False
    return valid

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequnece obtained by inserting the second DNA sequence into the first DNA sequence at the give nindex.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CAGCTT', 'TTGCA', 4)
    'CAGCTTGCATT'
    """
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    >>> get_complement('B')
    'Not valid nucleotide'
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'C':
        return 'G'
    else:
        return 'Error: not a valid nucleotide'

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('GAC')
    'CTG'
    >>> get_complementary_sequence('ATGCGTTA')
    'TACGCAAT'
    """
    dna_sequence = ''
    for char in dna:
        if char == 'A':
            dna_sequence = dna_sequence + 'T'
        elif char == 'T':
            dna_sequence = dna_sequence + 'A'
        elif char == 'C':
            dna_sequence = dna_sequence + 'G'
        elif char == 'G':
            dna_sequence = dna_sequence + 'C'
        else:
            return 'Error: not a valid dna sequence'
    return dna_sequence
