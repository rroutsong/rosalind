# insert rosalind problem libs into system path
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../lib'))

# import the rosalind dna library
import dna

dataset = open('datasets/problem1/rosalind_dna.txt')
strand = dataset.read()

print('Anwser to problem 1: ')
print('---------------------')
print(dna.countnuc(strand))
