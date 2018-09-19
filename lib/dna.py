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
    
    k-odds, m-odds, n-odds = (k/t), (m/t), (n/t)
    
    ##
    ## Selection of second mating organism
    ##
    
    kk-odds, km-odds, kn-odds = (k-1)/(t-1), (m)/(t-1), (n)/(t-1)
    mm-odds, mk-odds, mn-odds = (m-1)/(t-1), (k)/(t-1), (n)/(t-1)
    nn-odds, nk-odds, nm-odds = (n-1)/(t-1), (k)/(t-1), (n)/(t-1)
    
    ##
    ## Punnett square odds for dominant phenotype
    ##
    ##  two-homo-dominant = MM x MM = (4/4)
    ##   two-heterozygous = Mm x Mm = (3/4)
    ## two-homo-recessive = mm x mm = (0/4)
    ##      dom-recessive = MM x mm = (4/4)
    ##    hetero-homo-dom = Mm x MM = (4/4)
    ##    hetero-homo-rec = Mm x mm = (1/2)
    
    two-homo-dominant, two-heterozygous, two-homo-recessive, dom-recessive, hetero-homo-dom, hetero-homo-rec = 1.00, 0.75, 0.00, 1.00, 1.00, 0.50