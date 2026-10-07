from django.db import models
from abc import ABC, abstractmethod
# Create your models here.
class BaseEntity(ABC):

    @abstractmethod
    def validate(self):
        pass

    def to_dict(self):
        return {
            key:value for key, value in self.__dict__.items()
        }


class Reporter(BaseEntity):
    def __init__(self,id,name,email,team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team    

    def validate(self):
        if not self.name:
            raise ValueError("Name can not define")

        if '@' not in self.email:
            raise ValueError("Email id is not correct")
        


class Issue(BaseEntity):
    def __init__(self, id, title, description, status, priority, reporter_id, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = created_at


    def validate(self):
        if not self.title:
            raise ValueError("The title should not be empty")

        if not self.description:
            raise ValueError("The description should not be empty")

        if not self.status:
            raise ValueError("The status should not be empty")

        if not self.priority:
            raise ValueError("The priority should not be empty")

        if not self.reporter_id:
            raise ValueError("Reporter ID cannot be empty")

        if not self.created_at:
            raise ValueError("Created date cannot be empty")

    def describe(self):
        return f"{self.title} [{self.priority}]"


class CriticalIssue(Issue):
    def describe(self):
        return f"[URGENT] {self.title} - need to take immediate attention"


class LowerPriorityIssue(Issue):
    def describe(self):
        return f"{self.title} - low priority when you free"