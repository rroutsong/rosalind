# insert rosalind problem libs into system path
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../lib'))

import dna

file = open('datasets/problem8/rosalind_prot.txt')
rna = file.read()
rna = rna.rstrip('\n').rstrip('\r')

dna.translate(rna)
