with open('unsorted_names.txt', 'r') as f:
    sort_names = sorted(str(f.read()).split('\n'))


with open('sorted_names.txt', 'w') as f:
    for i in sort_names:
        f.write(f'{i}\n')
