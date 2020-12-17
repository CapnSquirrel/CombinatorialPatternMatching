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
    genome_size = 20
    n_reads = 1
    read_len = 3

    human_genome = gg.genereate_genome(genome_size)
    reads = gg.generate_reads(n_reads, read_len, human_genome)
    pattern = reads[0]
    last_column = ""
    first_column = ""
    Mtext = ma.create_Mtext(human_genome + "$")
    for line in Mtext:
        last_column = last_column + line[-1]
        first_column = first_column + line[0]
        print(line)
    print("text: ", human_genome)
    print("last column: ", last_column)
    print("first column: ", first_column)
    first_occurrence = ma.create_first_occurrence(first_column)
    print("first occurrence: ", first_occurrence)
    count = ma.create_count(last_column)
    for thing in count:
        print(thing)
    print("pattern", pattern)
    print(ma.better_BWT_matching(first_occurrence, last_column, pattern, count))

test_BWT()