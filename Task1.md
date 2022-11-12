1. Создать локальную директорию и инициировать ее для git:

mkdir
Gitinit
git init

2. Создать текстовый файл в директории и выполнить коммит

create gitlocal.txt
git add .
git status
git commit -m"description"

3. Создать удаленный репозиторий на GitHub

create "GitTrainee" on github

4. Отправить (Push) локальный репозиторий в GitHub

git push --set-upstream https://github.com/Artemio007/GitTrainee.git master

5. Создать новую ветку (назвать develop) и переключиться на нее

git branch develop
git checkout develop

6. Создать новую ветку от 'develop' и переключиться на нее

git branch develop1
git checkout develop1

7. Добавить первую строку в текстовый файл, выполнить коммит и отправить в репозиторий


added line to text file
git add .
git status
git commit -m"ADD"

8. Клонировать ваш репозиторий с GitHub в отдельную директорию

cd ..
git clone https://github.com/Artemio007/GitTrainee.git

9. Создать другую ветку от ветки 'develop' и переключиться на нее, используя клонированный
проект

git checkout develop
git branch new_develop

10. Добавить первую строку в текстовый файл (отличный от первой ветки), выполнить коммит и
отправить в удаленный реозиторий

create new.txt
git add .
git status
git commit -m"New add"

11. Переключиться на 'develop'

git checkout develop

12. Объединить (merge) первую ветку и отправить (push) изменения

git merge new_develop
git push

13. Объединить (merge) вторую ветку и отправить (push) изменения

git merge develop
git push

14. Разрешить конфликты, если необходимо

no conflicts 

15. Все использованные команды записать в отдельный файл и отправить в репозиторий под
именем Task1.md

ok