from typing import List, Tuple 

def get_pairs(lst: List) -> List[Tuple]:
    return [(lst[i], lst[i+1]) for i in range (len(lst)-1)]


lst =[1,2,3,4,5]
print(get_pairs(lst))
