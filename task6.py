from typing import List, Tuple
def split_by_index(s: str, indexes: list) -> List[str]:
    start = 0 
    list_of_words = []
    for end in indexes:
        try:
            list_of_words.append(s[start: end])
            start = end 
        except:
            print('index out of index')
            list_of_words.append(s[end:])
        return list_of_words
