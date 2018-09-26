# Problem 1

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

*Given*: A DNA string s of length at most 1000 nt.

*Return*: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

> __Sample Dataset__  
> AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

> __Sample Output__  
> 20 12 17 21

# Solution

[Solution file](solution1.py)

```python
def countnuc(strand):
    anuc, tnuc, cnuc, gnuc, unuc = 0, 0, 0, 0, 0
    strand = strand.upper()

    for c in strand:
        if c == "A":
            anuc += 1
        if c == "T":
            tnuc += 1
        if c == "C":
            cnuc += 1
        if c == "G":
            gnuc += 1
        if c == "U":
            unuc += 1

    # account for RNA strand as well
    if(tnuc == 0):
        tu_nuc = unuc
    else:
        tu_nuc = tnuc

    counts = str(anuc) + " " + str(cnuc) + " " + str(gnuc) + " " + str(tu_nuc)

    return counts

dataset = open('path/to/rosalind/dataset')
strand = dataset.read()

print(countnuc(strand))
```
