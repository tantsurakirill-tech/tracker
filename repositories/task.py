from datetime import datetime

from models import Task


class TaskRepository:

    def __init__(self, session):
        self.session = session

    def all(self) -> list[Task]:
        return self.session.query(Task).all()

    def get_by_id(self, id: int) -> Task:
        return self.session.get(Task, id)

    def create(
        self,
        name: str,
        user_id: int | None = None,
        deadline: datetime | None=None,
        category_id: int | None = None,
        priority: str = "low",
        commit: bool = False
    ) -> Task:
        task = Task(
            name=name,
            user_id=user_id,
            deadline=deadline,
            category_id=category_id,
            priority=priority
        )
        self.session.add(task)

        if commit:
            self.session.commit()
        else:
            self.session.flush()

        return task