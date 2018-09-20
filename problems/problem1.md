# Problem 1

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

*Given: A DNA string s of length at most 1000 nt.*

*Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.*

> __Sample Dataset__
> AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

> __Sample Output__
> 20 12 17 21

# Solution

[Python solution](solution1.py)

```python
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../lib'))

# load dna tools library
import dna

dataset = open('datasets/problem1/rosalind_dna.txt')
strand = dataset.read()

print(dna.countnuc(strand))
```
