from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import user

from database import get_db
from models import User
from schemas import UserCreate,UserUpdate

app = FastAPI()
@app.get("/hello")
def hello():
    return {"message": "hello"}




@app.post("/users")
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(name=user_data.name, age=user_data.age)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@app.get('/users')
async def get_users(db:AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


@app.get('/users/{user_id}')
async def get_user(user_id: int,db: AsyncSession = Depends(get_db)):
    user = await db.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user

@app.put("/users/{user_id}")
async def update_user(user_id: int,user_data: UserUpdate, db: AsyncSession = Depends(get_db)):
    user = await db.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    data = user_data.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(user, key, value)# 等价于 user.name = value / user.age = value
    await db.commit()
    await db.refresh(user)
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int,db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    await db.delete(user)
    await db.commit()
    return {"message": "用户删除成功"}