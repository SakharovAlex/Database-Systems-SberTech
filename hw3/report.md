### Выполнение дз по CouchDB + PouchDB
#### Установил couchdb
<image src="./screenshots/CouchDBInstall.png">

#### Запустил контейнер с CouchDB
<image src="./screenshots/CouchDBRun.png">

#### Авторизовался, зайдя на http://127.0.0.1:5984/_utils
<image src="./screenshots/CouchDBAuthentication.png">

#### Создал базу данных через GUI
<image src="./screenshots/CouchDBCreate.png">

#### Создал документ с полем "name"
<image src="./screenshots/CouchDBCreateDoc.png">

#### Поменял в html файле путь на 25-й строке
```
http://admin:password@localhost:5984/my_db
```

#### Открыл html и нажал кнопку sync
<image src="./screenshots/HtmlSync.png">
##### Убедился, что отобразилась моя фамилия

#### Остановил контейнер с couchdb
<image src="./screenshots/CouchDBStop.png">

#### Убедился, что фамилия все еще отображается
<image src="./screenshots/HtmlSecondSync.png">
