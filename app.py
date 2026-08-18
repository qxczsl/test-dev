from fastapi import FastAPI
app = FastAPI()
@app.get("/hello")
def hello():
    return {"message": "hello"}

users = []

@app.post('/users')
def create_user(name: str, age: int = None):
    user_id = len(users) + 1
    user = {"id": user_id, "name": name}
    if age is not None:
        user["age"] = age
    users.append(user)
    return user
