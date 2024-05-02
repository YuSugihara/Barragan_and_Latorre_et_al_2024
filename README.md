# Data and code for the manuscript: "Multiple horizontal mini-chromosome transfers drive genome evolution of clonal blast fungus lineages"

### Table of contents

1. [Annotate effectors using miniprot](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024?tab=readme-ov-file#1-annotate-effectors-using-miniprot)




## 1. Annotate effectors using miniprot
To complement the effector annotation of BRAKER, we used miniprot and aligned two effector datasets ([Petit-Houdenot et al., 2020](https://doi.org/10.1094/MPMI-03-20-0052-A); [Yan et al., 2023](https://doi.org/10.1093/plcell/koad036)) to [AG006 and Br62 genomes](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/tree/main/1_genomes).

First, we merged two effector datasets into a single file.
```

```



```bash
miniprot -t 2 \
         -G 3k \
         -P SEC \
         -p 0.3 \
         --outs=0.5 \
         --gff \
         $1 \
         ./effector_dataset.fa \
         2> ${PREFIX}/${PREFIX}.miniprot.log | \
grep -v "##PAF" > ${PREFIX}/${PREFIX}.miniprot.gff3
```



| Program    | Version    |
| ---------- | ---------- |
| *miniprot* | v0.13-r248 |