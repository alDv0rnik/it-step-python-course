def get_pairs(lst: list):
    list_result = []
    if len(lst) == 1:
        return None
    else:
        for i in range(len(lst)-1):
            list_result.append((lst[i], lst[i + 1]))
        return list_result


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))



