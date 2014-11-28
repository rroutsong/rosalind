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