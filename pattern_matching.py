from genome_generation import generate_reads
from genome_generation import genereate_genome

genome_size = 1000000
X = 100000
Y = 100

human_genome = genereate_genome(genome_size)
reads = generate_reads(X, Y, human_genome)