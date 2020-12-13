import genome_generation as gg
import matching_algorithms as ma
# import timeit
# from sys import getsizeof

genome_size = 10
n_reads = 10 # X
read_len = 1 # Y

human_genome = gg.genereate_genome(genome_size)
reads = gg.generate_reads(n_reads, read_len, human_genome)

# start = timeit.default_timer()

suffix_array = ma.create_suffix_array(human_genome)

# stop = timeit.default_timer()
# print('Time: ', stop - start)  
# print(getsizeof(suffix_array))

for k, v in suffix_array.items():
    print(k, v)

for pattern in reads:
    print(ma.pattern_matching_with_suffix_array(human_genome, pattern, suffix_array))
    # print(pattern)