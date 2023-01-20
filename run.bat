@echo off
start msedge http://localhost:23901/
uvicorn main:app --reload --port 23901

REM gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
