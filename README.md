
## rest api получеия и дополнения данных

+ Создаем в базе подписку по имени героя комикса
+ По запросу получаем данные по названию с этим героем
+ Данные в формате _JSON_
+ Для получения информации о фильмах используется API [omdbapi.com](http://www.omdbapi.com)
+ для заполнения базы со стороннего api используется команда в crontab
+ подробно:
    http://nergilz.pythonanywhere.com/api/movies/ все данные по фильмам с указанными героями
    http://nergilz.pythonanywhere.com/api/create/ создаем имя героя

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

#### Получение токена
```bash
curl -X POST http://127.0.0.1:8000/api-token-auth/ --data "username=ad&password=adpass"
```
```bash
curl -X POST http://nergilz.pythonanywhere.com/api-token-auth/ --data "username=ad&password=adpass"
```

#### POST запрос - подписка по имени героя 
```bash
curl -u ad:adpass -X POST http://nergilz.pythonanywhere.com/api/create/ -H "Content-Type: application/json" -d "{'name':'Hulk'}"
```

#### Пример получения данных
```bash
curl -u ad:adpass GET http://nergilz.pythonanywhere.com/api/movies/
```
```bash
curl -LX GET http://nergilz.pythonanywhere.com/api/movies/ -H "Authorization: Token 8f4c9ab5ffc252f26c864c50ef85be400268c42d"
```

---

##### для проверки:
+ admin :  _ad_:_adpass_  

---

#### вопросы:
+ заполнение базы через management/command, можно было через celery, 
    но как сделать "на лету" при оформлении подписки я пока не знаю
+ перевод названия фильма вносить в админке

---
созданно как тестовое для [ооо"Expotestdrive"](https://potokconf.ru/)
