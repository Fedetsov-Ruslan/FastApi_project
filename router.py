from fastapi import APIRouter
from repositories import TaskRepository
from scheamas import STaskAdd

router = APIRouter(prefix="/tasks", tags=["Тасочки"])



@router.post("")
async def add_task(task:STaskAdd):
    task_id = await TaskRepository.add_one(task)
    return {"ok":True, "task_id":task_id}

@router.get("")
async def get_home():
    tasks = await TaskRepository.find_all()
    return {"name":tasks}