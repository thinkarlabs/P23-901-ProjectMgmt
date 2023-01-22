from fastapi import FastAPI, Request, Form
from dotenv import dotenv_values
from pymongo import MongoClient
from app.routes import router as project_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

config = dotenv_values(".env")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mongodb_client = MongoClient(config["CONNECTION_STRING"])
app.database = app.mongodb_client[config["DB_NAME"]]

@app.get("/")
async def index(request: Request):
  return FileResponse('static/index.html')

app.include_router(project_router, tags=["projects"], prefix="/api/project")
