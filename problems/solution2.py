file = open('datasets/problem2/rosalind_rna.txt')
strand_dna = file.read()
strand_rna = ''

strand_dna.upper()

for c in strand_dna:
    if c == 'T':
        strand_rna += 'U'
    else:
        strand_rna += c

print(strand_rna)
