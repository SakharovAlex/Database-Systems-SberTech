## Выполнение ДЗ по Redis

### Генерация JSON:
Для генерации большого json файла использовал скрипт
```
json_script.py
```
в котором создается json с рандомной строкой и рандомным числом и получил файл
```
json_file.json
```
### Работа с Redis
  
 #### Скачал Redis через
 ```
 brew install redis
```
<image src="./screenshots/RedisInstallation.png">

#### Создал образ с помощью
```
docker build -t redis .
```
<image src="./screenshots/RedisBuild.png">

#### Запустил контейнер и зашел в него
```
docker run -d redis
docker exec -it <container_name> bash
```
<image src="./screenshots/RedisRun.png">

#### Замерил время с помощью
```
python3 main.py
```
<image src="./screenshots/SpeedTest.png">


### Развертывание redis кластера в docker контейнерах

#### Поднял контейнеры с помощью
```
docker compose up -d
```
<image src="./screenshots/DockerCompose.png">

#### Связал три ноды друг с другом
```
docker exec -it first redis-cli --cluster create first:8001 second:8002 third:8003 --cluster-replicas 0
```
<image src="./screenshots/3NodesConnection.png">
  

#### Проверил статус работы redis кластера
```
docker exec -it first redis-cli --cluster check first:8001
```
<image src="./screenshots/StatusCheck.png">
