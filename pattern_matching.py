import genome_generation as gg
import matching_algorithms as ma
import timeit
from guppy import hpy
import sys
sys.stdout = open("output.txt", "a")

def test_suffix_array(human_genome, reads):
    if reads == []:
        return 
    
    h.setrelheap() # measure memory starting here
    start = timeit.default_timer()
    suffix_array = ma.create_suffix_array(human_genome)
    
    for pattern in reads:
        ma.pattern_matching_with_suffix_array(len(human_genome), pattern, suffix_array) # memory used up by function is lost

    stop = timeit.default_timer()
    print('Suffix array time: ', stop - start)
    print('Suffix array memory', h.heap().size) 
      
def test_BWT(human_genome, reads):
    if reads == []:
        return 
    
    h.setrelheap() # measure memory starting here
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
    
    for pattern in reads:
        ma.better_BWT_matching(first_occurrence, last_column, pattern, count) # memory used up by function is lost

    stop = timeit.default_timer()
    print('BetterBWT time: ', stop - start)
    print('BetterBWT memory', h.heap().size)  

h = hpy()
genome_size = 100000
n_reads = 100000
read_len = 100

human_genome = gg.genereate_genome(genome_size)
reads = gg.generate_reads(n_reads, read_len, human_genome)

print(f"{n_reads} reads, read length of {read_len}")
test_suffix_array(human_genome, reads)
test_BWT(human_genome, reads)
