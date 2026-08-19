from fastapi import FastAPI
app = FastAPI()
@app.get("/hello")
def hello():
    return {"message": "hello"}

users = []

@app.post("/users")
def create_user(name: str,age: int=None):
    user_id = len(users) +1
    user = {'id': user_id, 'name': name }
    if age is not None:
        user['age'] = age
    users.append(user)
    return user

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def gete_user(user_id: int):
    for user in users:
        if user['id'] == user_id:
            return user
    return {'error':'用户不存在'}

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, age: int=None):
    for user in users:
        if user['id'] == user_id:
            if name is not None:
                user['name'] = name
            if age is not None:
                user['age'] = age
            return user
        return {'error':'用户不存在'}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            users.pop(i)
            return {'message':'用户删除成功'}
    return {'error':'用户不存在'}

