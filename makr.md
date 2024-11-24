# Создание локально репозетория и привязка к GIT
1. Создаем папку, заходим в нее. Вводим git init
2. Задаем настройки по умолчанию через команду git config --global + название настройки
Например: git config --global user.name "Bibanin Ivan Ivanovich"
user.email=bibaninivan1988@gmail.com
git config --global core.autocrlf=input
git config --global core.safecrlf=warn
git config --global core.quotepath=off
git config --global init.defaultbranch=main
Посмотреть настройки можно через git config --global --list
# Создание SSH ключа
1. Вводим в терминале ssh-keygen
2. Нажимаем несколько раз на ENTER
3. Открываем фаил через cat (Например cat .ssh/id_rsa.pub)
4. -[Вставляем этот ключ в] (https://github.com/settings/keys)
# Связать удаленный репозеторий
git remote add origin + ssh ключ
# Посмотреть связь с удаленным репозеторием
git remote -v
# Отправить данные в удаленный репозеторий
git push -u origin + название ветки (main стандартная)
# Ветки
1. Посмотреть ветки: git branch 
2. Создать ветку: git branch + название ветки
3. Переключиться на ветку: git checkaut + название ветки
# Ветки (просмотр истории)
Просмотр истории конкретной ветки: git log + название ветки --oneline
# Слияние веток
git merge + название ветки из которой хотим взять изменение (находится в той ветке куда хотим слить изменения)
# Добавить в отслеживание и сразу закомитить
git commit -A -m "Название комита"
# Заменить предыдущий комит
git commit --amend -m "Название комита"
# Принять данные с удаленного репозитория
git pull
# Отмена комита
- сохраняется история
- заходим в лог git log --oneline, копируем хэш комита на который хотим вернуться
git revert +номер хэша 
- далее откроется терминал где нужно будет задать название коммита или оставить старое