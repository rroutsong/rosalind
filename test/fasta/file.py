# parse fasta, determine highest gc_content and return results
import dna

fidna = dna.fasta_parse('FASTA.fas')

gc_highest = ['', 0]

for i in fidna:
    if(dna.gc_content(i[1])>gc_highest[1]):
        gc_highest = [i[0], dna.gc_content(i[1])]

print gc_highest[0] + '\n' + str(gc_highest[1])