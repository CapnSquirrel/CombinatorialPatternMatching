import genome_generation as gg
import matching_algorithms as ma
import timeit
# from sys import getsizeof

def test_suffix_array():
    genome_size = 150000
    n_reads = 10000 # X
    read_len = 100 # Y

    human_genome = gg.genereate_genome(genome_size)
    reads = gg.generate_reads(n_reads, read_len, human_genome)

    start = timeit.default_timer()

    suffix_array = ma.create_suffix_array(human_genome)
    for pattern in reads:
        ma.pattern_matching_with_suffix_array(len(human_genome), pattern, suffix_array)

    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    # print(getsizeof(suffix_array))

def test_BWT():
    genome_size = 5
    # n_reads = 1
    # read_len = 3

    human_genome = gg.genereate_genome(genome_size)
    # reads = gg.generate_reads(n_reads, read_len, human_genome)
    
    BWT = ""
    for line in ma.create_Mtext(human_genome + "$"):
        BWT = BWT + line[-1]
        print(line)
    print(BWT)

test_BWT()