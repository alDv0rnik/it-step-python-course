# Задание 2 (I). Откройте файл data/unsorted_names.txt в папке данных. Сортируйте имена и
# записывайте их в новый файл sorted_names.txt. Каждое имя должно начинаться с новой строки,
# как в следующем примере:
# Adele
# Adrienne
# ...
# Willodean
# Xavier


with open('data/unsorted_names.txt') as in_file, open('sorted_names.txt', "w") as out_file:
    lst_read = sorted(in_file.read().split())
    str_sort = '\n'.join(lst_read)
    out_file.write(str_sort)




