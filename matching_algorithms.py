import operator
# 9.6 on online textbook, with many adjustments
def pattern_matching_with_suffix_array(text_len, pattern, suffix_array):
    text_len += 1 # plus one for $
    pattern_len = len(pattern)
    min_index = 0
    max_index = text_len - 1
    first = min_index
    last = max_index
    mid_index = 0

    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        if pattern > suffix_array[mid_index][1]:
            min_index = mid_index + 1
        else:
            max_index = mid_index

    mid_index = (min_index + max_index) // 2
    if pattern == suffix_array[mid_index][1][:pattern_len]:
        first = mid_index
    else:
        return f"{pattern} not in text"

    min_index = 0
    max_index = text_len - 1

    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        if pattern >= suffix_array[mid_index][1][:pattern_len]:
            min_index = mid_index + 1
        else:
            max_index = mid_index
    if pattern != suffix_array[max_index][1][:pattern_len]:
        max_index -= 1
    last = max_index
    return (first, last)

def better_BW_matching():
    pass

# bad implementation memory-wise
def create_suffix_array(text):
    text = text + "$"
    suffixes = [(i, text[i:]) for i in range(len(text))]
    suffixes.sort(key=lambda kv: kv[1])
    return suffixes

