from sqlalchemy import select
from database import session, TaskOrm
from scheamas import STaskAdd

class TaskRepository:
    @classmethod
    async def add_one(cls, data:STaskAdd):
        async with session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
        
    @classmethod
    async def find_all(cls):
        async with session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_model = result.scalars().all()
            return task_model