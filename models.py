from datetime import datetime
from pydantic import BaseModel, Field, SecretStr


class Meeting(BaseModel):
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "start_date": "2023-10-23 17:00",
                    "end_date": "2023-10-23 19:00",
                    "seats_required": "50"
                }
            ]
        }
    start_date: datetime
    end_date: datetime
    seats_required: int

