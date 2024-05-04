import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Bio import SeqIO
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable


sns.set_style("ticks")

isolate_name = "AG006" # or "Br62"
genome = SeqIO.to_dict(SeqIO.parse(f"{isolate_name}.fa", "fasta"))
gene_table = pd.read_csv(f"{isolate_name}.genes.tsv", sep='\t', header=None)
output_contig_table = open(f"{isolate_name}_contig.tsv", "w")
output_window_table = open(f"{isolate_name}_window.tsv", "w")

def count_gc_content(seq):
    seq = seq.upper()
    gc_content = seq.count("G") + seq.count("C")
    return gc_content

def count_soft_masking(seq):
    return sum(1 for base in seq if base.islower())

window_size = 100000
cummulative_end_posi = 0
cummulative_end_posi_list = [0]
chrom_labels = []
x = []
gene_y = []
secreted_gene_y = []
repeat_y = []
gc_content_y = []
fig = plt.figure(figsize=(12, 3.1))
for chrom in gene_table[0].drop_duplicates():
    gene_posi = gene_table[gene_table[0] == chrom][1]
    secreted_gene_posi = gene_table[(gene_table[0] == chrom) & (gene_table[2] == 'secreted_protein')][1]
    end_posi = genome[chrom].seq.__len__()
    if end_posi < window_size:
        print(chrom)
        output_contig_table.write(f"{chrom}\t{len(gene_posi)}\t{len(secreted_gene_posi)}\t{100*count_soft_masking(genome[chrom].seq)/end_posi}\t{100*count_gc_content(genome[chrom].seq)/end_posi}\n")
        continue
    gene_cut = pd.cut(gene_posi, list(range(0, int(end_posi), window_size)) + [end_posi]).value_counts().sort_index()
    secreted_gene_cut = pd.cut(secreted_gene_posi, list(range(0, int(end_posi), window_size)) + [end_posi]).value_counts().sort_index()
    x = x + list(cummulative_end_posi + np.array([k.left for k in gene_cut.keys()]))
    gene_y = gene_y + list(gene_cut)
    secreted_gene_y = secreted_gene_y + list(secreted_gene_cut)
    for k in gene_cut.keys():
        seq = genome[chrom].seq[k.left:k.right]
        repeat_y.append(100*count_soft_masking(seq)/window_size)
        gc_content_y.append(100*count_gc_content(seq)/window_size)
        output_window_table.write(f"{chrom}\t{k.left}\t{k.right}\t{gene_cut[k]}\t{secreted_gene_cut[k]}\t{100*count_soft_masking(seq)/window_size}\t{100*count_gc_content(seq)/window_size}\n")
    cummulative_end_posi += end_posi + window_size
    cummulative_end_posi_list.append(cummulative_end_posi)
    chrom_labels.append(chrom)
    output_contig_table.write(f"{chrom}\t{gene_cut.sum()}\t{secreted_gene_cut.sum()}\t{100*count_soft_masking(genome[chrom].seq)/end_posi}\t{100*count_gc_content(genome[chrom].seq)/end_posi}\n")
cmap1 = plt.get_cmap('plasma')
cmap2 = plt.get_cmap('winter')
cmap3 = plt.get_cmap('summer')
cmap4 = plt.get_cmap('gist_ncar_r')
norm1 = Normalize(vmin=0, vmax=50)
norm2 = Normalize(vmin=0, vmax=20)
norm3 = Normalize(vmin=0, vmax=80)
norm4 = Normalize(vmin=20, vmax=max(gc_content_y))
ax1 = fig.add_subplot(4, 1, 1)
ax2 = fig.add_subplot(4, 1, 2)
ax3 = fig.add_subplot(4, 1, 3)
ax4 = fig.add_subplot(4, 1, 4)
ax1.bar(np.array(x)/window_size, gene_y, width=1, linewidth=0, color=cmap1(norm1(gene_y)), align='edge')
ax2.bar(np.array(x)/window_size, secreted_gene_y, width=1, linewidth=0, color=cmap2(norm2(secreted_gene_y)), align='edge')
ax3.bar(np.array(x)/window_size, repeat_y, width=1, linewidth=0, color=cmap3(norm3(repeat_y)), align='edge')
ax4.bar(np.array(x)/window_size, gc_content_y, width=1, linewidth=0, color=cmap4(norm4(gc_content_y)), align='edge')
for end_posi in cummulative_end_posi_list:
    ax1.axvline(end_posi/window_size, color='black', linewidth=0.5, linestyle='--', lw=0.7)
    ax2.axvline(end_posi/window_size, color='black', linewidth=0.5, linestyle='--', lw=0.7)
    ax3.axvline(end_posi/window_size, color='black', linewidth=0.5, linestyle='--', lw=0.7)
    ax4.axvline(end_posi/window_size, color='black', linewidth=0.5, linestyle='--', lw=0.7)
sm1 = ScalarMappable(cmap=cm.plasma, norm=norm1)
sm2 = ScalarMappable(cmap=cm.winter, norm=norm2)
sm3 = ScalarMappable(cmap=cm.summer, norm=norm3)
sm4 = ScalarMappable(cmap=cm.gist_ncar_r, norm=norm4)
ax1.set_xlim(0, cummulative_end_posi/window_size)
ax2.set_xlim(0, cummulative_end_posi/window_size)
ax3.set_xlim(0, cummulative_end_posi/window_size)
ax4.set_xlim(0, cummulative_end_posi/window_size)
ax4.set_ylim(25, 55)
ax1.set_xticks(ticks=[])
ax2.set_xticks(ticks=[])
ax3.set_xticks(ticks=[])
ax1.set_yticks([0, 25, 50])
ax2.set_yticks([0, 10, 20])
ax3.set_yticks([0, 40, 80])
ax1.tick_params(axis='both', which='major', labelsize=6)
ax2.tick_params(axis='both', which='major', labelsize=6)
ax3.tick_params(axis='both', which='major', labelsize=6)
ax4.tick_params(axis='both', which='major', labelsize=6)
cbar1 = fig.colorbar(sm1, ax=ax1, fraction=0.1, pad=0.01, aspect=7)
cbar2 = fig.colorbar(sm2, ax=ax2, fraction=0.1, pad=0.01, aspect=7)
cbar3 = fig.colorbar(sm3, ax=ax3, fraction=0.1, pad=0.01, aspect=7)
cbar4 = fig.colorbar(sm4, ax=ax4, fraction=0.1, pad=0.01, aspect=7)
cbar1.ax.set_yticks([0, 25, 50])
cbar2.ax.set_yticks([0, 10, 20])
cbar3.ax.set_yticks([0, 40, 80])
cbar4.ax.set_yticks([30, 40, 50])
cbar1.ax.tick_params(labelsize=6)
cbar2.ax.tick_params(labelsize=6)
cbar3.ax.tick_params(labelsize=6)
cbar4.ax.tick_params(labelsize=6)
plt.xticks(np.array(cummulative_end_posi_list[:-1])/window_size, labels=chrom_labels, rotation=45, ha='right')
plt.tight_layout(pad=0.3)
plt.savefig(f"{isolate_name}.pdf")
plt.show()

output_contig_table.close()
output_window_table.close()
