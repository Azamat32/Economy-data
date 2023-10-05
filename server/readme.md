инструкция

на рабочем столе в папке config - создаем файл config.json
внутри :

{
    "database": {
      "name": "server",
      "user": "postgres",
      "password": "musakhan003"
    },
    "other_settings": {
      "SOME_SETTING": "value"
    }
}
  тут будут настройки бд. сохроняем

далее в каталоге server:
pip install -r requiremets.txt
python manage.py makemigartions
python manage.py migrate
python manage.py runserver
localhost:127.0.0.1 - пусто
localhost:127.0.0.1/api/....
... = topics : api topics
... = economic_indices : Макроэкономика разделы
... =  economic_index  : Макроэкономика раздел