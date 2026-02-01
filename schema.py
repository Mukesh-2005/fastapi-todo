from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int

# Set Pydantic configuration after class definition to avoid defining
# both `model_config` and `Config` inside the class (which raises an error).
import pydantic as _pydantic
if getattr(_pydantic, "__version__", "").startswith("2"):
    Todo.model_config = {"from_attributes": True}
else:
    class _Config:
        orm_mode = True
    Todo.Config = _Config