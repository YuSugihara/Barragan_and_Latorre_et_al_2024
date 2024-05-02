#! /usr/bin/env python3

import os
import sys
import pandas as pd
from Bio import SeqIO


gff_name = sys.argv[1]
protein_fasta_name = sys.argv[2]
nt_seq_len_check_points = [int(n) for n in sys.argv[3].split(',')]
masking_check_points = [int(n) for n in sys.argv[4].split(',')]

def read_gff(gff_name):
	gff = pd.read_csv(gff_name, sep='\t', header=None, comment='#', low_memory=False)
	gff = gff[gff[2]!='gene']
	gff['gene_id'] = gff[8].str.split(';').str[0].str.split('.').str[0].str.split('=').str[1]
	gff['transcript_id'] = gff[gff[2]!='mRNA'][8].str.split('Parent=').str[1].str.split(';').str[0]
	gff.loc[gff[2]=='mRNA', 'transcript_id'] = gff.loc[gff[2]=='mRNA'][8].str.split(';').str[0].str.replace('ID=', '')
	return gff

def read_fasta(protein_fasta_name):
	records_dict = SeqIO.to_dict(SeqIO.parse(protein_fasta_name, 'fasta'))
	return records_dict

def check_seq(nuc_seq):
	qc_list = []
	if nuc_seq[:3].upper() != 'ATG':
		qc_list.append('no_start_codon')
	if nuc_seq[-3:].upper() not in ['TGA', 'TAG', 'TAA']:
		qc_list.append('no_stop_codon')
	if len(nuc_seq) % 3 != 0:
		qc_list.append('not_multiple_of_3')
	else:
		aa_seq = nuc_seq.translate().rstrip('*')
		if '*' in aa_seq:
			qc_list.append('stop_codon_in_cds')
	if not nuc_seq.isupper():
		qc_list.append('masked_over_00')
		n_masked_base = nuc_seq.count('a') + nuc_seq.count('t') + nuc_seq.count('g') + nuc_seq.count('c')
		for masking_check_point in masking_check_points:
			if n_masked_base/len(nuc_seq) > masking_check_point/100:
				qc_list.append('masked_over_{}'.format(masking_check_point))
	for nt_seq_len_check_point in nt_seq_len_check_points:
		if len(nuc_seq) < nt_seq_len_check_point:
			qc_list.append('shorter_than_{}nt'.format(nt_seq_len_check_point))
	return '|'.join(qc_list)
		

gff = read_gff(gff_name)
records_dict = read_fasta(protein_fasta_name)

qc_lines = []
qc_lines_dict = {}
transcript_ids = list(gff['transcript_id'])
for transcript_id in transcript_ids:
	if transcript_id not in qc_lines_dict:
		nuc_seq = records_dict[transcript_id].seq
		qc_line = check_seq(nuc_seq)
		qc_lines_dict[transcript_id] = qc_line
		print(transcript_id, qc_line, sep='\t', file=sys.stderr)
	qc_lines.append(qc_lines_dict[transcript_id])

gff['qc'] = qc_lines
gff.to_csv(sys.stdout, sep='\t', header=None, index=False)
