import genome_generation as gg
import matching_algorithms as ma
import timeit
from guppy import hpy

def test_suffix_array(human_genome, reads):

    start = timeit.default_timer()

    suffix_array = ma.create_suffix_array(human_genome)

    for pattern in reads:
        ma.pattern_matching_with_suffix_array(len(human_genome), pattern, suffix_array)

    stop = timeit.default_timer()
    print('Suffix array time: ', stop - start)  
    print(h.heap())

def test_BWT(human_genome, reads):

    start = timeit.default_timer()

    last_column = ""
    first_column = ""
    Mtext = ma.create_Mtext(human_genome + "$")
    for line in Mtext:
        last_column = last_column + line[-1]
        first_column = first_column + line[0]
        # print(line)
    # print("text: ", human_genome)
    # print("last column: ", last_column)
    # print("first column: ", first_column)
    first_occurrence = ma.create_first_occurrence(first_column)
    # print("first occurrence: ", first_occurrence)
    count = ma.create_count(last_column)
    # for thing in count:
    #     print(thing)
    # print("pattern", pattern)

    for pattern in reads:
        ma.better_BWT_matching(first_occurrence, last_column, pattern, count)

    stop = timeit.default_timer()
    print('Better BWT time: ', stop - start)
    print(h.heap())  

h = hpy()
genome_size = 100000
n_reads = 20000
read_len = 200

human_genome = gg.genereate_genome(genome_size)
reads = gg.generate_reads(n_reads, read_len, human_genome)

test_suffix_array(human_genome, reads)
test_BWT(human_genome, reads)
