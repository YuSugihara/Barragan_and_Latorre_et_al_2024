# Data and code for the manuscript: "Multiple horizontal mini-chromosome transfers drive genome evolution of clonal blast fungus lineages"

### Table of contents

1. [Annotate effectors using miniprot](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024?tab=readme-ov-file#1-annotate-effectors-using-miniprot)
2. [Filter and merge gene models](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/tree/main#2-filter-and-merge-gene-models)




## 1. Annotate effectors using miniprot
To complement the effector annotation of BRAKER, we used miniprot and aligned two effector datasets ([Petit-Houdenot et al., 2020](https://doi.org/10.1094/MPMI-03-20-0052-A); [Yan et al., 2023](https://doi.org/10.1093/plcell/koad036)) to [AG006 and Br62 genomes](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/tree/main/2_genomes).

First, we merged two effector datasets into a single file.
```
cat 178_MO_effectors.fa \
    Moryzae_MG8_XiaYan_secretome.fa > \
    effector_dataset.fa
```
**Input files:**
- [178_MO_effectors.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/1_effector_dataset/178_MO_effectors.fa): Effector dataset published in [Petit-Houdenot et al., 2020](https://doi.org/10.1094/MPMI-03-20-0052-A)
- [Moryzae_MG8_XiaYan_secretome.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/1_effector_dataset/Moryzae_MG8_XiaYan_secretome.fa): Effector dataset published in [Yan et al., 2023](https://doi.org/10.1093/plcell/koad036)

**Output files:**
- [effector_dataset.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/1_effector_dataset/effector_dataset.fa): Merged effector dataset

We then aligned the effector dataset to the genomes using miniprot.


```bash
miniprot -t 2 \
         -G 3k \
         -P SEC \
         -p 0.3 \
         --outs=0.5 \
         --gff \
         AG006.fa \
         effector_dataset.fa | \
grep -v "##PAF" > AG006.miniprot.gff3

miniprot -t 2 \
         -G 3k \
         -P SEC \
         -p 0.3 \
         --outs=0.5 \
         --gff \
         Br62.fa \
         effector_dataset.fa | \
grep -v "##PAF" > Br62.miniprot.gff3
```
**Input files:**
- [AG006.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/AG006.fa): *M. oryzae* AG006 genome
- [Br62.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/Br62.fa): *M. oryzae* Br62 genome
- [effector_dataset.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/1_effector_dataset/effector_dataset.fa): Merged effector dataset

**Output files:**
- [AG006.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/AG006.miniprot.gff3): miniprot annotation of AG006
- [Br62.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/Br62.miniprot.gff3): miniprot annotation of Br62

## 2. Filter and merge gene models

We extracted CDS from both BRAKER and miniprot annotations using gffread.

```bash
gffread -g AG006.fa -x AG006.cds.fa AG006.gff3
gffread -g AG006.fa -x AG006.miniprot.cds.fa AG006.miniprot.gff3
gffread -g Br62.fa -x Br62.cds.fa Br62.gff3
gffread -g Br62.fa -x Br62.miniprot.cds.fa Br62.miniprot.gff3
```

***Input files:*
- [AG006.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/AG006.fa): *M. oryzae* AG006 genome
- [Br62.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/Br62.fa): *M. oryzae* Br62 genome
- [AG006.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/AG006.gff3): BRAKER annotation of AG006
- [Br62.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/Br62.gff3): BRAKER annotation of Br62
- [AG006.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/AG006.miniprot.gff3): miniprot annotation of AG006
- [Br62.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/Br62.miniprot.gff3): miniprot annotation of Br62

**Output files:**
- [AG006.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/AG006.cds.fa): CDS extracted from BRAKER annotation of AG006
- [Br62.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/Br62.cds.fa): CDS extracted from BRAKER annotation of Br62
- [AG006.miniprot.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/AG006.miniprot.cds.fa): CDS extracted from miniprot annotation of AG006
- [Br62.miniprot.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/Br62.miniprot.cds.fa): CDS extracted from miniprot annotation of Br62

Using [gff_qc.py](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/gff_qc.py), we added new columns to the GFF files to annotate gene models that lacked complete codons, contained a premature stop codon within the CDS, did not start with a start codon, or were shorter than 150 bases.

```bash
# Usage:
# gff_qc.py <input_GFF3> \
#           <input_CDS_FASTA> \
#           <min_nt_length_check_points> \
#           <repeat_masking_%_check_points> \
#           1> <GFF3_with_qc_annotation_columns> \
#           2> <list_of_annotations>

gff_qc.py AG006.gff3 \
          AG006.cds.fa \
          150,180,195 \
          10,25,50 \
          1> AG006.braker_qc.gff3 \
          2> AG006.braker_qc.txt

gff_qc.py Br62.gff3 \
          Br62.cds.fa \
          150,180,195 \
          10,25,50 \
          1> Br62.braker_qc.gff3 \
          2> Br62.braker_qc.txt

gff_qc.py AG006.miniprot.gff3 \
          AG006.miniprot.cds.fa \
          150,180,195 \
          10,25,50 \
          1> AG006.miniprot_qc.gff3 \
          2> AG006.miniprot_qc.txt

gff_qc.py Br62.miniprot.gff3 \
          Br62.miniprot.cds.fa \
          150,180,195 \
          10,25,50 \
          1> Br62.miniprot_qc.gff3 \
          2> Br62.miniprot_qc.txt
```

**Input files:**
- [AG006.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/AG006.gff3): BRAKER annotation of AG006
- [AG006.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/AG006.cds.fa): CDS extracted from BRAKER annotation of AG006
- [Br62.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/Br62.gff3): BRAKER annotation of Br62
- [Br62.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/Br62.cds.fa): CDS extracted from BRAKER annotation of Br62
- [AG006.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/AG006.miniprot.gff3): miniprot annotation of AG006
- [AG006.miniprot.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/AG006.miniprot.cds.fa): CDS extracted from miniprot annotation of AG006
- [Br62.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/Br62.miniprot.gff3): miniprot annotation of Br62
- [Br62.miniprot.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/Br62.miniprot.cds.fa): CDS extracted from miniprot annotation of Br62

**Output files:**
- [AG006.braker_qc.gff3](): BRAKER annotation of AG006 with QC annotations
- [AG006.braker_qc.txt](): List of QC annotations for AG006 BRAKER annotation
- [Br62.braker_qc.gff3](): BRAKER annotation of Br62 with QC annotations
- [Br62.braker_qc.txt](): List of QC annotations for Br62 BRAKER annotation


| Program    | Version    |
| ---------- | ---------- |
| *miniprot* | v0.13-r248 |
| *gffread*  | v0.12.7    |
| *python*   | v3.10.14   |
| *biopyhon* | v1.83      |
| *pandas*   | v2.2.1     |
