from datetime import datetime
from pydantic import BaseModel, Field, SecretStr


class Meeting(BaseModel):

    """Representation of a meeting in the system"""

    # displaying an example for the user
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "start_time": "2023-10-23 17:00",
                    "end_time": "2023-10-23 19:00",
                    "seats_required": "50"
                }
            ]
        }
    # meeting properties
    start_time: datetime
    end_time: datetime
    seats_required: int

