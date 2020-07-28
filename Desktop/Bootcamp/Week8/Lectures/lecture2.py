# http --> HyperText Transfer Protocol
# TCP, SMTP, FTP --> Read

# Метод запроса (GET, POST, PATCH, PUT, DELETE) URI HTTP/версия

# Метод запроса - определяет какую операцию нужно осуществить с ресурсом

# URI - идентификатор ресурса, путь до конкретного ресурса (документа), над которым мы хотим произвести действие

# Версия - определяет какую именно версию стандарта HTTP используем в запросе

# Example: GET /products HTTP/1.1 - стартовая строка HTTP запроса

# GET /money HTTP/2.0 - gets info without changing on server
# Host: yandex.ru

# import requests
# res = requests.get('https://yandex.ru/money')

# HTTP/Версия Код состояния пояснения

# HTTP/1.1 200 OK 
# Server: Apacher/2.0
# Date: 09, Apr 2020 22:24:56 UTC+6
# Content-Type: application /json
# Content-Length: 100

# {"id":1, "name": 'Apple', "city": "Cupertino"}

# HTTP/2.0 200 OK
# Server: nginx
# Date: Sun, 26 Jul 2020 22:11:59 UTC
# Content-Type: text/html 
# Content-Length: 159
# Connection: keep-alive

# <html>
# <head></head>
# <body></body>
# </html>


# GET - для запроса содержимого ресурса                   !!!!!!!!!!!!!!!!!!!!!!!!!!!
# GET /money?param1=value1&param2=value2 HTTP/1.1

# POST -  для передачи пользовательских данных на сервер
# POST /login HTTP/1.1
# headers
# username=nurbuster&password=qwerty


# PUT, PATCH - для изменения каких-то данных на сервере

# DELETE - удаляет указанный ресурс 


# 1** - информационный
# 2** - success
# 3** - перенаправление 
# 4** - ошибка клиениа
# 5** - ошибка сервера

# 2** - success
# 200 OK - success
# 201 Created - если мы успешно создали что-то на сервере
# 202 Accepted - запрос принят успешно, но он еще в обработке 
# 204 No Content - сервер успешно обработан, но в ответе нет тела
# 400 Bad request - сервер обнаружил ошибку в отправляемых данных
# 401 Unauthorized - когда обращение к ресурсу требуется аутентификация

# аутентификация - подтверждение личности
# авторизация - подтверждение прав на выполнение 

# 403 Forbidden - сервер отказывает в каком-то действии, из-за недостатка прав
# 404 Not Found - сервер не может найти запрошенный ресурс
# 405 Method Not Allowed - указанный метод невозможно применить к ресурсу
# 500 Internal Server Error - любая внутренняя ошибка
# 501 Not Implemented - сервер не понимает метод 
# 502 Bad Gateway - сервер в роли шлюза и прокси не получает ответа от вышестоящего сервева 
# 503 Service Unavailable 
# 504 Gateway Timeout

