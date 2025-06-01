from pydantic import BaseModel

class Workout(BaseModel):
    date: str
    exercise_name: str
    set_order: int
    reps: int
    weight: float