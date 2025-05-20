from dataclasses import dataclass


@dataclass
class TaskCreateDTO:
    title: str
    description: str = ""


@dataclass
class TaskDTO:
    id: int
    title: str
    description: str
    created_at: str
