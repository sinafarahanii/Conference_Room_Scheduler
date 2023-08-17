# Conference Room Scheduler

## Description

Welcome to my project! This project is about handling common HTTP request and the difference between their APIs using FastAPI.
FastAPI is a modern, high performance, easy to use web framework for building APIs.

## Install

Note: It is assumed that you have python installed on your system.

In order yo use pip commands, you can make a virtual environment in your directory by running:

    python -m venv venv
then activate it by running: (on windows)

    venv\Scripts\activate.bat
    
Required packages are mentioned in `requriements.txt`.

Note: all packages are provided in the project but you can install them seperately.

You can install them by running:

    pip install -r requirements.txt
    
## Run the app

    uvicorn api_handler:app --reload

FastAPI provides you a client to test API requests in your project: <a href="http://127.0.0.1:8000/docs#/">`http://127.0.0.1:8000/docs#/`


## Test each method

You can test each method and each possible case by test functions provided in `test_api.py`.You can also can run all the tests at once by running:

        python test_api.py

## Contact
Contact me at my eamil address: sinafarahani@aut.ac.ir
