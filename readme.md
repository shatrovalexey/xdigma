### ПОИСК СВОБОДНЫХ РЕСУРСОВ НА ОРБИТАХ ПЛАНЕТ ###

### ТРЕБОВАНИЯ ###
* Python v>=3.6
* `apt-get install python3-selenium chromium-chromedriver`
* cp 'chromedriver' '/usr/lib/chromium-browser/chromedriver'

### ЗАПУСК ###
* `python3 run.py --login="${LOGIN}" --password="${PASSWORD}"` - просмотр всех галактик и систем
* `python3 run.py --login="${LOGIN}" --password="${PASSWORD}" --galaxy=${GALAXY}` - просмотр указанной галактики
* `python3 run.py --login="${LOGIN}" --password="${PASSWORD}" --galaxy=${GALAXY} --system=${SYSTEM}` - просмотр указанной системы в указанной галактике
* `python3 run.py --login="${LOGIN}" --password="${PASSWORD}" --galaxy_from=${GALAXY_FROM} --galaxy_from=${GALAXY_TO} - просмотр галактик от и до
* `python3 run.py --login="${LOGIN}" --password="${PASSWORD}" --galaxy_from=${GALAXY_FROM} --galaxy_from=${GALAXY_TO} --system=${SYSTEM} - просмотр только указанной системы галактик от и до
* `python3 run.py --login="${LOGIN}" --password="${PASSWORD}" --galaxy_from=${GALAXY_FROM} --galaxy_from=${GALAXY_TO} --system_from=${SYSTEM_FROM} --system_to=${SYSTEM_TO} - просмотр только систем от и до галактик от и до
* за просмотр каждой страницы игрой взимается 300 водорода

### АВТОР ###
Шатров Алексей Сергеевич <mail@ashatrov.ru>