# database.py —— MySQL 连接配置

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# ① 连接 URL：告诉 SQLAlchemy 怎么连 MySQL
DATABASE_URL = "mysql+aiomysql://root:root@127.0.0.1:3306/test_dev"

# ② 创建异步引擎：底层管 TCP 连接池
engine = create_async_engine(DATABASE_URL, echo=True)

# ③ 创建会话工厂：每次操作数据库时从这里拿一个 session
async_session = async_sessionmaker(engine, expire_on_commit=False)

# ④ FastAPI 依赖：接口用 Depends(get_db) 自动注入 session
async def get_db():
    async with async_session() as session:
        yield session
