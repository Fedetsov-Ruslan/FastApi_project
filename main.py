from fastapi import FastAPI

from contextlib import asynccontextmanager

from router import router as task_router
from database import create_table, delete_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("база очещена")
    await create_table()
    print("база готова к работе")
    yield
    print("выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)







