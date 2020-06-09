
## rest api получеия и дополнения данных

+ Создаем в базе подписку по имени героя комикса
+ По запросу получаем данные по названию с этим героем
+ Данные в формате _JSON_
+ Для получения информации о фильмах используется API [omdbapi.com](http://www.omdbapi.com)
+ для заполнения базы со стороннего api используется команда в crontab
+ подробно:
    http://localhost:8080/api/movies/ здесь все данные по фильмам с указанными героями
    http://localhost:8080/api/create/ здесь создаем имя героя

### Требования (requirements)
+ [virtualenv](https://virtualenv.pypa.io/en/latest/)
+ [Python3](https://www.python.org/)
+ [crontab](https://help.ubuntu.ru/wiki/cron)
+ [Django](https://docs.djangoproject.com/)
+ [django-rest-framework](https://www.django-rest-framework.org/)

### API endpoints, через браузер
```bash
http://localhost:8080/api/movies/
http://localhost:8080/api/create/
http://localhost:8080/api/authtoken/token/login/
http://localhost:8080/api/authtoken/token/logout/
```
### Установка зависимостей
```bash
(venv)name@host:~/exemp pip3 install requirements.txt
```

###  Для обновления базы использовать [crontab](https://help.ubuntu.ru/wiki/cron)
#### запуск команды _tick_ с нужной периодичностью
```bash
./manage.py tick
``` 

#### Пример POST запроса на подниску
```bash
curl -u ad:adpass -X POST http://127.0.0.1:8000/api/create/ -H "Content-Type: application/json" -d "{'name':'Hulk'}"
```
#### Пример получения данных
```bash
curl -u ad:adpass GET http://127.0.0.1:8000/api/movies/
```

---

##### для проверки:
+ admin :  _ad_:_adpass_  

---

#### вопросы:
+ заполнение базы через management/command, можно было через celery, 
    но как сделать "на лету" при оформлении подписки я честно пока не знаю
+ логин по токену, можно но в условии нет
+ перевод писать руками в админке

---
созданно как тестовое для [ооо"Expotestdrive"](https://potokconf.ru/)