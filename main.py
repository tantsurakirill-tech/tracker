from datetime import datetime

from repositories.task import TaskRepository
from settings import Session


with Session() as session:
    task_repo = TaskRepository(session)
    task_repo.create(
        name='Task_1',
        user_id=1,
        deadline=datetime.now(),
        commit=True
    )

    task = task_repo.get_by_id(1)
    print(task)
