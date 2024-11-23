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
4. [Вставляем этот ключ в] (https://github.com/settings/keys)
# Связать удаленный репозеторий
git remote add origin + ssh ключ
# Посмотреть связь с удаленным репозеторием
git remote -v
# Отправить данные в удаленный репозеторий
git push -u origin main

