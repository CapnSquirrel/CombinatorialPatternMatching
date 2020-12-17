# bad implementation memory-wise
def create_suffix_array(text):
    text = text + "$"
    suffixes = [(i, text[i:]) for i in range(len(text))]
    suffixes.sort(key=lambda kv: kv[1])
    return suffixes

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

def better_BW_matching(first_ocurrence, last_column, pattern, count):
    top = 0
    bottom = len(last_column) - 1
    
    while top <= bottom:
        if pattern != "":
            symbol = pattern[-1]
            pattern = pattern[:len(pattern)-1]
            if symbol in last_column[top:bottom+1]: # may be off by one
                symbol_fo = first_ocurrence[symbol]
                top = symbol_fo + count[top][symbol]
                bottom = symbol_fo + count[bottom+1][symbol] - 1
            else:
                return 0
        else:
            return bottom - top + 1

    return 0

def create_first_ocurrence(first_column):
    first_ocurrence = dict()
    for i, symbol in enumerate(first_column):
        if symbol not in first_ocurrence:
            first_ocurrence[symbol] = i
    return first_ocurrence

def create_count(last_column):
    symbols = sorted(set(last_column))
    counts = dict.fromkeys(symbols, 0)
    count_matrix = [dict.fromkeys(symbols, 0)]
    for char in last_column:
        counts[char] += 1
        count_matrix.append(counts.copy())

    return count_matrix

# rotate text to the right by n
def rotate_right(text, n):
    return text[-n:] + text[:-n]

# Need M(Text) matrix, BWT = last_column. 
def create_Mtext(text):
    CRM = []

    for n in range(len(text)):
        CRM.append(rotate_right(text, n))

    CRM.sort()
    return CRM

