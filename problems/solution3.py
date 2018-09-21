# insert rosalind problem libs into system path
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../lib'))

# import the rosalind dna library
import dna

file = open('datasets/problem3/rosalind_revc.txt')
strand = file.read()
strand = strand.rstrip('\n')

print(dna.revcomp(strand))
