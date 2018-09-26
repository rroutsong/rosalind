# insert rosalind problem libs into system path
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../lib'))

# import the rosalind dna library
import dna

rosalindinput = open('datasets/problem3/rosalind_revc.txt')
strand = rosalindinput.read()
# scrub line breaks
strand = strand.rstrip('\n')

print('Anwser to problem 3: ')
print('---------------------')
print(dna.revcomp(strand))
