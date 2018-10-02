# Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

*Given*: A DNA string t having length at most 1000 nt.

*Return*: The transcribed RNA string of t.

> __Sample Dataset__  
> GATGGAACTTGACTACGTAAATT

> __Sample Output__  
> GAUGGAACUUGACUACGUAAAUU

# Solution

[Solution file](solution2.py)

```python
strand = open('path/to/rosalind/dataset')
strand_dna = strand.read()
strand_rna = ''

# ensure input is all uppercase
strand_dna.upper()

for c in strand_dna:
    if c == 'T':
        strand_rna += 'U'
    else:
        strand_rna += c

print(strand_rna)
```
