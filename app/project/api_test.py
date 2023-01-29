import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from dotenv import dotenv_values
from pymongo import MongoClient

from app.project.apis import project_api as project_apiroutes

app = FastAPI()
config = dotenv_values(".env")
app.mongodb_client = MongoClient(config["CONNECTION_STRING"])
app.database = app.mongodb_client[config["DB_NAME"] + "_test"]
app.database["projects"].drop()
#app.mongodb_client.drop_database(config["DB_NAME"] + "_test")
app.include_router(project_apiroutes, tags=["projects"], prefix="/api/project")


def test_get_projects(capsys):
    with TestClient(app) as client:
        with capsys.disabled():
            print('Testing Scenario 1...')
        get_projects_response = client.get("/api/project/")
        assert get_projects_response.status_code == 200
 
def test_create_project():
    with TestClient(app) as client:
        response = client.post("/api/project/", json={"name": "Project 01a", "start": "2023-01-12","end": "2023-01-17", "desc": "New Project"})
        assert response.status_code == 201

        body = response.json()
        assert body.get("name") == "Project 01a"
        assert body.get("start") == "2023-01-12"
        assert body.get("end") == "2023-01-17"
        assert body.get("desc") == "New Project"
        assert "_id" in body

def test_create_project_missing_name():
    with TestClient(app) as client:
        response = client.post("/api/project/", json={"start": "2023-01-12","end": "2023-01-17", "desc": "New Project"})
        assert response.status_code == 422


def test_create_project_missing_start():
    with TestClient(app) as client:
        response = client.post("/api/project/", json={"name": "Project 01", "end": "2023-01-17", "desc": "New Project"})
        assert response.status_code == 422


def test_create_project_missing_end():
    with TestClient(app) as client:
        response = client.post("/api/project/", json={"name": "Project 01", "start": "2023-01-12", "desc": "New Project"})
        assert response.status_code == 422
        
def test_create_project_missing_desc():
    with TestClient(app) as client:
        response = client.post("/api/project/", json={"name": "Project 01", "start": "2023-01-12","end": "2023-01-17"})
        assert response.status_code == 422
        
def test_get_project():
    with TestClient(app) as client:
        new_project = client.post("/api/project/", json={"name": "Project 01b", "start": "2023-01-12","end": "2023-01-17", "desc": "New Project"}).json()

        get_project_response = client.get("/api/project/" + new_project.get("_id"))
        assert get_project_response.status_code == 200
        assert get_project_response.json() == new_project


def test_get_project_unexisting():
    with TestClient(app) as client:
        get_project_response = client.get("/api/project/unexisting_id")
        assert get_project_response.status_code == 404
        
def test_update_project():
    with TestClient(app) as client:
        new_project = client.post("/api/project/", json={"name": "Project 01c", "start": "2023-01-12","end": "2023-01-17", "desc": "New Project"}).json()

        response = client.post("/api/project/" + new_project.get("_id"), json={"name": "Project 01c - Updated"})
        assert response.status_code == 200
        assert response.json().get("name") == "Project 01c - Updated"


def test_update_project_unexisting():
    with TestClient(app) as client:
        update_project_response = client.post("/api/project/unexisting_id", json={"name": "Project - Updated"})
        assert update_project_response.status_code == 404  

def test_delete_project():
    with TestClient(app) as client:
        new_project = client.post("/api/project/", json={"name": "Project 01d", "start": "2023-01-12","end": "2023-01-17", "desc": "New Project"}).json()

        delete_project_response = client.delete("/api/project/" + new_project.get("_id"))
        assert delete_project_response.status_code == 204

def test_delete_project_unexisting():
    with TestClient(app) as client:
        delete_project_response = client.delete("/api/project/unexisting_id")
        assert delete_project_response.status_code == 404        