from itertools import groupby

def revcomp(dna):
    nuc = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    reverse = ''
    
    for char in dna:
        reverse += nuc[char]
        
    return reverse[::-1]
    
def gc_content(dna):
    gsandcs = 0.0
    
    for char in dna:
        if char == 'G' or char == 'C':
            gsandcs+=1
    
    gc_per = ((gsandcs/len(dna))*100)
    
    return gc_per
    
def fasta_parse(fasta_data):
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