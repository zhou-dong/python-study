# Analyze fasta data of Ebola

## Description




## Data

Dataset: http://hgdownload.soe.ucsc.edu/goldenPath/eboVir3/ebolaAbSequences.fasta

Data Format: Fasta

```
    >gi|166007127|pdb|2QHR|H Chain H, Crystal Structure Of The 13f6-1-2 Fab Fragment Bound To Its Ebola Virus Glycoprotein Peptide Epitope.|pmid|18005986
    EVQVVESGGGLVKPGGSLKLSCAASGFAFSSYDMSWVRQTPEKRLEWVAYISRGGGYTYYPDTVKGRFTI
    SRDNAKNTLYLQMSSLKSEDTAMYYCSRHIYYGSSHYYAMDYWGQGTSVTVSSAKTTAPSVYPLAPVCGD
    TTGSSVTLGCLVKGYFPEPVTLTWNSGSLSSGVHTFPAVLQSDLYTLSSSVTVTSSTWPSQSITCNVAHP
    ASSTKVDKKIEP
```

## Development Lauguage

- Language: python

## Algorithm

- FP-Growth
- Dynamic programming


## Python Package:

- Biopython
- python-fp-growth
- matplotlib

### Install FP-growth:

    git clone https://github.com/enaeseth/python-fp-growth.git
    cd python-fp-growth
    python setup.py install
    or 
    sudo python setup.py install

### Test FP-Growth

    python -m fp_growth -s 4 examples/tsk.csv
