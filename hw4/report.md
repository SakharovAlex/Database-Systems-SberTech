### Выполнение дз по Chroma DB
#### История развития СУБД

Chroma - open-source векторная база данных, появившаяся совсем недавно, точнее, первый релиз на GitHub состоялся 22 октября 2022 года. Так как сейчас очень часто применяют методы машинное обучение, то векторные базы данных становятся все более популярны, соответсвенно, Chroma очень быстро набрала свою популярность.

#### Инструменты взаимодействия
С данной бд можно взаимодействовать на языке Python и JavaScript

#### Database Engine
В Chroma DB используется SQLite

#### Query Language
Запросы выполняется через различные методы коллекции. Пример:
```
import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)
```
Так мы создали коллекцию и добавили в нее какую-то информацию. Теперь сделаем запрос:
```
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)
```
Получим:
```
{'ids': [['id1', 'id2']], 'distances': [[0.7110877633094788, 1.0109351873397827]], 'metadatas': [[{'source': 'my_source'}, {'source': 'my_source'}]], 'embeddings': None, 'documents': [['This is a document', 'This is another document']], 'uris': None, 'data': None}
```
Также в запросах есть ```where``` фильтр.
Например, в данном запросе:
```
collection.query(
    query_embeddings=[[11.1, 12.1, 13.1],[1.1, 2.3, 3.2], ...],
    n_results=10,
    where={"metadata_field": "is_equal_to_this"},
    where_document={"$contains":"search_string"}
)
```
Фильтруем метаданные по связям с определенными документами.
```where_document``` используется для фильтрации по содержимому документа.
Поддерживаются такие операторы:
```
$eq - equal to (string, int, float)
$ne - not equal to (string, int, float)
$gt - greater than (int, float)
$gte - greater than or equal to (int, float)
$lt - less than (int, float)
$lte - less than or equal to (int, float)
```
Получаем, что:
```
{
    "metadata_field": "search_string"
}

# is equivalent to

{
    "metadata_field": {
        "$eq": "search_string"
    }
}
```
Можно использовать ```$and``` и ```$or``` для комбинации фильтров.
```
{
    "$and": [
        {
            "metadata_field": {
                <Operator>: <Value>
            }
        },
        {
            "metadata_field": {
                <Operator>: <Value>
            }
        }
    ]
}
```
Существуют операторы включения:
```
$in - a value is in predefined list (string, int, float, bool)
$nin - a value is not in predefined list (string, int, float, bool)
```
Пример:
```
{
  "metadata_field": {
    "$in": ["value1", "value2", "value3"]
  }
}

{
  "metadata_field": {
    "$nin": ["value1", "value2", "value3"]
  }
}
```
#### На каком языке/ах программирования написана Chroma?
Благо Chroma - open-source база данных, так что можно все посмотреть на GitHub-е.
<image src="./Languages.png">

#### Какие типы индексов поддерживаются в БД? Приведите пример создания индексов.
Chroma DB автоматически создает индекс. В случае его повреждения или несинхронизации с embedding-ом запросы не будут выполнены.

