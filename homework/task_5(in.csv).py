import csv


def get_top_age(file_path):
    global name_sorted
    error_lines_count = 0
    with open(file_path, "r") as file:
        data = list(csv.reader(file, delimiter=","))
    names = {}
    result = []
    in_digit_res = []
    keys_indexes_counter = 0
    for row in data[1:]:
        if row[0].isdigit() and "." not in row[0]:
            names[row[0]] = row[1:]
        else:
            error_lines_count += 1
            name_sorted = dict(sorted(names.items(), key=lambda x: x[0], reverse=True))
    keys_indexes = list(sorted(name_sorted.keys(), reverse=True))

    for el in name_sorted.values():

        if int(keys_indexes[keys_indexes_counter]) not in range(len(name_sorted.values()) + 1):
            error_lines_count += 1

        elif str(el[int(keys_indexes[keys_indexes_counter])]).isalpha() or \
                str(el[int(keys_indexes[keys_indexes_counter])]).isalnum() \
                and not str(el[int(keys_indexes[keys_indexes_counter])]).isdigit():
            error_lines_count += 1

        else:
            result.append(el[int(keys_indexes[keys_indexes_counter])])

        keys_indexes_counter += 1

    for digit in result:
        if digit.isdigit() or digit.isdigit() and "-" in digit.isdigit():
            in_digit_res.append(int(digit))
        elif "-" and "." in digit:
            in_digit_res.append(float(digit))
        elif "-" not in digit and "." in digit:
            in_digit_res.append(float(digit))
        else:
            print("error")
    print(f"error lines = {error_lines_count}")

    str_res = str(result).replace(", ", " + ")
    print(f"{str_res} = {sum(in_digit_res)}")
    return sum(in_digit_res)


print(get_top_age("data/for_task_5/in.csv"))
