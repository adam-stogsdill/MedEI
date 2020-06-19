import Gene_Engine.gene_base as gb

gene = open('F:/MedEI/gene_samples/sars2-genome', 'r')
x = "".join([line for line in gene])
print("Done Reading!")
gene = gb.Gene("Sars-2", x)

gene.describe()
