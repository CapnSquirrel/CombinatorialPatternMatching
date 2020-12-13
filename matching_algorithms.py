import operator
# 9.6 on online textbook
def pattern_matching_with_suffix_array(text, pattern, suffix_array):
    n = len(text)
    min_index = 0
    max_index = n - 1
    first = min_index
    last = max_index

    # print(pattern, suffix_array[min_index])

    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        if pattern > suffix_array[mid_index]:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    print(pattern + "$", suffix_array[mid_index])
    if pattern == suffix_array[mid_index]:
        first = mid_index
    else:
        return f"{pattern} not in text"

    min_index = first
    max_index = n - 1

    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        if pattern > suffix_array[mid_index]:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    last = max_index
    return (first, last)

def better_BW_matching():
    pass

# bad implementation memory-wise
def create_suffix_array(text):
    text = text + "$"
    suffixes = dict()
    for i in range(len(text)):
        suffixes[i] = text[i:]

    return dict(sorted(suffixes.items(), key=lambda kv: kv[1]))   
