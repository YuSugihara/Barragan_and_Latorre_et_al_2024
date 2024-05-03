import pandas as pd
from Bio import SeqIO


isolate_name = "AG006" # or "Br62"

secretome_records = SeqIO.to_dict(SeqIO.parse(f"{isolate_name}.proteins.secreted_proteins.final.fa", "fasta"))

gff = pd.read_csv(f'{isolate_name}.merged.gff3', sep='\t', comment='#', header=None)
gff = gff[gff[2] == 'locus']

with open(f"{isolate_name}.genes.tsv", "w") as f:
    for i, row in gff.iterrows():
        chrom, _, _, start, end, _, strand, _, info = row
        transcript_ids = info.split(';transcripts=')[1].split(';')[0].split(',')
        secreted_protein = False
        for transcript_id in transcript_ids:
            if transcript_id in secretome_records:
                secreted_protein = True
            elif "SEC" in transcript_id:
                secreted_protein = True
        if secreted_protein:
            f.write("\t".join([chrom, str((start + end)/2), "secreted_protein", ",".join(transcript_ids)]) + '\n')
        else:
            f.write("\t".join([chrom, str((start + end)/2), "not_secreted_protein", ",".join(transcript_ids)]) + '\n')
