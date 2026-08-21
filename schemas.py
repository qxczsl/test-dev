# schemas.py —— Pydantic 请求/响应模型（接口收什么参数、返什么格式）

from pydantic import BaseModel
from datetime import datetime


# ===== User 相关 =====

class UserCreate(BaseModel):
    name: str
    age: int | None = None


class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    age: int | None = None
    created_at: datetime | None = None

    class Config:
        from_attributes = True


# ===== Order 相关 =====

class OrderCreate(BaseModel):
    user_id: int
    product_name: str
    amount: float
    status: int = 1


class OrderUpdate(BaseModel):
    product_name: str | None = None
    amount: float | None = None
    status: int | None = None


class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_name: str
    amount: float
    status: int
    created_at: datetime | None = None

    class Config:
        from_attributes = True
