import json
import redis
import time

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

with open("json_file.json", "r", encoding="utf-8") as file:
   data = json.load(file)

def get_create_time(struct):
    if struct == 'string':
        start_time = time.time()
        redis_client.set("data_string", str(data))
        end_time = time.time()
        create_time.append((end_time - start_time) * 1000)
    elif struct == 'hset':
        start_time = time.time()
        redis_client.hset("data_hset", mapping={
            "data" : str(data)
        })
        end_time = time.time()
        create_time.append((end_time - start_time) * 1000)
    elif struct == 'zset':
        start_time = time.time()
        redis_client.zadd("data_zset", mapping={
            str(data) : 1
        })
        end_time = time.time()
        create_time.append((end_time - start_time) * 1000)
    elif struct == 'list':
        start_time = time.time()
        redis_client.lpush("data_list", str(data))
        end_time = time.time()
        create_time.append((end_time - start_time) * 1000)

def get_select_time(struct):
    if struct == 'string':
        start_time = time.time()
        redis_client.get("data_string")
        end_time = time.time()
        select_time.append((end_time - start_time) * 1000)
    elif struct == 'hset':
        start_time = time.time()
        redis_client.hgetall("data_hset")
        end_time = time.time()
        select_time.append((end_time - start_time) * 1000)
    elif struct == 'zset':
        start_time = time.time()
        redis_client.zrange("data_zset", 0, -1)
        end_time = time.time()
        select_time.append((end_time - start_time) * 1000)
    elif struct == 'list':
        start_time = time.time()
        redis_client.lrange("data_list", 0, -1)
        end_time = time.time()
        select_time.append((end_time - start_time) * 1000)

create_time = []
select_time = []
data_structures = ["string", "hset", "zset", "list"]

for i in range(len(data_structures)):
    get_create_time(data_structures[i])
    print(f"{data_structures[i]} create time: {create_time[i]}\n")

for i in range(len(data_structures)):
    get_select_time(data_structures[i])
    print(f"{data_structures[i]} select time: {select_time[i]}\n")

redis_client.close()