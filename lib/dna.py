from itertools import groupby

def countnuc(strand):
    ##
    ## Count the number of each nucleotides in a given strand of DNA/RNA
    ##
    ## strand - string - Strand of DNA/RNA.
    ##

    anuc, tnuc, cnuc, gnuc, unuc = 0, 0, 0, 0, 0
	
	# ensure no case issues
    strand = strand.upper()

    for c in strand:
        if c == "A":
            anuc += 1
        if c == "T":
            tnuc += 1
        if c == "C":
            cnuc += 1
        if c == "G":
            gnuc += 1
        if c == "U":
            unuc += 1

    # account for RNA strand as well
	# potential to raise exception here if both tnuc and unuc != 0
    if(tnuc == 0):
        tu_nuc = unuc
    else:
        tu_nuc = tnuc

    counts = str(anuc) + " " + str(cnuc) + " " + str(gnuc) + " " + str(tu_nuc)

    return counts

def revcomp(strand):
    ##
    ## Determine the reverse comploment strand to a given DNA strand.
    ##
    ## strand - string - DNA strand you want to generate reverse complement of
    ##

	# define dictionary of complements
    nuc = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    strand.upper()

    comp = ''

    for char in strand:
        comp += nuc[char]

	# comp is 3'->5' direction, problem expects 5'->3' (as do all usual genomics questions)
	# must reverse the entire string to present in correct direction
    revcomp = comp[::-1]
    return revcomp

def translate(rna):
    ##
    ## Translate a given strand of rna into a sequence of proteins identified by their abbreviated letter
    ##
    ## rna - string - RNA strand to translate into protein residues
    ##

    codons = {
        'UUU': 'F',
        'CUU': 'L',
        'AUU': 'I',
        'GUU': 'V',
        'UUC': 'F',
        'CUC': 'L',
        'AUC': 'I',
        'GUC': 'V',
        'UUA': 'L',
        'CUA': 'L',
        'AUA': 'I',
        'GUA': 'V',
        'UUG': 'L',
        'CUG': 'L',
        'AUG': 'M',
        'GUG': 'V',
        'UCU': 'S',
        'CCU': 'P',
        'ACU': 'T',
        'GCU': 'A',
        'UCC': 'S',
        'CCC': 'P',
        'ACC': 'T',
        'GCC': 'A',
        'UCA': 'S',
        'CCA': 'P',
        'ACA': 'T',
        'GCA': 'A',
        'UCG': 'S',
        'CCG': 'P',
        'ACG': 'T',
        'GCG': 'A',
        'UAU': 'Y',
        'CAU': 'H',
        'AAU': 'N',
        'GAU': 'D',
        'UAC': 'Y',
        'CAC': 'H',
        'AAC': 'N',
        'GAC': 'D',
        'UAA': 'Stop',
        'CAA': 'Q',
        'AAA': 'K',
        'GAA': 'E',
        'UAG': 'Stop',
        'CAG': 'Q',
        'AAG': 'K',
        'GAG': 'E',
        'UGU': 'C',
        'CGU': 'R',
        'AGU': 'S',
        'GGU': 'G',
        'UGC': 'C',
        'CGC': 'R',
        'AGC': 'S',
        'GGC': 'G',
        'UGA': 'Stop',
        'CGA': 'R',
        'AGA': 'R',
        'GGA': 'G',
        'UGG': 'W',
        'CGG': 'R',
        'AGG': 'R',
        'GGG': 'G'
    }

    rna.upper()
    protein = ''

    i = 0
    while i < len(rna):
        residue = rna[i:(i+3)]
        if codons[residue] != 'Stop':
            protein += codons[residue]
        i+=3

    print(protein)

def gc_content(dna):
    ##
    ## Determine the gc content of a string of DNA.
    ##
    ## dna - string - strand of dna
    ##
    gsandcs = 0.0

    for char in dna:
        if char == 'G' or char == 'C':
            gsandcs+=1

    gc_per = ((gsandcs/len(dna))*100)

    return gc_per

def fasta_parse(fasta_data):
    ##
    ## Quick parse a fasta file. Just returns header and sequence
    ## Could expand in the future.
    ##
    ## fasta_data - string - file location
    ##

    # input should be a local file location
    fo = open(fasta_data)
    faiter = (x[1] for x in groupby(fo, lambda line: line[0] == ">"))
    for header in faiter:
        # drop the ">"
        header = header.next()[1:].strip()
        # join all sequence lines to one.
        seq = "".join(s.strip() for s in faiter.next())
        yield header, seq

def fib_num(n, k):
    ##
    ## Fibonacci rabbits sequence,
    ## where n = numbers of months,
    ## and k = liters per pair of breeding rabbits

    a, b = 1, 1
    for _ in xrange(n):
        yield a
        a, b = b, (k*a) + b

def hamngdist(s,t):
    ## Calculate the hamming distance between two strings:
    ##
    ## dh(s1,s1) = number of differing nucleotides between two strands
    ##             of the same length
    ##

    if(len(s) != len(t)):
        raise Exception('The two strands not the same length.')

    h, i = 0, 0

    for nuc in s:
        if(s[i] != t[i]):
            h+=1
        i+=1

    return h

def prob_dom_pheno(k,m,n):
    ##
    ## Calculate the probability of two randomly selected mating individuals will
    ## produce offspring with atleast one dominant allele and therefore phenotype,
    ## assuming classical mendelian inheritance.
    ##
    ## k - homozygous dominant individuals within population
    ## m - heterozygous individuals within a population
    ## n - homozygous recessive individuals within popluation
    ##

    ## total population

    t = k + m + n

    ##
    ## Probability of selecting mating pairs
    ##

    ##
    ## Selection of first mating organism
    ##

    k_odds, m_odds, n_odds = (k/t), (m/t), (n/t)

    ##
    ## Selection of second mating organism
    ##

    kk_odds, km_odds, kn_odds = (k-1)/(t-1), (m)/(t-1), (n)/(t-1)
    mm_odds, mk_odds, mn_odds = (m-1)/(t-1), (k)/(t-1), (n)/(t-1)
    nn_odds, nk_odds, nm_odds = (n-1)/(t-1), (k)/(t-1), (n)/(t-1)

    ##
    ## Punnett square odds for dominant phenotype
    ##
    ##  two-homo-dominant = MM x MM = (4/4)
    ##   two-heterozygous = Mm x Mm = (3/4)
    ## two-homo-recessive = mm x mm = (0/4)
    ##      dom-recessive = MM x mm = (4/4)
    ##    hetero-homo-dom = Mm x MM = (4/4)
    ##    hetero-homo-rec = Mm x mm = (1/2)

    two_homo_dominant, two_heterozygous, two_homo_recessive, dom_recessive, hetero_homo_dom, hetero_homo_rec = 1.00, 0.75, 0.00, 1.00, 1.00, 0.50
