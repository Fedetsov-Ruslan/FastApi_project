from fastapi import APIRouter
from repositories import TaskRepository
from scheamas import STaskAdd, STask, STaskId

router = APIRouter(prefix="/tasks", tags=["Тасочки"])



@router.post("")
async def add_task(task:STaskAdd) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok":True, "task_id":task_id}

@router.get("")
async def get_task() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks