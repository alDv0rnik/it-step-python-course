def new_data(data, new_value):
    if type(data) == list:
        data.append(new_value)
        return print(data)
    elif type(data) == set:
        data.add(new_value)
        return print(data)
    elif type(data) == str:
        if type(new_value) == list:
            return print(data)
        else:
            print(data + new_value)
    elif type(data) == int or type(data) == bool or type(data) == dict:
        return print(data)


new_data([1, 2, 3],'Kisi_Misi')
new_data({1, 2, 3},'Kisi_Misi')
new_data('Xagi_Vagi','Kisi_Misi')
new_data('Xagi_Vagi', [6, 6, 6])
new_data(666, 'Kisi_Misi')
new_data(True, 'Kisi_Misi')
new_data({1: 'x', 2: 'a', 3: 'g', 4: 'i'}, 'Kisi_Misi')



