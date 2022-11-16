1. Создать локальную директорию и инициировать ее для git
   B Git Bash перехожу на нужный диск и в соответсвующие папки: 
   cd ..
   cd  мой путь расположения папки
   Создаю локальную директорию:
   mkdir lesson5_Tribuhova
   Проверяю создалась ли директория:
   ls
   Перейду в директорию:
   cd lesson5_Tribuhova
   Инициировать ее для git:
   git init
   Посмотрим создалась ли системная папка(ls - не покажет):
   ls -a
   Если проинициировали не ту директорию - отменяем:
   rm -rf .git
2. Создать текстовый файл в директории и выполнить коммит
   Созданию файл:
   touch mytext.txt
   Просматриваю создался ли:
   ls
   Выполняю коммит:
   git add . (либо git add mytext.txt)
   git status (должен быть зеленым)
   git commit -m "File created"(либо запустить редактор commit)
   Либо можно заменить 2 команды одной : git commit -am "File created"
3. Создать удаленный репозиторий на GitHub(название как у локальной директории)
   На сайте github->new repository->public -> add a readme file -> add .gitignore(выбрала Python)
   ->в settings переименовала main в master-> update -> Create
   В Git Bash:
   Создаю связь(добавляю удаленный источник данных):
   git remote add original https://github.com/Marina8619/lesson5_Tribuhova.git
   Для проверки смотрю список соединений(должны быть 2 записи с fetch и с push):
   git remote -v
   Подтягиваю изменения с удаленного репозитория:
   git pull origin master
   Проверяю сколько веток:
   git branch -a
   Выполняю commit после объединения репозиториев:
   git add .
   git commit -m "Merging repositories"

4. Отправить (Push) локальный репозиторий в GitHub
   git push origin master
   Не отправился по причине того, что после git init был commit на создание файла
   Просмотрю историю:
   git log (или git log --oneline)
   Смотрю ветки:
   git branch (на како ветке нахожусь)
   git branch -a (зеленым вижу мою, красным удаленную)
   git branch --set-upstream-to=origin/master master
   Комментарий программы: branch 'master' set up to track 'origin/master'(Теперь мой мастер отслеживает мастер на ремоуте)
   отменяю предыдущие измения:
   Удалила тестовый файл из локального репозитория:
   rm mytxt.txt
   git revert хэш нужного коммита(i->esc->:wq для выхода из редактора)
   git pull --rebase
   Комментарий программы: Successfully rebased and updated refs/heads/master.
   git push(без ошибок)
   ls -a (вижу папки из удаленного репо ./  ../  .git/  .gitignore  README.md)
   Делаю снова 2 пункт задания: 
   Созданию файл:
   touch mytext.txt
   Просматриваю создался ли:
   ls
   Выполняю коммит:
   git add . (либо git add mytext.txt)
   git status (должен быть зеленым)
   git commit -m "File created"(либо запустить редактор commit)
   git push(удаленный репозиторий увидел папку)   
5. Создать новую ветку (назвать develop) и переключиться на нее
   git branch
   git checkout -b develop
7. Добавить первую строку в текстовый файл, выполнить коммит и отправить в репозиторий
   echo "The first string" > mytext.txt
   cat mytext.txt
   git add .
   git commit -m "The first string"
   git push --set-upstream origin develop(вижу на git hub и ветку developer и и mytext.txt с добавленной строкой)
8. Клонировать ваш репозиторий с GitHub в отдельную директорию
   mkdir dir_point8
   ls
   cd dir_point8
   git clone https://github.com/Marina8619/lesson5_Tribuhova.git
   cd lesson5_Tribuhova
9. Создать другую ветку от ветки 'develop' и переключиться на нее, используя клонированный проект
   git branch
   git checkout develop
   git branch develop1 develop
   git checkout develop1
10. Добавить первую строку в текстовый файл (отличный от первой ветки), выполнить коммит и
отправить в удаленный реозиторий
    echo new line > mytext.txt
    cat mytext.txt
    ls -l
    git add .
    git commit -m "Added another line"
    git branch
    git push origin develop1_new
11. Переключиться на 'develop'
    git branch
    git checkout develop
    git branch 
12. Объединить (merge) первую ветку и отправить (push) изменения
    git merge develop1
    git commit -m "The first merging of branches"
13. Объединить (merge) вторую ветку и отправить (push) изменения
    Нет второй ветки, т.к объединение репозиториев прошло успешно
14. Разрешить конфликты, если необходимо
    Нет конфликтов
15. Все использованные команды записать в отдельный файл и отправить в репозиторий под
именем Task1.md
   Зашла по ссылке преподавателя -> fork -> название -> описание-> убрала V -> create fork
   code -> копирую ссылкe-> в командной строке в переходим в нужную папку-> клонируем git clone + ссылка
   dir -> зашла в папку -> 
   git branch
   git branch -a
   Чтобы локальный репозиторий отслеживал изменения удаленного
   git remote add upstream https://github.com/Marina8619/Tribuhova_Marina_lesson5.git
   Убеждаемся:
   git config --local -l
   Добавляем файл
   touch tribuhova_lesson5.md
   dir
   вставляю инструкцию как выполнила задание
   git status
   add tribuhova_lesson5.md
   git status
   touch .gitignore
   внести .idea\
          .gitignore
   dir
   git status
   git commit -m "Create file md"
   git log
   Если надо меняем config
   push origin master
   В git hub pull request