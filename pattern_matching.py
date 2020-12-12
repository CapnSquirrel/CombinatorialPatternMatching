from genome_generation import generate_reads
from genome_generation import genereate_genome
from matching_algorithms import create_suffix_array
import timeit

genome_size = 64900
n_reads = 10 # X
read_len = 10 # Y

human_genome = genereate_genome(genome_size)
reads = generate_reads(n_reads, read_len, human_genome)

start = timeit.default_timer()

suffix_array = create_suffix_array(human_genome)

stop = timeit.default_timer()

print('Time: ', stop - start)  

# for item in suffix_array:
#     print(item)