# encoding: utf-8

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from operator import itemgetter, attrgetter, methodcaller
from fp_growth import find_frequent_itemsets
import matplotlib.pyplot as plt

# Fatch sequence from ebola.fasta file
datas = {}
input_file = "./ebola.fasta"
fasta_sequences = SeqIO.parse(open(input_file),'fasta')
for fasta in fasta_sequences:
    name, sequence = fasta.id, str(fasta.seq)
    datas[name] = sequence
fasta_sequences.close()

# use dynamic programming to alignment two sequence
def alignment(a, b):
    result = pairwise2.align.globalxx(a, b)
    #result = pairwise2.align.globalmx(a, b, 2, 1)
    result = sorted(result, key=itemgetter(2), reverse=True)
    result =  sorted(result, key=itemgetter(4), reverse=True)
    return result[0]

def common(a, b):
    return [i for i, j in zip(a, b) if i == j]

def calculate_different(dicts):
    pivot = dicts.popitem()
    result = {}
    for key, value in dicts.iteritems():
        result[key] = (alignment(pivot[1], value)[2])/len(value);
        print result[key]
    return result

cal_dif = calculate_different(datas)

plt.plot(cal_dif.values(), 'ro')
plt.axis([0, 42, 0, 1])
plt.show()

#print format_alignment(*r)
#print format_alignment(*r1)
