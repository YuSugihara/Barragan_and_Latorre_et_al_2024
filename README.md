# Data and code for the manuscript: "Multiple horizontal mini-chromosome transfers drive genome evolution of clonal blast fungus lineages"

### Table of contents

1. [Annotate effectors using miniprot](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024?tab=readme-ov-file#1-annotate-effectors-using-miniprot)


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
- [AG006.miniprot.gff3]()
- [Br62.miniprot.gff3]()




| Program    | Version    |
| ---------- | ---------- |
| *miniprot* | v0.13-r248 |