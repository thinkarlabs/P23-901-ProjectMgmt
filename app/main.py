from fastapi import FastAPI, Request, Form
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.project.models import AnyJson

config = dotenv_values(".env")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mongodb_client = MongoClient(config["CONNECTION_STRING"])
app.database = app.mongodb_client[config["DB_NAME"]]


from app.project.apis import project_api as project_apiroutes
app.include_router(project_apiroutes, tags=["projects"], prefix="/api/project")

app_users = {
	'admin01@thinkar.org':{'pwd':'pass@admin01','role':'admin'},
	'admin02@thinkar.com':{'pwd':'pass@admin02','role':'admin'},
	'cand01@thinkar.com':{'pwd':'pass@cand01','role':'user'},
	'cand02@thinkar.com':{'pwd':'pass@cand02','role':'user'},
	'cand03@thinkar.com':{'pwd':'pass@cand03','role':'user'}
}
#app.database["projects"].drop()

@app.get("/")
async def index(request: Request):
  return FileResponse('static/index.html')

@app.post("/api/login")
async def index(request: Request):
  #form = await request.form() #- only gets this on form post - not on $ajax post.
  #form = await request.body() #- give a b'' string
  form = await request.json()
  print ('Form is : ',form['id'])
  #data = {k: v for k, v in form.items() if k != "upload-file"}

  #print ('Data is : ',data)
  if (form['id'] in app_users):
    if (app_users[form['id']]['pwd'] == form['pwd']):
        print(app_users[form['id']]['role'])
        return "OK"
    else:
        return "OK"
  else:
    return "OK"
  
