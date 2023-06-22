## foodgram_tests
Тесты для проекта продуктовый помощник
### Требования
 - Соответствие имен проверяемых полей в Моделях:
   - User:
     - `username`
     - `password`
     - `email`
     - `first_name`
     - `last_name`
### Установка
 - Склонировать проект:
   - `git clone git@github.com:pelldis/foodgram_tests.git`
 - Скопировать папку tests в корневую папку с проектом foodgram:
   - `copy -r tests ../<foodgram directory>/`
 - Скопировать файлы `pytest.ini` и `run.sh` в корневую папку с проектом foodgram:
   - `copy pytest.ini ../<foodgram directory>/`
   - `copy run.sh ../<foodgram directory>/`
 - Установить pytest в venv foodgram проект:
   - `pip install pytest`
 - Возможно понадобится скорректировать переменные в pytest.ini:
   `python_paths = backend/`
   `DJANGO_SETTINGS_MODULE = foodgram.settings`
   ```
   Должна получиться примерно такая структура
    project
      backend/
        foodgram/
          settings.py
          ...
      frontend/
      tests/
      run.sh
      pytest.ini
      ...
    ```
 - Запустить тест из корневой дирректории проекта:
   - `pytest`
