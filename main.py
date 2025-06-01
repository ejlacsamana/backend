from fastapi import FastAPI
from models import Workout
from database import init_db
import sqlite3

app = FastAPI()
init_db()

@app.post("/workouts")
def add_workout (workout: Workout):
    conn = sqlite3.connect("workout_tracker.db")
    c = conn.cursor()
    c.execute("""INSERT INTO workouts(
              date, exercise_name, set_order, reps, weight
              ) VALUES(?, ?, ?, ?, ?)""", (
                  workout.date,
                  workout.exercise_name,
                  workout.set_order,
                  workout.reps,
                  workout.weight
              ))
    
    conn.commit()
    conn.close()
    return {"message": "Workout saved succcessfully!"}