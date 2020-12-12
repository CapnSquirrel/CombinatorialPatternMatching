# 9.6 on online textbook
def pattern_matching_with_suffix_array():
    pass

def better_BW_matching():
    pass


# suffix array creation
def create_suffix_array(text):
    text = text + "$"
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort(key=lambda x: x[0]) 
    return suffixes  
