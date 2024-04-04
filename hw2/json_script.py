import json
import random
import string

data = []

# Генерируем случайные данные для заполнения JSON файла
for _ in range(500000):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    random_number = random.randint(1, 1000)
    data.append({"random_string": random_string, "random_number": random_number})

# Записываем данные в JSON файл
with open("json_file.json", "w") as file:
    json.dump(data, file)
