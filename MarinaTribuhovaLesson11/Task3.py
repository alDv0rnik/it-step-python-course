# Задача 3 (I) Напишите анонимную функцию, которая принимает на вход Имя и Фамилию, а
# выводит текст «Меня зовут <Имя> <Фамилия>. Обратить внимание на регистр значений

func = lambda name, surname: f"My name is {name.title()} {surname.title()}"


print(func("marina", "tribuhova"))


