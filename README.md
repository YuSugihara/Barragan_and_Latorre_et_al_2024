# Data and code for the manuscript: "Multiple horizontal mini-chromosome transfers drive genome evolution of clonal blast fungus lineages"

### Table of contents

1. [Annotate effectors using miniprot](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024?tab=readme-ov-file#1-annotate-effectors-using-miniprot)


The BRAKER annotation was complemented by the alignment of two effector datasets (Petit-Houdenot et al., 2020; Yan et al., 2023) to the genomes using miniprot v0.13-r248 with the options "-G 3k -p 0.3 --outs=0.5 --gff" (Li, 2023). We then extracted the coding sequences (CDSs) in nucleotide form from both BRAKER and miniprot GFF files using gffread v0.12.7 (Pertea & Pertea, 2020). Based on the extracted sequences, we filtered out the gene models that lacked complete codons, contained a premature stop codon within the CDS, did not start with a start codon, or were shorter than 150 bases. BRAKER and miniprot annotations were merged using gffread with the options "--sort-alpha --force-exons -M -K". To plot the distribution of gene models, we used their middle positions. When a locus had multiple alternative transcripts, we used the middle position of the locus region and regarded them as a single gene. When one of the alternative transcripts was derived from miniprot or predicted as a putative secreted protein, that locus was regarded as coding for a putative secreted protein. We used the 'cut' function from the Python library 'pandas' v2.2.1 to count how many genes are in each window. To plot the distribution of repetitive sequences, we counted how many soft-masked bases are in each window.

## 1. Annotate effectors using miniprot
To complement the effector annotation of BRAKER, we used miniprot and aligned two effector datasets.(Petit-Houdenot et al., 2020; Yan et al., 2023) to the [genomes]().


| Program    | Version    |
| ---------- | ---------- |
| *miniprot* | v0.13-r248 |