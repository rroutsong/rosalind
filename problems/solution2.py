strand = open('datasets/problem2/rosalind_rna.txt')
strand_dna = strand.read()
strand_rna = ''

# ensure no issues due to case
strand_dna.upper()

for c in strand_dna:
    if c == 'T':
        strand_rna += 'U'
    else:
        strand_rna += c

print('Anwser to problem 1: ')
print('---------------------')
print(strand_rna)
