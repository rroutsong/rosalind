# Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

*Given*: A DNA string s of length at most 1000 bp.

*Return*: The reverse complement sc of s.

> __Sample Dataset__
> AAAACCCGGT

> __Sample Output__
> ACCGGGTTTT

# Solution

[Solution file](solution3.py)

```python
def revcomp(strand):
	# define dictionary of complements
    nuc = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

	# ensure no issues due to case
    strand.upper()

    comp = ''

    for char in strand:
        comp += nuc[char]
	
	# comp is 3'->5' direction, problem expects 5'->3' (as do all usual genomics questions)
	# must reverse the entire string to present in correct direction
    revcomp = comp[::-1]
	
    return revcomp
end

rosalindinput = open('path/to/rosalind/dataset')
strand = rosalindinput.read()

# scrub line breaks
strand = strand.rstrip('\n')

print(revcomp(strand))
```