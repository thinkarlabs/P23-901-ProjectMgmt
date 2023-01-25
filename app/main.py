from fastapi import FastAPI, Request, Form
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

config = dotenv_values(".env")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mongodb_client = MongoClient(config["CONNECTION_STRING"])
app.database = app.mongodb_client[config["DB_NAME"]]


from app.project.apis import project_api as project_apiroutes
app.include_router(project_apiroutes, tags=["projects"], prefix="/api/project")

@app.get("/")
async def index(request: Request):
  return FileResponse('static/index.html')

