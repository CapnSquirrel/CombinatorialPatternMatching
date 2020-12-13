import random

def genereate_genome(size):
    nucleobases = ["A", "C", "T", "G"]
    genome = ""
    for _ in range(size):
        genome += nucleobases[random.randint(0, 3)]
    return genome

def generate_reads(n_reads, read_length, genome):
    reads = []
    genome_length = len(genome)
    for _ in range(n_reads):
        start = random.randint(0, genome_length - read_length) 
        read = "".join([genome[x] for x in range(start, start + read_length)])
        reads.append(read)
        
    return reads