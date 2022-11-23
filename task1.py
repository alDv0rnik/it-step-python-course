def concat(*string, sep=" "):
    return sep.join(map(str, string))

items = ('My' 'name' 'is' 'Vadim')
print(concat(items))




