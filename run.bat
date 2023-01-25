@echo on
start msedge http://localhost:23901/
uvicorn app.main:app --reload --port 23901

REM gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
