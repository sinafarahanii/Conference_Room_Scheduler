import requests
import json
import pytest


def test_get_meetings():
    response = requests.get("http://127.0.0.1:8000/meetings")
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting():
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "2023-10-23 17:00",
                                                                               "end_time": "2023-10-23 19:00",
                                                                               "seats_required": 50})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting_missing_parameters():
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting_giving_wrong_type():
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "this is start_time",
                                                                               "end_time": "2023-10-23 19:00"})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting_overlap_with_other_meetings():
    # first meeting
    requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "2023-10-23 17:00",
                                                                    "end_time": "2023-10-23 19:00",
                                                                    "seats_required": 50})
    # second meeting
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "2023-10-23 18:00",
                                                                               "end_time": "2023-10-23 20:00",
                                                                               "seats_required": 50})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting_seats_exceeding_conference_room_capacity():
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "2023-10-23 17:00",
                                                                               "end_time": "2023-10-23 19:00",
                                                                               "seats_required": 150})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting_giving_negative_value_seats():
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "2023-10-23 17:00",
                                                                               "end_time": "2023-10-23 19:00",
                                                                               "seats_required": -50})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting_start_time_older_than_current_date():
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "2023-01-23 17:00",
                                                                               "end_time": "2023-10-23 19:00",
                                                                               "seats_required": 50})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting_end_time_is_before_start_time():
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "2023-10-23 17:00",
                                                                               "end_time": "2023-10-22 19:00",
                                                                               "seats_required": 50})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


def test_schedule_meeting_start_time_and_end_time_are_in_different_dates():
    response = requests.post("http://127.0.0.1:8000/schedule_meeting", params={"start_time": "2023-10-23 17:00",
                                                                               "end_time": "2023-10-24 19:00",
                                                                               "seats_required": 50})
    assert response.status_code == 200, f"{response.json()}"
    print(response.json())


if __name__ == '__main__':
    pytest.main()
