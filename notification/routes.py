from flask import jsonify

from notification import app, db


@app.route("/create", methods=["post"])
def create():
    """
    - user_id - строка на 24 символа (является ObjectID документа пользователя которому отправляется уведомление)
    - target_id - строка на 24 символа (является ObjectID документа сущности, к которой относится уведомление) (Может отсутствовать)
    - key - ключ уведомления enum
        - registration (Только отправит пользователю Email)
        - new_message (только создаст запись в документе пользователя)
        - new_post (только создаст запись в документе пользователя)
        - new_login (Создаст запись в документе пользователя и отправит email)
    - data - произвольный объект из пар ключ/значение (Может отсутствовать)


{
    "user_id": "638f394d4b7243fc0399ea67",
    "key": "registration",
}

HTTP 201 Created


{
    "success": true,
}
    """
    # online_users = mongo.db.users.find({"online": True})
    return jsonify({"name": "create"})


@app.route('/list', methods=["get"])
def list_notification():
    collections = db.list_collection_names()
    print(collections)
    for collection in collections:
        print(collection)
    """
#### query params
- user_id [string] - идентификатор пользователя
- skip [int] - кол-во уведомлений, которые следует пропустить
- limit [int] - кол-во уведомлений которые следует вернуть
#### Пример ответа

HTTP 200 Ok

```json
{
    "success": true,
    "data": {
        "elements": 23, // всего уведомлений
        "new": 12, // Кол-во непрочитанных уведомлений
        "request": {
            "user_id": "638f394d4b7243fc0399ea67",
            "skip": 0,
            "limit": 10,
        }
        "list": [
            {
                "id": "some_notification_id",
                "timestamp": 1698138241,
                "is_new": false,
                "user_id": "638f394d4b7243fc0399ea67",
                "key": "new_message",
                "target_id": "0399ea67638f394d4b7243fc",
                "data": {
                    "some_field": "some_value"
                },
            },
            ...
        ]
    }
}
```
    """
    return jsonify({"name": "list"})


@app.route('/read', methods=["post"])
def read():
    """
#### query params
- user_id [string] - идентификатор пользователя
- notification_id [string] - Идентификатор уведомления

#### Пример ответа

HTTP 200 Ok

```json
{
    "success": true,
}
    """
    return jsonify({"name": "read"})