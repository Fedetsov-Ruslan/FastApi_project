from sqlalchemy import select
from database import session, TaskOrm
from scheamas import STask, STaskAdd

class TaskRepository:
    @classmethod
    async def add_one(cls, data:STaskAdd):
        async with session() as s:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            s.add(task)
            await s.flush()
            await s.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with session() as s:
            query = select(TaskOrm)
            result = await s.execute(query)
            task_models = result.scalars().all()
            task_dict = [orm_to_dict(task_model) for task_model in task_models]
            task_schemas = [STask.model_validate(task) for task in task_dict]
            return task_schemas
        
def orm_to_dict(orm_model):
    return {column.name: getattr(orm_model, column.name) for column in orm_model.__table__.columns}
