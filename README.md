# Data and code for the manuscript: "Multiple horizontal mini-chromosome transfers drive genome evolution of clonal blast fungus lineages"

### Table of contents

1. [Complement effector annotations using miniprot](#1-complement-effector-annotations-using-miniprot)
2. [Filter gene models](#2-filter-gene-models)
3. [Merge gene models](#3-merge-gene-models)
4. [Plot genome features](#4-plot-genome-features)
5. [Annotate proteins using InterProScan](#5-annotate-proteins-using-interproscan)
6. [Version information](#6-version-information) 

## 1. Complement effector annotations using miniprot
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
- [AG006.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/AG006.fa): AG006 genome
- [Br62.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/Br62.fa): Br62 genome
- [effector_dataset.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/1_effector_dataset/effector_dataset.fa): Merged effector dataset

**Output files:**
- [AG006.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/AG006.miniprot.gff3): miniprot annotation of AG006
- [Br62.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/Br62.miniprot.gff3): miniprot annotation of Br62

## 2. Filter gene models

We extracted CDS from both BRAKER and miniprot annotations using gffread.

```bash
gffread -g AG006.fa -x AG006.cds.fa AG006.gff3
gffread -g AG006.fa -x AG006.miniprot.cds.fa AG006.miniprot.gff3
gffread -g Br62.fa -x Br62.cds.fa Br62.gff3
gffread -g Br62.fa -x Br62.miniprot.cds.fa Br62.miniprot.gff3
```

***Input files:**
- [AG006.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/AG006.fa): AG006 genome
- [Br62.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/Br62.fa): Br62 genome
- [AG006.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/AG006.gff3): BRAKER annotation of AG006
- [Br62.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/Br62.gff3): BRAKER annotation of Br62
- [AG006.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/AG006.miniprot.gff3): miniprot annotation of AG006
- [Br62.miniprot.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/Br62.miniprot.gff3): miniprot annotation of Br62

**Output files:**
- [AG006.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/AG006.cds.fa): CDS extracted from BRAKER annotation of AG006
- [Br62.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/Br62.cds.fa): CDS extracted from BRAKER annotation of Br62
- [AG006.miniprot.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/AG006.miniprot.cds.fa): CDS extracted from miniprot annotation of AG006
- [Br62.miniprot.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/3_miniprot_annotation/Br62.miniprot.cds.fa): CDS extracted from miniprot annotation of Br62

Using [gff_qc.py](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/scripts/gff_qc.py), we added new columns to the GFF files to annotate gene models for QC (quality control).

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
- [AG006.braker_qc.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.braker_qc.gff3): BRAKER annotation of AG006 with QC annotations
- [AG006.braker_qc.txt](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.braker_qc.txt): List of QC annotations for AG006 BRAKER annotation
- [Br62.braker_qc.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.braker_qc.gff3): BRAKER annotation of Br62 with QC annotations
- [Br62.braker_qc.txt](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.braker_qc.txt): List of QC annotations for Br62 BRAKER annotation
- [AG006.miniprot_qc.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.miniprot_qc.gff3): miniprot annotation of AG006 with QC annotations
- [AG006.miniprot_qc.txt](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.miniprot_qc.txt): List of QC annotations for AG006 miniprot annotation
- [Br62.miniprot_qc.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.miniprot_qc.gff3): miniprot annotation of Br62 with QC annotations
- [Br62.miniprot_qc.txt](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.miniprot_qc.txt): List of QC annotations for Br62 miniprot annotation


We filtered out gene models that lacked complete codons, contained a premature stop codon within the CDS, did not start with a start codon, or were shorter than 150 bases.

```bash
grep -v 'not_multiple_of_3' AG006.braker_qc.gff3  | \
grep -v 'stop_codon_in_cds' | \
grep -v 'no_start_codon' | \
grep -v 'shorter_than_150nt' | \
cut -f 1-9 > \
AG006.braker_qc.filtered.gff3

grep -v 'not_multiple_of_3' AG006.miniprot_qc.gff3  | \
grep -v 'stop_codon_in_cds' | \
grep -v 'no_start_codon' | \
grep -v 'shorter_than_150nt' | \
cut -f 1-9 > \
AG006.miniprot_qc.filtered.gff3

grep -v 'not_multiple_of_3' Br62.braker_qc.gff3  | \
grep -v 'stop_codon_in_cds' | \
grep -v 'no_start_codon' | \
grep -v 'shorter_than_150nt' | \
cut -f 1-9 > \
Br62.braker_qc.filtered.gff3

grep -v 'not_multiple_of_3' Br62.miniprot_qc.gff3  | \
grep -v 'stop_codon_in_cds' | \
grep -v 'no_start_codon' | \
grep -v 'shorter_than_150nt' | \
cut -f 1-9 > \
Br62.miniprot_qc.filtered.gff3
```

**Input files:**
- [AG006.braker_qc.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.braker_qc.gff3): BRAKER annotation of AG006 with QC annotations
- [Br62.braker_qc.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.braker_qc.gff3): BRAKER annotation of Br62 with QC annotations
- [AG006.miniprot_qc.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.miniprot_qc.gff3): miniprot annotation of AG006 with QC annotations
- [Br62.miniprot_qc.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.miniprot_qc.gff3): miniprot annotation of Br62 with QC annotations

**Output files:**
- [AG006.braker_qc.filtered.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.braker_qc.filtered.gff3): Filtered BRAKER annotation of AG006
- [AG006.miniprot_qc.filtered.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.miniprot_qc.filtered.gff3): Filtered miniprot annotation of AG006
- [Br62.braker_qc.filtered.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.braker_qc.filtered.gff3): Filtered BRAKER annotation of Br62
- [Br62.miniprot_qc.filtered.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.miniprot_qc.filtered.gff3): Filtered miniprot annotation of Br62

## 3. Merge gene models

We merged the BRAKER and miniprot annotations using gffread. We then extracted CDS and protein sequences from merged GFF.

```bash
gffread --sort-alpha \
        --force-exons \
        -M \
        -K \
        AG006.braker_qc.filtered.gff3 \
        AG006.miniprot_qc.filtered.gff3 > \
        AG006.merged.gff3

gffread --sort-alpha \
        --force-exons \
        -M \
        -K \
        Br62.braker_qc.filtered.gff3 \
        Br62.miniprot_qc.filtered.gff3 > \
        Br62.merged.gff3

gffread -x AG006.merged.cds.fa \
        -g AG006.fa \
        AG006.merged.gff3

gffread -x Br62.merged.cds.fa \
        -g Br62.fa \
        Br62.merged.gff3

gffread -y AG006.merged.protein.fa \
        -g AG006.fa \
        AG006.merged.gff3

gffread -y Br62.merged.protein.fa \
        -g Br62.fa \
        Br62.merged.gff3
```

**Input files:**
- [AG006.braker_qc.filtered.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.braker_qc.filtered.gff3): Filtered BRAKER annotation of AG006
- [AG006.miniprot_qc.filtered.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/AG006.miniprot_qc.filtered.gff3): Filtered miniprot annotation of AG006
- [Br62.braker_qc.filtered.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.braker_qc.filtered.gff3): Filtered BRAKER annotation of Br62
- [Br62.miniprot_qc.filtered.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/5_gff_qc/Br62.miniprot_qc.filtered.gff3): Filtered miniprot annotation of Br62

**Output files:**
- [AG006.merged.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/AG006.merged.gff3): Merged annotation of AG006
- [Br62.merged.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/Br62.merged.gff3): Merged annotation of Br62
- [AG006.merged.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/AG006.merged.cds.fa): CDS extracted from merged annotation of AG006
- [Br62.merged.cds.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/Br62.merged.cds.fa): CDS extracted from merged annotation of Br62
- [AG006.merged.protein.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/AG006.merged.protein.fa): Protein sequences extracted from merged annotation of AG006
- [Br62.merged.protein.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/Br62.merged.protein.fa): Protein sequences extracted from merged annotation of Br62

## 4. Plot genome features

To plot the distribution of gene models, we used their middle positions. When a locus had multiple alternative transcripts, we used the middle position of the locus region and regarded them as a single gene. If any of the alternative transcripts was derived from miniprot or predicted to be a putative secreted protein, the locus was considered to code for a putative secreted protein. We used [secreted_protein_or_not.py](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/scripts/secreted_protein_or_not.py) to summarize the information.

**Input files:**
- [AG006.merged.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/AG006.merged.gff3): Merged annotation of AG006
- [AG006.proteins.secreted_proteins.final.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/AG006.proteins.secreted_proteins.final.fa): Putative secreted proteins extracted from the BRAKER annotation [AG006.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/AG006.gff3)
- [Br62.merged.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/Br62.merged.gff3): Merged annotation of Br62
- [Br62.proteins.secreted_proteins.final.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/Br62.proteins.secreted_proteins.final.fa): Putative secreted proteins extracted from BRAKER annotation [Br62.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/4_BRAKER_annotation/Br62.gff3)

**Output files:**
- [AG006.genes.tsv](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/AG006.genes.tsv): Table of gene models in AG006. Each row represents a gene model with the following columns: contig_name, position, secreted_or_not, transcript_ids.
- [Br62.genes.tsv](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/Br62.genes.tsv): Table of gene models in Br62. Each row represents a gene model with the following columns: contig_name, position, secreted_or_not, transcript_ids.

To plot genomic features, we run the scripts in [plot_genome_features.py](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/scripts/plot_genome_features.py) and [plot_mChrA_features.py](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/scripts/plot_mChrA_features.py) on Jupyter Notebook.

**Input files:**
- [AG006.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/AG006.fa): AG006 genome
- [Br62.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/2_genomes/Br62.fa): Br62 genome
- [AG006.genes.tsv](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/AG006.genes.tsv): Table of gene models in AG006. Each row represents a gene model with the following columns: contig_name, position, secreted_or_not, transcript_ids.
- [Br62.genes.tsv](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/Br62.genes.tsv): Table of gene models in Br62. Each row represents a gene model with the following columns: contig_name, position, secreted_or_not, transcript_ids.

**Output files:**
- [AG006_contig.tsv](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/AG006_contig.tsv): Table of AG006 contigs with the following columns: contig_name, No_genes, No_secreted_proteins, repeat_%, GC_%.
- [AG006_window.tsv](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/AG006_window.tsv): Table of AG006 genome features with the following columns: contig_name, start, end, No_genes, No_secreted_proteins, repeat_%, GC_%.
- [AG006.pdf](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/AG006.pdf): Plot of AG006 genome features (100-kbp window)
- [AG006_mChrA.pdf](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/AG006_mChrA.pdf): Plot of AG006 mChrA features (10-kbp window)
- [Br62_contig.tsv](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/Br62_contig.tsv): Table of Br62 contigs with the following columns: contig_name, No_genes, No_secreted_proteins, repeat_%, GC_%.
- [Br62_window.tsv](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/Br62_window.tsv): Table of Br62 genome features with the following columns: contig_name, start, end, No_genes, No_secreted_proteins, repeat_%, GC_%.
- [Br62.pdf](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/Br62.pdf): Plot of Br62 genome features (100-kbp window)
- [Br62_mChrA.pdf](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/7_plot_features/Br62_mChrA.pdf): Plot of Br62 mChrA features (10-kbp window)


## 5. Annotate proteins using InterProScan

We annotated the protein sequences using InterProScan.

```
interproscan.sh -i AG006.merged.protein.fa \
                -o AG006.merged.protein.interproscan_results.gff3 \
                -f gff3 \
                -t p \
                -cpu 60 \
                -dp \
                --goterms

interproscan.sh -i Br62.merged.protein.fa \
                -o Br62.merged.protein.interproscan_results.gff3 \
                -f gff3 \
                -t p \
                -cpu 60 \
                -dp \
                --goterms
```

**Input files:**
- [AG006.merged.protein.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/AG006.merged.protein.fa): Protein sequences extracted from merged annotation of AG006
- [Br62.merged.protein.fa](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/6_merged_annotation/Br62.merged.protein.fa): Protein sequences extracted from merged annotation of Br62

**Output files:**
- [AG006.merged.protein.interproscan_results.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/8_interproscan_results/AG006.merged.protein.interproscan_results.gff3): InterProScan results of AG006 protein sequences
- [Br62.merged.protein.interproscan_results.gff3](https://github.com/YuSugihara/Barragan_and_Latorre_et_al_2024/blob/main/8_interproscan_results/Br62.merged.protein.interproscan_results.gff3): InterProScan results of Br62 protein sequences

## 6. Version information

| Program        | Version    |
| -------------- | ---------- |
| *miniprot*     | v0.13-r248 |
| *gffread*      | v0.12.7    |
| *interproscan* | v5.67-99.0 |
| *python*       | v3.10.14   |
| *biopyhon*     | v1.83      |
| *pandas*       | v2.2.1     |
| *matplotlib*   | v3.8.3     |
| *seaborn*      | v0.13.2    |
| *numpy*        | v1.26.4    |
