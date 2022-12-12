with open('data/unsorted_names.txt', 'r') as rf, open('data/sorted_name.txt', 'w') as wf:
    wf.writelines(sorted(rf.readlines()))
    
