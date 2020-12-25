# CombinatorialPatternMatching
CS 221 Project by Alejandro Zapata Acosta

To test the project please run setup.py to install dependencies,
than run pattern_matching.py with python 3.6 and above.

Organization of the project files is as follows:

genome_generation.py 
    contains two functions related to the generation of a pseudo-random genome
    and reads of varying length and size.

    generate_genome(size) takes an integer as input and returns a string representing a genome
    made up of the nucleotides A C T G with a length of size.

    generate_reads(n_reads, read_length, genome) takes a number of reads to generate (int) as
    input, an int detailing the desired size for each read, and a string representing a genome
    from which to make reads. The function returns a list of strings representing n_reads number
    of reads, each with length read_length. 

matching_algorithms.py
    contains implementations for PatternMatchingWithSuffixArray and BetterBWT along with auxiliary
    functions used in the creation of the required inputs for each algorithm. 

    create_suffix_array(text) takes a string and creates a suffix array in the form of a list of tuples 
    (index, suffix)

    pattern_matching_with_suffix_array(text_len, pattern, suffix_array) implementation of 
    PatternMatchingWithSuffixArray according to section 9.6 of the textbook. Returns
    a tuple with the first and last index where a pattern can be found in suffix_array.

    better_BWT_matching(first_occurrence, last_column, pattern, count) implemenation of BetterBWT
    according to section 9.11 of the textbook. Returns the number of times a pattern is found
    in a text. The inputs must be created with the help of the following functions.

    create_first_occurrence(first_column)

    create_count(last_column)

    rotate_right(text, n)

    create_Mtext(text)

    an example of these four functions being used to create the inputs for BetterBWT is found within
    pattern_matching.py

pattern_matching.py
    This file contains the code used to test both algorithms. It creates a genome, reads, and uses both 
    algorithms using the same genome and reads. It prints to a file named "output.txt" which will contain the 
    time it took to execute each algorithm and the memory in bytes required for each algorithm. It will also
    label how many reads and length of read it used for each run. 
    By default, the program will run using genome_size = 100000, n_reads = 100000, and read_len = 100.

    test_suffix_array(human_genome, reads) takes a genome and a list of reads and applies the 
    PatternMatchingWithSuffixArray algorithm to it, outputting the time it took to execute in seconds and memory
    used in bytes.

    test_BWT(human_genome, reads) same as test_suffix_array. Contains code for generating prerequisites of the
    BetterBWT algorithm. 