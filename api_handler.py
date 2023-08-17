from datetime import datetime
from ortools.sat.python import cp_model
import pandas as pd
from fastapi import FastAPI, HTTPException
from models import Meeting


app = FastAPI()

conference_room_seats = 100
meetings = []


@app.get("/meetings")
def get_meetings():
    return {"meetings": meetings}


@app.post("/schedule_meeting")
def schedule_meeting(start_time: datetime or None = None,
                     end_time: datetime or None = None,
                     seats_required: int or None = None):
    for info in (start_time, end_time, seats_required):
        if info is None:
            raise HTTPException(status_code=400, detail="You must provide all the parameters.")

    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    model.Add(seats_required <= conference_room_seats)
    status = solver.Solve(model=model)
    if status != cp_model.OPTIMAL and status != cp_model.FEASIBLE:
        raise HTTPException(status_code=409,
                            detail="Meeting can't be scheduled because it exceeds the number of seats in the conference room.")
    start_time_minutes = start_time.hour*60 + start_time.minute
    end_time_minutes = end_time.hour*60 + end_time.minute
    i0 = model.NewIntervalVar(start_time_minutes, end_time_minutes-start_time_minutes, end_time_minutes, 'i0')
    overlap_check = list()
    overlap_check.append(i0)
    for meeting in meetings:
        meeting_start_time = meeting.start_time.hour*60 + meeting.start_time.minute
        meeting_end_time = meeting.end_time.hour*60 + meeting.end_time.minute
        i1 = model.NewIntervalVar(meeting_start_time, meeting_end_time-meeting_start_time, meeting_end_time, 'i1')
        overlap_check.append(i1)
    model.AddNoOverlap(overlap_check)
    status = solver.Solve(model=model)
    if status != cp_model.OPTIMAL and status != cp_model.FEASIBLE:
        raise HTTPException(status_code=409, detail="Meeting can't be scheduled because it is in conflict with other meetings")

    new_meeting = Meeting(start_time=start_time, end_time=end_time, seats_required=seats_required)
    meetings.append(new_meeting)
    print(new_meeting)
    return {"meeting": new_meeting}
